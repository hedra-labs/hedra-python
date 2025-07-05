#!/usr/bin/env python3
"""
Face Memory System for Hedra CLI
SQLite-based face recognition database for persistent identity storage
"""

import sqlite3
import os
import json
import pickle
import numpy as np
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import shutil


class FaceMemory:
    """
    SQLite-based face recognition database
    Stores face embeddings, labels, and metadata for persistent identity recognition
    """
    
    def __init__(self, db_path: str = None):
        """
        Initialize face memory database
        
        Args:
            db_path: Path to SQLite database file (defaults to ~/.hedra_faces.db)
        """
        if db_path is None:
            db_path = os.path.expanduser("~/.hedra_faces.db")
        
        self.db_path = db_path
        self.face_crops_dir = os.path.join(os.path.dirname(db_path), "face_crops")
        
        # Create face crops directory
        os.makedirs(self.face_crops_dir, exist_ok=True)
        
        # Initialize database
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Face identities table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS faces (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    label TEXT NOT NULL,
                    name TEXT,
                    embedding BLOB,
                    first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                    confidence_avg REAL DEFAULT 0.0,
                    image_count INTEGER DEFAULT 1,
                    metadata TEXT,
                    UNIQUE(label)
                )
            ''')
            
            # Face recognition history table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS face_recognitions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    face_id INTEGER,
                    image_path TEXT,
                    confidence REAL,
                    bounding_box TEXT,
                    crop_path TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(face_id) REFERENCES faces(id)
                )
            ''')
            
            # Projects table (for future chaining feature)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(name)
                )
            ''')
            
            # Project clips table (for future chaining feature)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS project_clips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id INTEGER,
                    clip_order INTEGER,
                    face_label TEXT,
                    dialogue TEXT,
                    output_path TEXT,
                    input_image TEXT,
                    generation_id TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(project_id) REFERENCES projects(id)
                )
            ''')
            
            # Create indexes for performance
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_faces_label ON faces(label)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_recognitions_face_id ON face_recognitions(face_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_recognitions_timestamp ON face_recognitions(timestamp)')
            
            conn.commit()
    
    def save_face(self, label: str, embedding: np.ndarray, name: str = None, 
                  image_path: str = None, bbox: Tuple[int, int, int, int] = None,
                  confidence: float = 1.0, metadata: Dict = None) -> int:
        """
        Save a face to the database
        
        Args:
            label: Face label (e.g., "host", "guest", "john")
            embedding: Face embedding vector
            name: Optional real name
            image_path: Source image path
            bbox: Face bounding box (x, y, w, h)
            confidence: Recognition confidence
            metadata: Additional metadata
            
        Returns:
            Face ID in database
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if face already exists
            cursor.execute('SELECT id FROM faces WHERE label = ?', (label,))
            existing_face = cursor.fetchone()
            
            if existing_face:
                # Update existing face
                face_id = existing_face[0]
                self._update_existing_face(cursor, face_id, embedding, confidence, metadata)
            else:
                # Insert new face
                face_id = self._insert_new_face(cursor, label, embedding, name, metadata)
            
            # Save face crop if image provided
            crop_path = None
            if image_path and bbox:
                crop_path = self._save_face_crop(face_id, image_path, bbox)
            
            # Record recognition event
            self._record_recognition(cursor, face_id, image_path, confidence, bbox, crop_path)
            
            conn.commit()
            return face_id
    
    def _insert_new_face(self, cursor, label: str, embedding: np.ndarray, 
                        name: str = None, metadata: Dict = None) -> int:
        """Insert new face into database"""
        embedding_blob = pickle.dumps(embedding)
        metadata_json = json.dumps(metadata) if metadata else None
        
        cursor.execute('''
            INSERT INTO faces (label, name, embedding, metadata)
            VALUES (?, ?, ?, ?)
        ''', (label, name, embedding_blob, metadata_json))
        
        return cursor.lastrowid
    
    def _update_existing_face(self, cursor, face_id: int, embedding: np.ndarray, 
                             confidence: float, metadata: Dict = None):
        """Update existing face with new embedding (average with existing)"""
        # Get current embedding
        cursor.execute('SELECT embedding, confidence_avg, image_count FROM faces WHERE id = ?', (face_id,))
        row = cursor.fetchone()
        
        if row:
            current_embedding = pickle.loads(row[0])
            current_confidence = row[1]
            image_count = row[2]
            
            # Average embeddings (weighted by confidence)
            weight_current = current_confidence * image_count
            weight_new = confidence
            total_weight = weight_current + weight_new
            
            if total_weight > 0:
                averaged_embedding = (current_embedding * weight_current + embedding * weight_new) / total_weight
            else:
                averaged_embedding = embedding
            
            # Update face
            new_confidence = (current_confidence * image_count + confidence) / (image_count + 1)
            embedding_blob = pickle.dumps(averaged_embedding)
            metadata_json = json.dumps(metadata) if metadata else None
            
            cursor.execute('''
                UPDATE faces 
                SET embedding = ?, last_seen = CURRENT_TIMESTAMP, 
                    confidence_avg = ?, image_count = image_count + 1, metadata = ?
                WHERE id = ?
            ''', (embedding_blob, new_confidence, metadata_json, face_id))
    
    def _record_recognition(self, cursor, face_id: int, image_path: str = None, 
                           confidence: float = 1.0, bbox: Tuple[int, int, int, int] = None,
                           crop_path: str = None):
        """Record face recognition event"""
        bbox_str = f"{bbox[0]},{bbox[1]},{bbox[2]},{bbox[3]}" if bbox else None
        
        cursor.execute('''
            INSERT INTO face_recognitions (face_id, image_path, confidence, bounding_box, crop_path)
            VALUES (?, ?, ?, ?, ?)
        ''', (face_id, image_path, confidence, bbox_str, crop_path))
    
    def _save_face_crop(self, face_id: int, image_path: str, bbox: Tuple[int, int, int, int]) -> str:
        """Save cropped face image for verification"""
        try:
            import cv2
            
            # Load image
            img = cv2.imread(image_path)
            if img is None:
                return None
            
            # Crop face
            x, y, w, h = bbox
            face_crop = img[y:y+h, x:x+w]
            
            # Generate crop filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            crop_filename = f"face_{face_id}_{timestamp}.jpg"
            crop_path = os.path.join(self.face_crops_dir, crop_filename)
            
            # Save crop
            cv2.imwrite(crop_path, face_crop)
            
            return crop_path
            
        except Exception as e:
            print(f"⚠️  Could not save face crop: {e}")
            return None
    
    def find_similar_faces(self, embedding: np.ndarray, threshold: float = 0.8) -> List[Dict]:
        """
        Find similar faces in database
        
        Args:
            embedding: Face embedding to match
            threshold: Similarity threshold (0.0 to 1.0)
            
        Returns:
            List of matching faces with similarity scores
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, label, name, embedding, confidence_avg, image_count, last_seen
                FROM faces
            ''')
            
            matches = []
            for row in cursor.fetchall():
                face_id, label, name, embedding_blob, confidence_avg, image_count, last_seen = row
                
                stored_embedding = pickle.loads(embedding_blob)
                similarity = self._calculate_similarity(embedding, stored_embedding)
                
                if similarity >= threshold:
                    matches.append({
                        'face_id': face_id,
                        'label': label,
                        'name': name,
                        'similarity': similarity,
                        'confidence_avg': confidence_avg,
                        'image_count': image_count,
                        'last_seen': last_seen
                    })
            
            # Sort by similarity (highest first)
            matches.sort(key=lambda x: x['similarity'], reverse=True)
            return matches
    
    def find_face_by_label(self, label: str) -> Optional[Dict]:
        """
        Find face by label
        
        Args:
            label: Face label to search for
            
        Returns:
            Face information dict or None if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, label, name, embedding, confidence_avg, image_count, 
                       first_seen, last_seen, metadata
                FROM faces WHERE label = ?
            ''', (label,))
            
            row = cursor.fetchone()
            if row:
                face_id, label, name, embedding_blob, confidence_avg, image_count, first_seen, last_seen, metadata = row
                
                return {
                    'face_id': face_id,
                    'label': label,
                    'name': name,
                    'embedding': pickle.loads(embedding_blob),
                    'confidence_avg': confidence_avg,
                    'image_count': image_count,
                    'first_seen': first_seen,
                    'last_seen': last_seen,
                    'metadata': json.loads(metadata) if metadata else None
                }
            
            return None
    
    def list_faces(self) -> List[Dict]:
        """
        List all faces in database
        
        Returns:
            List of face information dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, label, name, confidence_avg, image_count, 
                       first_seen, last_seen
                FROM faces
                ORDER BY last_seen DESC
            ''')
            
            faces = []
            for row in cursor.fetchall():
                face_id, label, name, confidence_avg, image_count, first_seen, last_seen = row
                
                faces.append({
                    'face_id': face_id,
                    'label': label,
                    'name': name,
                    'confidence_avg': confidence_avg,
                    'image_count': image_count,
                    'first_seen': first_seen,
                    'last_seen': last_seen
                })
            
            return faces
    
    def delete_face(self, label: str) -> bool:
        """
        Delete face from database
        
        Args:
            label: Face label to delete
            
        Returns:
            True if deleted, False if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get face ID
            cursor.execute('SELECT id FROM faces WHERE label = ?', (label,))
            row = cursor.fetchone()
            
            if not row:
                return False
            
            face_id = row[0]
            
            # Delete recognition records
            cursor.execute('DELETE FROM face_recognitions WHERE face_id = ?', (face_id,))
            
            # Delete face crops
            cursor.execute('SELECT crop_path FROM face_recognitions WHERE face_id = ?', (face_id,))
            for (crop_path,) in cursor.fetchall():
                if crop_path and os.path.exists(crop_path):
                    try:
                        os.remove(crop_path)
                    except Exception:
                        pass
            
            # Delete face
            cursor.execute('DELETE FROM faces WHERE id = ?', (face_id,))
            
            conn.commit()
            return True
    
    def update_face_label(self, old_label: str, new_label: str) -> bool:
        """
        Update face label
        
        Args:
            old_label: Current label
            new_label: New label
            
        Returns:
            True if updated, False if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if old label exists
            cursor.execute('SELECT id FROM faces WHERE label = ?', (old_label,))
            if not cursor.fetchone():
                return False
            
            # Check if new label already exists
            cursor.execute('SELECT id FROM faces WHERE label = ?', (new_label,))
            if cursor.fetchone():
                raise ValueError(f"Label '{new_label}' already exists")
            
            # Update label
            cursor.execute('UPDATE faces SET label = ? WHERE label = ?', (new_label, old_label))
            conn.commit()
            return True
    
    def get_face_history(self, label: str, limit: int = 10) -> List[Dict]:
        """
        Get recognition history for a face
        
        Args:
            label: Face label
            limit: Maximum number of records to return
            
        Returns:
            List of recognition records
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT fr.image_path, fr.confidence, fr.bounding_box, fr.crop_path, fr.timestamp
                FROM face_recognitions fr
                JOIN faces f ON fr.face_id = f.id
                WHERE f.label = ?
                ORDER BY fr.timestamp DESC
                LIMIT ?
            ''', (label, limit))
            
            history = []
            for row in cursor.fetchall():
                image_path, confidence, bounding_box, crop_path, timestamp = row
                
                bbox = None
                if bounding_box:
                    try:
                        bbox = tuple(map(int, bounding_box.split(',')))
                    except Exception:
                        pass
                
                history.append({
                    'image_path': image_path,
                    'confidence': confidence,
                    'bounding_box': bbox,
                    'crop_path': crop_path,
                    'timestamp': timestamp
                })
            
            return history
    
    def export_database(self, export_path: str) -> bool:
        """
        Export database to backup file
        
        Args:
            export_path: Path for backup file
            
        Returns:
            True if successful
        """
        try:
            # Copy database file
            shutil.copy2(self.db_path, export_path)
            
            # Copy face crops directory
            export_dir = os.path.dirname(export_path)
            crops_backup_dir = os.path.join(export_dir, "face_crops_backup")
            
            if os.path.exists(self.face_crops_dir):
                shutil.copytree(self.face_crops_dir, crops_backup_dir, dirs_exist_ok=True)
            
            return True
            
        except Exception as e:
            print(f"⚠️  Export failed: {e}")
            return False
    
    def import_database(self, import_path: str) -> bool:
        """
        Import database from backup file
        
        Args:
            import_path: Path to backup file
            
        Returns:
            True if successful
        """
        try:
            # Backup current database
            if os.path.exists(self.db_path):
                backup_path = self.db_path + ".backup"
                shutil.copy2(self.db_path, backup_path)
            
            # Copy imported database
            shutil.copy2(import_path, self.db_path)
            
            # Import face crops if available
            import_dir = os.path.dirname(import_path)
            crops_import_dir = os.path.join(import_dir, "face_crops_backup")
            
            if os.path.exists(crops_import_dir):
                shutil.copytree(crops_import_dir, self.face_crops_dir, dirs_exist_ok=True)
            
            return True
            
        except Exception as e:
            print(f"⚠️  Import failed: {e}")
            return False
    
    def clear_database(self) -> bool:
        """
        Clear all faces from database
        
        Returns:
            True if successful
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Delete all records
                cursor.execute('DELETE FROM face_recognitions')
                cursor.execute('DELETE FROM faces')
                cursor.execute('DELETE FROM project_clips')
                cursor.execute('DELETE FROM projects')
                
                conn.commit()
            
            # Remove face crops
            if os.path.exists(self.face_crops_dir):
                shutil.rmtree(self.face_crops_dir)
                os.makedirs(self.face_crops_dir, exist_ok=True)
            
            return True
            
        except Exception as e:
            print(f"⚠️  Clear failed: {e}")
            return False
    
    def get_database_stats(self) -> Dict:
        """
        Get database statistics
        
        Returns:
            Statistics dictionary
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Count faces
            cursor.execute('SELECT COUNT(*) FROM faces')
            face_count = cursor.fetchone()[0]
            
            # Count recognitions
            cursor.execute('SELECT COUNT(*) FROM face_recognitions')
            recognition_count = cursor.fetchone()[0]
            
            # Database size
            db_size = os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0
            
            # Face crops size
            crops_size = 0
            if os.path.exists(self.face_crops_dir):
                for root, dirs, files in os.walk(self.face_crops_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        crops_size += os.path.getsize(file_path)
            
            return {
                'face_count': face_count,
                'recognition_count': recognition_count,
                'database_size_bytes': db_size,
                'crops_size_bytes': crops_size,
                'total_size_bytes': db_size + crops_size,
                'database_path': self.db_path,
                'crops_path': self.face_crops_dir
            }
    
    def _calculate_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """Calculate cosine similarity between embeddings"""
        try:
            # Normalize embeddings
            norm1 = np.linalg.norm(embedding1)
            norm2 = np.linalg.norm(embedding2)
            
            if norm1 == 0 or norm2 == 0:
                return 0.0
            
            # Calculate cosine similarity
            similarity = np.dot(embedding1, embedding2) / (norm1 * norm2)
            
            # Convert to 0-1 range
            return (similarity + 1) / 2
            
        except Exception:
            return 0.0


# Factory function
def get_face_memory(db_path: str = None) -> FaceMemory:
    """Factory function to create face memory instance"""
    return FaceMemory(db_path)


if __name__ == "__main__":
    # Test the face memory system
    memory = get_face_memory()
    
    print("🧠 Face Memory System Test")
    print(f"📊 Database: {memory.db_path}")
    
    # Show stats
    stats = memory.get_database_stats()
    print(f"📈 Stats: {stats['face_count']} faces, {stats['recognition_count']} recognitions")
    
    # List faces
    faces = memory.list_faces()
    if faces:
        print(f"\n👥 Known faces:")
        for face in faces:
            print(f"  - {face['label']}: {face['image_count']} images, avg confidence {face['confidence_avg']:.2f}")
    else:
        print("\n👥 No faces in database yet")