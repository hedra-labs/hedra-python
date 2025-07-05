#!/usr/bin/env python3
"""
DeepFace Recognition Module for Hedra CLI
Provides superior face detection, recognition, and analysis using DeepFace library
"""

import os
import numpy as np
from typing import List, Dict, Tuple, Optional, Union
import cv2

# DeepFace imports with graceful fallback
try:
    from deepface import DeepFace
    DEEPFACE_AVAILABLE = True
except ImportError:
    DEEPFACE_AVAILABLE = False


class DeepFaceRecognizer:
    """
    Advanced face recognition using DeepFace library
    Falls back to OpenCV if DeepFace is not available
    """
    
    def __init__(self, detector_backend='retinaface', model_name='Facenet512'):
        """
        Initialize the DeepFace recognizer
        
        Args:
            detector_backend: 'retinaface', 'mtcnn', 'opencv', 'ssd', 'dlib'
            model_name: 'Facenet512', 'VGG-Face', 'ArcFace', 'Dlib'
        """
        self.detector_backend = detector_backend
        self.model_name = model_name
        self.available = DEEPFACE_AVAILABLE
        
        # Fallback to OpenCV if DeepFace not available
        if not self.available:
            self.detector_backend = 'opencv'
            self._init_opencv_fallback()
        
        # Cache for model loading
        self._models_loaded = False
        
    def _init_opencv_fallback(self):
        """Initialize OpenCV fallback for face detection"""
        try:
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
        except Exception as e:
            raise RuntimeError(f"Could not initialize OpenCV fallback: {e}")
    
    def detect_faces(self, img_path: str, confidence_threshold: float = 0.7) -> List[Dict]:
        """
        Detect faces in an image
        
        Args:
            img_path: Path to image file
            confidence_threshold: Minimum confidence for face detection
            
        Returns:
            List of face dictionaries with bbox, confidence, and analysis
        """
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")
        
        if not self.available:
            return self._detect_faces_opencv(img_path)
        
        try:
            # Use DeepFace for detection
            faces = DeepFace.extract_faces(
                img_path=img_path,
                detector_backend=self.detector_backend,
                enforce_detection=False,
                align=True
            )
            
            # Get face regions with DeepFace
            face_objs = DeepFace.analyze(
                img_path=img_path,
                actions=['age', 'gender', 'emotion'],
                detector_backend=self.detector_backend,
                enforce_detection=False,
                silent=True
            )
            
            # Handle both single face and multiple faces
            if not isinstance(face_objs, list):
                face_objs = [face_objs]
            
            detected_faces = []
            
            for i, face_obj in enumerate(face_objs):
                # Extract region coordinates
                region = face_obj.get('region', {})
                x, y, w, h = region.get('x', 0), region.get('y', 0), region.get('w', 0), region.get('h', 0)
                
                # Skip if no valid region
                if w == 0 or h == 0:
                    continue
                
                # Calculate confidence based on detection
                confidence = self._calculate_detection_confidence(face_obj)
                
                if confidence >= confidence_threshold:
                    face_data = {
                        'bbox': (x, y, w, h),
                        'confidence': confidence,
                        'center': (x + w/2, y + h/2),
                        'area': w * h,
                        'analysis': {
                            'age': face_obj.get('age', 0),
                            'gender': face_obj.get('dominant_gender', 'unknown'),
                            'emotion': face_obj.get('dominant_emotion', 'neutral'),
                            'gender_confidence': face_obj.get('gender', {}).get(face_obj.get('dominant_gender', 'Woman'), 0),
                            'emotion_confidence': face_obj.get('emotion', {}).get(face_obj.get('dominant_emotion', 'neutral'), 0)
                        }
                    }
                    detected_faces.append(face_data)
            
            # Sort faces left to right
            detected_faces.sort(key=lambda x: x['center'][0])
            
            return detected_faces
            
        except Exception as e:
            print(f"⚠️  DeepFace detection failed: {e}")
            print("🔄 Falling back to OpenCV detection...")
            return self._detect_faces_opencv(img_path)
    
    def _detect_faces_opencv(self, img_path: str) -> List[Dict]:
        """Fallback OpenCV face detection"""
        img = cv2.imread(img_path)
        if img is None:
            return []
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=6,
            minSize=(40, 40),
            maxSize=(400, 400)
        )
        
        detected_faces = []
        for (x, y, w, h) in faces:
            face_data = {
                'bbox': (x, y, w, h),
                'confidence': 0.8,  # Default confidence for OpenCV
                'center': (x + w/2, y + h/2),
                'area': w * h,
                'analysis': {
                    'age': 0,
                    'gender': 'unknown',
                    'emotion': 'neutral',
                    'gender_confidence': 0,
                    'emotion_confidence': 0
                }
            }
            detected_faces.append(face_data)
        
        # Sort faces left to right
        detected_faces.sort(key=lambda x: x['center'][0])
        
        return detected_faces
    
    def _calculate_detection_confidence(self, face_obj: Dict) -> float:
        """Calculate overall detection confidence from face analysis"""
        # Base confidence from successful detection
        base_confidence = 0.8
        
        # Boost confidence based on analysis quality
        try:
            # Age confidence (younger/older faces are usually clearer)
            age = face_obj.get('age', 25)
            age_factor = 1.0 if 20 <= age <= 60 else 0.9
            
            # Gender confidence
            gender_conf = max(face_obj.get('gender', {}).values()) if face_obj.get('gender') else 0
            gender_factor = min(gender_conf / 100, 1.0)
            
            # Emotion confidence
            emotion_conf = max(face_obj.get('emotion', {}).values()) if face_obj.get('emotion') else 0
            emotion_factor = min(emotion_conf / 100, 1.0)
            
            # Combined confidence
            combined_confidence = base_confidence * age_factor * (0.3 + 0.7 * gender_factor) * (0.3 + 0.7 * emotion_factor)
            
            return min(combined_confidence, 0.99)
            
        except Exception:
            return base_confidence
    
    def create_embedding(self, img_path: str, face_bbox: Tuple[int, int, int, int] = None) -> Optional[np.ndarray]:
        """
        Create face embedding for recognition
        
        Args:
            img_path: Path to image
            face_bbox: Optional bounding box (x, y, w, h) to crop face
            
        Returns:
            Face embedding as numpy array or None if failed
        """
        if not self.available:
            print("⚠️  Face embedding requires DeepFace library")
            return None
        
        try:
            # If bbox provided, crop the face first
            if face_bbox:
                img = cv2.imread(img_path)
                x, y, w, h = face_bbox
                face_img = img[y:y+h, x:x+w]
                
                # Save temporary cropped face
                temp_path = "/tmp/temp_face.jpg"
                cv2.imwrite(temp_path, face_img)
                img_path = temp_path
            
            # Generate embedding
            embedding = DeepFace.represent(
                img_path=img_path,
                model_name=self.model_name,
                detector_backend=self.detector_backend,
                enforce_detection=False
            )
            
            # Handle both single and multiple face results
            if isinstance(embedding, list) and len(embedding) > 0:
                embedding = embedding[0]
            
            if isinstance(embedding, dict) and 'embedding' in embedding:
                return np.array(embedding['embedding'])
            
            return None
            
        except Exception as e:
            print(f"⚠️  Embedding generation failed: {e}")
            return None
    
    def compare_faces(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Compare two face embeddings
        
        Args:
            embedding1: First face embedding
            embedding2: Second face embedding
            
        Returns:
            Similarity score (0.0 to 1.0, higher = more similar)
        """
        if embedding1 is None or embedding2 is None:
            return 0.0
        
        try:
            # Calculate cosine similarity
            dot_product = np.dot(embedding1, embedding2)
            norm1 = np.linalg.norm(embedding1)
            norm2 = np.linalg.norm(embedding2)
            
            if norm1 == 0 or norm2 == 0:
                return 0.0
            
            similarity = dot_product / (norm1 * norm2)
            
            # Convert to 0-1 range (cosine similarity is -1 to 1)
            return (similarity + 1) / 2
            
        except Exception as e:
            print(f"⚠️  Face comparison failed: {e}")
            return 0.0
    
    def analyze_face_quality(self, img_path: str, face_bbox: Tuple[int, int, int, int] = None) -> Dict:
        """
        Analyze face quality for lip-sync suitability
        
        Args:
            img_path: Path to image
            face_bbox: Optional bounding box
            
        Returns:
            Quality analysis dictionary
        """
        try:
            img = cv2.imread(img_path)
            if img is None:
                return {'quality_score': 0.0, 'recommendation': 'Image not found'}
            
            # Crop face if bbox provided
            if face_bbox:
                x, y, w, h = face_bbox
                face_img = img[y:y+h, x:x+w]
            else:
                face_img = img
            
            # Basic quality metrics
            quality_metrics = {
                'size_score': self._calculate_size_score(face_bbox, img.shape[:2]),
                'sharpness_score': self._calculate_sharpness_score(face_img),
                'brightness_score': self._calculate_brightness_score(face_img),
                'position_score': self._calculate_position_score(face_bbox, img.shape[:2]) if face_bbox else 0.8
            }
            
            # Overall quality score
            weights = {'size': 0.3, 'sharpness': 0.3, 'brightness': 0.2, 'position': 0.2}
            quality_score = sum(quality_metrics[k.replace('_score', '') + '_score'] * weights[k.replace('_score', '')] 
                               for k in quality_metrics.keys())
            
            # Recommendation
            if quality_score >= 0.8:
                recommendation = "Excellent for lip-sync"
            elif quality_score >= 0.6:
                recommendation = "Good for lip-sync"
            elif quality_score >= 0.4:
                recommendation = "Moderate quality"
            else:
                recommendation = "Poor quality, consider different image"
            
            return {
                'quality_score': quality_score,
                'recommendation': recommendation,
                'metrics': quality_metrics
            }
            
        except Exception as e:
            return {'quality_score': 0.0, 'recommendation': f'Analysis failed: {e}'}
    
    def _calculate_size_score(self, bbox: Tuple[int, int, int, int], img_shape: Tuple[int, int]) -> float:
        """Calculate face size score (larger faces are better for lip-sync)"""
        if not bbox:
            return 0.5
        
        _, _, w, h = bbox
        img_h, img_w = img_shape
        
        face_area = w * h
        img_area = img_w * img_h
        face_ratio = face_area / img_area
        
        # Optimal face size is 10-40% of image
        if 0.1 <= face_ratio <= 0.4:
            return 1.0
        elif 0.05 <= face_ratio <= 0.6:
            return 0.8
        else:
            return 0.4
    
    def _calculate_sharpness_score(self, face_img: np.ndarray) -> float:
        """Calculate face sharpness using Laplacian variance"""
        try:
            gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
            
            # Normalize to 0-1 range
            return min(laplacian_var / 1000, 1.0)
        except Exception:
            return 0.5
    
    def _calculate_brightness_score(self, face_img: np.ndarray) -> float:
        """Calculate face brightness score"""
        try:
            gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            mean_brightness = np.mean(gray)
            
            # Optimal brightness is 80-180 (out of 255)
            if 80 <= mean_brightness <= 180:
                return 1.0
            elif 60 <= mean_brightness <= 220:
                return 0.7
            else:
                return 0.4
        except Exception:
            return 0.5
    
    def _calculate_position_score(self, bbox: Tuple[int, int, int, int], img_shape: Tuple[int, int]) -> float:
        """Calculate face position score (centered faces are usually better)"""
        if not bbox:
            return 0.5
        
        x, y, w, h = bbox
        img_h, img_w = img_shape
        
        # Face center
        face_center_x = x + w/2
        face_center_y = y + h/2
        
        # Image center
        img_center_x = img_w / 2
        img_center_y = img_h / 2
        
        # Distance from center (normalized)
        distance_x = abs(face_center_x - img_center_x) / img_w
        distance_y = abs(face_center_y - img_center_y) / img_h
        
        # Score based on distance from center
        distance_score = 1.0 - (distance_x + distance_y) / 2
        
        return max(distance_score, 0.0)
    
    def get_available_backends(self) -> List[str]:
        """Get list of available detection backends"""
        if not self.available:
            return ['opencv']
        
        # Test which backends are available
        backends = []
        test_backends = ['retinaface', 'mtcnn', 'opencv', 'ssd', 'dlib']
        
        for backend in test_backends:
            try:
                # Quick test with a dummy call
                DeepFace.extract_faces(
                    img_path="dummy.jpg",
                    detector_backend=backend,
                    enforce_detection=False
                )
                backends.append(backend)
            except Exception:
                continue
        
        return backends if backends else ['opencv']
    
    def get_system_info(self) -> Dict:
        """Get system information for debugging"""
        info = {
            'deepface_available': self.available,
            'detector_backend': self.detector_backend,
            'model_name': self.model_name,
            'opencv_available': hasattr(cv2, 'CascadeClassifier')
        }
        
        if self.available:
            try:
                info['available_backends'] = self.get_available_backends()
            except Exception:
                info['available_backends'] = ['opencv']
        
        return info


def get_recognizer(detector_backend: str = 'retinaface') -> DeepFaceRecognizer:
    """Factory function to create recognizer instance"""
    return DeepFaceRecognizer(detector_backend=detector_backend)


if __name__ == "__main__":
    # Test the recognizer
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python deepface_recognizer.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    recognizer = get_recognizer()
    
    print("🔍 System Info:")
    info = recognizer.get_system_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    print(f"\n🎭 Detecting faces in: {image_path}")
    faces = recognizer.detect_faces(image_path)
    
    print(f"✅ Found {len(faces)} face(s)")
    for i, face in enumerate(faces):
        print(f"\n👤 Face {i+1}:")
        print(f"  📍 Position: {face['bbox']}")
        print(f"  🎯 Confidence: {face['confidence']:.2f}")
        print(f"  📊 Analysis: {face['analysis']}")
        
        # Test quality analysis
        quality = recognizer.analyze_face_quality(image_path, face['bbox'])
        print(f"  ⭐ Quality: {quality['quality_score']:.2f} - {quality['recommendation']}")