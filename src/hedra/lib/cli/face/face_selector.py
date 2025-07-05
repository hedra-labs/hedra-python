#!/usr/bin/env python3
"""
Enhanced Face Selector for Hedra CLI
Provides ASCII art visualization, numbered selection, and deepface recognition
"""

import cv2
import numpy as np
import os
from typing import List, Dict, Optional, Tuple

# Import our new modules
try:
    from .deepface_recognizer import get_recognizer
    from .face_memory import get_face_memory
    ENHANCED_RECOGNITION = True
except ImportError:
    ENHANCED_RECOGNITION = False

class EnhancedFaceSelector:
    """Enhanced face selector with deepface recognition and memory"""
    
    def __init__(self, image_path: str, use_deepface: bool = True):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        if self.img is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        self.original_img = self.img.copy()
        self.faces = []
        self.recognized_faces = []
        
        # Initialize recognition system
        self.use_deepface = use_deepface and ENHANCED_RECOGNITION
        
        if self.use_deepface:
            try:
                self.recognizer = get_recognizer()
                self.face_memory = get_face_memory()
                print("🧠 Enhanced face recognition enabled")
            except Exception as e:
                print(f"⚠️  DeepFace initialization failed: {e}")
                self.use_deepface = False
        
        # Fallback to OpenCV
        if not self.use_deepface:
            self._init_opencv_fallback()
    
    def _init_opencv_fallback(self):
        """Initialize OpenCV fallback"""
        try:
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
            print("📹 Using OpenCV face detection")
        except Exception as e:
            raise RuntimeError(f"Could not load face detection model: {e}")
    
    def detect_and_recognize_faces(self) -> List[Dict]:
        """Detect faces and attempt recognition"""
        if self.use_deepface:
            return self._detect_with_deepface()
        else:
            return self._detect_with_opencv()
    
    def _detect_with_deepface(self) -> List[Dict]:
        """Use DeepFace for detection and recognition"""
        try:
            # Detect faces
            detected_faces = self.recognizer.detect_faces(self.image_path)
            
            enhanced_faces = []
            for i, face in enumerate(detected_faces):
                # Create embedding for recognition
                embedding = self.recognizer.create_embedding(self.image_path, face['bbox'])
                
                # Try to recognize face
                recognition_result = None
                if embedding is not None:
                    matches = self.face_memory.find_similar_faces(embedding, threshold=0.8)
                    if matches:
                        recognition_result = matches[0]  # Best match
                
                # Enhanced face data
                enhanced_face = {
                    'index': i,
                    'bbox': face['bbox'],
                    'confidence': face['confidence'],
                    'center': face['center'],
                    'area': face['area'],
                    'analysis': face['analysis'],
                    'embedding': embedding,
                    'recognition': recognition_result,
                    'is_known': recognition_result is not None,
                    'label': recognition_result['label'] if recognition_result else None,
                    'name': recognition_result['name'] if recognition_result else None
                }
                
                enhanced_faces.append(enhanced_face)
            
            self.faces = enhanced_faces
            return enhanced_faces
            
        except Exception as e:
            print(f"⚠️  DeepFace detection failed: {e}")
            print("🔄 Falling back to OpenCV...")
            return self._detect_with_opencv()
    
    def _detect_with_opencv(self) -> List[Dict]:
        """Fallback OpenCV detection"""
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=6,
            minSize=(40, 40),
            maxSize=(400, 400)
        )
        
        enhanced_faces = []
        for i, (x, y, w, h) in enumerate(faces):
            enhanced_face = {
                'index': i,
                'bbox': (x, y, w, h),
                'confidence': 0.8,
                'center': (x + w/2, y + h/2),
                'area': w * h,
                'analysis': {'age': 0, 'gender': 'unknown', 'emotion': 'neutral'},
                'embedding': None,
                'recognition': None,
                'is_known': False,
                'label': None,
                'name': None
            }
            enhanced_faces.append(enhanced_face)
        
        # Sort left to right
        enhanced_faces.sort(key=lambda x: x['center'][0])
        
        self.faces = enhanced_faces
        return enhanced_faces
    
    def create_enhanced_ascii_layout(self) -> str:
        """Create enhanced ASCII layout with recognition info"""
        if not self.faces:
            return "❌ No faces detected"
        
        # Create grid
        grid_w, grid_h = 26, 8
        grid = [[' ' for _ in range(grid_w)] for _ in range(grid_h)]
        
        img_h, img_w = self.img.shape[:2]
        
        # Map faces to grid
        for i, face in enumerate(self.faces):
            x, y, w, h = face['bbox']
            center_x, center_y = face['center']
            
            # Grid position
            grid_x = int((center_x / img_w) * (grid_w - 6))
            grid_y = int((center_y / img_h) * (grid_h - 2))
            
            # Face box size
            face_grid_w = max(3, int((w / img_w) * grid_w * 0.3))
            face_grid_h = max(2, int((h / img_h) * grid_h * 0.4))
            
            # Draw face
            face_char = face['label'][:4].upper() if face['is_known'] else str(i + 1)
            
            for dy in range(face_grid_h + 1):
                for dx in range(face_grid_w + 1):
                    y_pos, x_pos = grid_y + dy, grid_x + dx
                    if 0 <= y_pos < grid_h and 0 <= x_pos < grid_w:
                        if dy == 0 or dy == face_grid_h or dx == 0 or dx == face_grid_w:
                            grid[y_pos][x_pos] = '█'
                        elif dy == face_grid_h//2 and dx == face_grid_w//2:
                            grid[y_pos][x_pos] = face_char[0] if face_char else str(i + 1)
                        elif grid[y_pos][x_pos] == ' ':
                            grid[y_pos][x_pos] = '░'
        
        # Build output
        lines = []
        known_count = sum(1 for f in self.faces if f['is_known'])
        unknown_count = len(self.faces) - known_count
        
        lines.append(f"🧠 Analyzing faces with AI...")
        lines.append(f"🎭 {len(self.faces)} faces detected ({known_count} known, {unknown_count} unknown)")
        lines.append("")
        lines.append("┌" + "─" * grid_w + "┐")
        
        for row in grid:
            lines.append("│" + "".join(row) + "│")
        
        lines.append("└" + "─" * grid_w + "┘")
        
        return "\n".join(lines)
    
    def get_enhanced_face_descriptions(self) -> List[Dict]:
        """Get enhanced face descriptions with recognition info"""
        descriptions = []
        img_h, img_w = self.img.shape[:2]
        
        for i, face in enumerate(self.faces):
            x, y, w, h = face['bbox']
            center_x, center_y = face['center']
            
            # Normalized coordinates
            norm_x = center_x / img_w
            norm_y = center_y / img_h
            
            # Description based on recognition
            if face['is_known']:
                if face['name']:
                    description = f"{face['label']} ({face['name']})"
                else:
                    description = face['label'].title()
                status = f"✅ {face['recognition']['similarity']:.0%} confidence"
            else:
                # Position description for unknown faces
                if len(self.faces) == 1:
                    description = "Unknown person"
                elif len(self.faces) == 2:
                    description = "Unknown person (left)" if i == 0 else "Unknown person (right)"
                else:
                    description = f"Unknown person #{i+1}"
                status = "❓ New face"
            
            # Analysis info
            analysis = face['analysis']
            demographics = ""
            if analysis['age'] > 0:
                demographics = f"📊 {analysis['gender']}, ~{analysis['age']}, {analysis['emotion']}"
            
            descriptions.append({
                'index': i,
                'number': i + 1,
                'description': description,
                'status': status,
                'demographics': demographics,
                'coordinates': (norm_x, norm_y),
                'coord_string': f"({norm_x:.3f}, {norm_y:.3f})",
                'is_known': face['is_known'],
                'label': face['label'],
                'confidence': face['confidence'],
                'face_data': face
            })
        
        return descriptions
    
    def interactive_selection_with_recognition(self) -> Optional[Tuple[float, float]]:
        """Enhanced interactive selection with recognition"""
        faces = self.detect_and_recognize_faces()
        
        if not faces:
            print("❌ No faces detected")
            print("💡 Try: Better lighting, face closer to camera, frontal angle")
            print("🔧 Fallback: Use manual --bounding-box x,y coordinates")
            return None
        
        if len(faces) == 1:
            # Single face auto-selection
            face = faces[0]
            desc = self.get_enhanced_face_descriptions()[0]
            
            if face['is_known']:
                print(f"✅ Recognized {desc['description']}")
            else:
                print("✅ One face detected - using automatically")
            
            print(f"📍 Coordinates: {desc['coord_string']}")
            return desc['coordinates']
        
        # Multiple faces - show enhanced selection
        print(self.create_enhanced_ascii_layout())
        print()
        
        descriptions = self.get_enhanced_face_descriptions()
        for desc in descriptions:
            print(f"[{desc['number']}] {desc['description']:<20} {desc['status']}")
            if desc['demographics']:
                print(f"    {desc['demographics']}")
            print(f"    📍 {desc['coord_string']}")
        
        print("\n[label] Label unknown faces for future use")
        print("[i] Visual selection mode")
        print("[q] Cancel")
        print()
        
        # Get user choice
        while True:
            try:
                choice = input("Choose face or action: ").strip().lower()
                
                if choice == 'q' or choice == 'quit':
                    print("Selection cancelled")
                    return None
                
                elif choice == 'i' or choice == 'interactive':
                    return self.visual_selection()
                
                elif choice == 'label':
                    self._label_unknown_faces()
                    continue
                
                elif choice.isdigit():
                    face_num = int(choice)
                    if 1 <= face_num <= len(faces):
                        selected = descriptions[face_num - 1]
                        print(f"✅ Selected {selected['description']}")
                        print(f"📍 Coordinates: {selected['coord_string']}")
                        return selected['coordinates']
                    else:
                        print(f"❌ Please choose 1-{len(faces)}")
                
                else:
                    print("❌ Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\nSelection cancelled")
                return None
            except EOFError:
                print("\nSelection cancelled")
                return None
    
    def _label_unknown_faces(self):
        """Interactive face labeling workflow"""
        if not self.use_deepface:
            print("⚠️  Face labeling requires DeepFace library")
            return
        
        unknown_faces = [f for f in self.faces if not f['is_known']]
        
        if not unknown_faces:
            print("✅ All faces are already labeled")
            return
        
        print(f"\n🏷️  Found {len(unknown_faces)} unknown face(s) to label")
        
        for face in unknown_faces:
            face_num = face['index'] + 1
            print(f"\n👤 Face {face_num}:")
            
            # Show demographics if available
            analysis = face['analysis']
            if analysis['age'] > 0:
                print(f"   📊 {analysis['gender']}, ~{analysis['age']}, {analysis['emotion']}")
            
            # Get label from user
            while True:
                label = input(f"   Enter label for Face {face_num} (or 'skip'): ").strip()
                
                if label.lower() == 'skip':
                    print("   ⏭️  Skipped")
                    break
                
                if not label:
                    print("   ❌ Label cannot be empty")
                    continue
                
                if label.lower() in ['q', 'quit', 'exit']:
                    return
                
                # Check if label already exists
                existing_face = self.face_memory.find_face_by_label(label)
                if existing_face:
                    print(f"   ⚠️  Label '{label}' already exists")
                    continue
                
                # Save face to memory
                if face['embedding'] is not None:
                    confidence = face['confidence']
                    metadata = {
                        'demographics': analysis,
                        'quality': self.recognizer.analyze_face_quality(self.image_path, face['bbox'])
                    }
                    
                    face_id = self.face_memory.save_face(
                        label=label,
                        embedding=face['embedding'],
                        image_path=self.image_path,
                        bbox=face['bbox'],
                        confidence=confidence,
                        metadata=metadata
                    )
                    
                    print(f"   ✅ Saved '{label}' - will recognize in future sessions")
                    
                    # Update face info
                    face['label'] = label
                    face['is_known'] = True
                    face['recognition'] = {
                        'label': label,
                        'name': None,
                        'similarity': 1.0,
                        'face_id': face_id
                    }
                    
                else:
                    print("   ❌ Could not create face embedding")
                
                break
        
        print("\n🎉 Face labeling complete!")
    
    def find_face_by_label(self, label: str) -> Optional[Tuple[float, float]]:
        """Find face by label in current image"""
        if not self.use_deepface:
            print("⚠️  Face recognition requires DeepFace library")
            return None
        
        # Get face from memory
        stored_face = self.face_memory.find_face_by_label(label)
        if not stored_face:
            print(f"❌ Face '{label}' not found in memory")
            return None
        
        # Detect faces in current image
        faces = self.detect_and_recognize_faces()
        
        # Find matching face
        for face in faces:
            if face['is_known'] and face['label'] == label:
                center_x, center_y = face['center']
                img_h, img_w = self.img.shape[:2]
                norm_coords = (center_x / img_w, center_y / img_h)
                
                print(f"✅ Found {label} - confidence {face['recognition']['similarity']:.0%}")
                print(f"📍 Coordinates: ({norm_coords[0]:.3f}, {norm_coords[1]:.3f})")
                return norm_coords
        
        print(f"❌ Face '{label}' not found in current image")
        return None
    
    def visual_selection(self):
        """Enhanced visual selection with recognition info"""
        print("🖼️  Opening visual selection...")
        print("   Click on any face to select it")
        print("   Press ENTER to confirm, ESC to cancel")
        
        if not hasattr(cv2, 'namedWindow'):
            print("❌ Visual mode not available (no display)")
            return None
        
        window_name = "Enhanced Face Selection - Click to Select"
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self._mouse_callback)
        
        self.selected_face_idx = None
        
        while True:
            display_img = self._draw_enhanced_faces()
            cv2.imshow(window_name, display_img)
            
            key = cv2.waitKey(30) & 0xFF
            
            if key == ord('\r') or key == ord('\n'):  # Enter
                break
            elif key == 27:  # ESC
                self.selected_face_idx = None
                break
        
        cv2.destroyAllWindows()
        
        if self.selected_face_idx is not None:
            face = self.faces[self.selected_face_idx]
            center_x, center_y = face['center']
            img_h, img_w = self.img.shape[:2]
            norm_coords = (center_x / img_w, center_y / img_h)
            
            if face['is_known']:
                print(f"✅ Selected {face['label']}")
            else:
                print(f"✅ Selected Face {self.selected_face_idx + 1}")
            
            print(f"📍 Coordinates: ({norm_coords[0]:.3f}, {norm_coords[1]:.3f})")
            return norm_coords
        
        print("No face selected")
        return None
    
    def _mouse_callback(self, event, x, y, flags, param):
        """Handle mouse clicks in enhanced visual selection"""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Check which face was clicked
            for i, face in enumerate(self.faces):
                fx, fy, fw, fh = face['bbox']
                if fx <= x <= fx + fw and fy <= y <= fy + fh:
                    self.selected_face_idx = i
                    if face['is_known']:
                        print(f"Selected {face['label']}")
                    else:
                        print(f"Selected Face {i + 1}")
                    return
    
    def _draw_enhanced_faces(self):
        """Draw faces with enhanced recognition info"""
        img = self.original_img.copy()
        
        for i, face in enumerate(self.faces):
            x, y, w, h = face['bbox']
            
            # Color coding
            if face['is_known']:
                color = (0, 255, 0)  # Green for known faces
                label = face['label']
            else:
                color = (0, 255, 255)  # Yellow for unknown faces
                label = f"Face {i + 1}"
            
            # Highlight selected face
            if self.selected_face_idx == i:
                color = (255, 0, 0)  # Blue for selected
                thickness = 4
            else:
                thickness = 2
            
            # Draw face rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
            
            # Label background
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
            cv2.rectangle(img, (x, y - 35), (x + label_size[0] + 10, y), color, -1)
            
            # Label text
            cv2.putText(img, label, (x + 5, y - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
            
            # Recognition status
            if face['is_known']:
                confidence_text = f"{face['recognition']['similarity']:.0%}"
                cv2.putText(img, confidence_text, (x, y + h + 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            
            # Coordinates
            center_x, center_y = face['center']
            coord_text = f"({center_x/img.shape[1]:.3f}, {center_y/img.shape[0]:.3f})"
            cv2.putText(img, coord_text, (x, y + h + 40), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        
        # Instructions
        instructions = "Click face to select | ENTER confirm | ESC cancel"
        cv2.putText(img, instructions, (10, img.shape[0] - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return img
    
    def auto_select_best(self):
        """Auto-select best face with enhanced logic"""
        faces = self.detect_and_recognize_faces()
        
        if not faces:
            return None
        
        if len(faces) == 1:
            face = faces[0]
            center_x, center_y = face['center']
            img_h, img_w = self.img.shape[:2]
            return (center_x / img_w, center_y / img_h)
        
        # Enhanced selection logic
        best_face = None
        best_score = -1
        
        for face in faces:
            score = 0
            
            # Prefer known faces
            if face['is_known']:
                score += 0.3
            
            # Face size score (normalized)
            area_ratio = face['area'] / (self.img.shape[0] * self.img.shape[1])
            size_score = min(area_ratio * 10, 1.0)  # Prefer larger faces
            score += size_score * 0.4
            
            # Detection confidence
            score += face['confidence'] * 0.3
            
            if score > best_score:
                best_score = score
                best_face = face
        
        if best_face:
            center_x, center_y = best_face['center']
            img_h, img_w = self.img.shape[:2]
            
            if best_face['is_known']:
                print(f"🤖 Auto-selected {best_face['label']} (known face)")
            else:
                print(f"🤖 Auto-selected best face (Face {best_face['index'] + 1})")
            
            coords = (center_x / img_w, center_y / img_h)
            print(f"📍 Coordinates: ({coords[0]:.3f}, {coords[1]:.3f})")
            return coords
        
        return None


class SimpleFaceSelector:
    """Backwards compatibility wrapper"""
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        if self.img is None:
            raise ValueError(f"Could not load image: {image_path}")
        
        self.original_img = self.img.copy()
        self.faces = []
        
        # Load face detection
        try:
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        except Exception as e:
            raise RuntimeError(f"Could not load face detection model: {e}")
    
    def detect_faces(self):
        """Detect faces in the image"""
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces with balanced parameters for accuracy
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.15,     # Balanced scale factor
            minNeighbors=6,       # Moderate confidence requirement
            minSize=(40, 40),     # Allow smaller faces but not tiny ones
            maxSize=(400, 400),   # Reasonable maximum size
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Filter out overlapping detections (non-maximum suppression)
        if len(faces) > 1:
            faces = self._remove_overlapping_faces(faces)
        
        # Sort faces left to right for consistent numbering
        if len(faces) > 1:
            faces = sorted(faces, key=lambda face: face[0])  # Sort by x coordinate
        
        self.faces = faces
        return len(faces)
    
    def _remove_overlapping_faces(self, faces):
        """Remove overlapping face detections using simple non-maximum suppression"""
        if len(faces) <= 1:
            return faces
        
        # Convert to list of [x, y, x2, y2, area] for easier processing
        boxes = []
        for (x, y, w, h) in faces:
            boxes.append([x, y, x + w, y + h, w * h])
        
        # Sort by area (largest first)
        boxes = sorted(boxes, key=lambda x: x[4], reverse=True)
        
        # Keep track of which boxes to keep
        keep = []
        
        for i, box in enumerate(boxes):
            should_keep = True
            
            for kept_box in keep:
                # Calculate intersection over union (IoU)
                x1 = max(box[0], kept_box[0])
                y1 = max(box[1], kept_box[1])
                x2 = min(box[2], kept_box[2])
                y2 = min(box[3], kept_box[3])
                
                if x1 < x2 and y1 < y2:
                    intersection = (x2 - x1) * (y2 - y1)
                    union = box[4] + kept_box[4] - intersection
                    iou = intersection / union if union > 0 else 0
                    
                    # If overlap is too high, don't keep this box
                    if iou > 0.3:  # 30% overlap threshold
                        should_keep = False
                        break
            
            if should_keep:
                keep.append(box)
        
        # Convert back to (x, y, w, h) format
        filtered_faces = []
        for box in keep:
            filtered_faces.append((box[0], box[1], box[2] - box[0], box[3] - box[1]))
        
        return filtered_faces
    
    def create_ascii_layout(self):
        """Create ASCII art representation of face positions"""
        if not len(self.faces):
            return "❌ No faces detected"
        
        # Create a grid representation
        grid_w, grid_h = 24, 8
        grid = [[' ' for _ in range(grid_w)] for _ in range(grid_h)]
        
        img_h, img_w = self.img.shape[:2]
        
        # Map faces to grid positions
        for i, (x, y, w, h) in enumerate(self.faces):
            # Calculate center position
            center_x = x + w/2
            center_y = y + h/2
            
            # Map to grid coordinates
            grid_x = int((center_x / img_w) * (grid_w - 4))  # Leave space for face box
            grid_y = int((center_y / img_h) * (grid_h - 2))
            
            # Calculate face box size on grid
            face_grid_w = max(2, int((w / img_w) * grid_w * 0.3))
            face_grid_h = max(1, int((h / img_h) * grid_h * 0.4))
            
            # Draw face box
            face_num = str(i + 1)
            
            # Draw the face representation
            for dy in range(face_grid_h + 1):
                for dx in range(face_grid_w + 1):
                    y_pos, x_pos = grid_y + dy, grid_x + dx
                    if 0 <= y_pos < grid_h and 0 <= x_pos < grid_w:
                        if dy == 0 or dy == face_grid_h or dx == 0 or dx == face_grid_w:
                            # Border
                            grid[y_pos][x_pos] = '█'
                        elif dy == face_grid_h//2 and dx == face_grid_w//2:
                            # Face number in center
                            grid[y_pos][x_pos] = face_num
                        elif grid[y_pos][x_pos] == ' ':
                            # Fill
                            grid[y_pos][x_pos] = '░'
        
        # Convert grid to string
        ascii_lines = []
        ascii_lines.append("🎭 DETECTED FACES")
        ascii_lines.append("┌" + "─" * grid_w + "┐")
        
        for row in grid:
            ascii_lines.append("│" + "".join(row) + "│")
        
        ascii_lines.append("└" + "─" * grid_w + "┘")
        
        return "\n".join(ascii_lines)
    
    def get_face_descriptions(self):
        """Get simple descriptions and coordinates for each face"""
        descriptions = []
        img_h, img_w = self.img.shape[:2]
        
        for i, (x, y, w, h) in enumerate(self.faces):
            # Calculate normalized center coordinates
            center_x = (x + w/2) / img_w
            center_y = (y + h/2) / img_h
            
            # Simple position description
            if len(self.faces) == 1:
                position = "Center person"
            elif len(self.faces) == 2:
                position = "Left person" if i == 0 else "Right person"
            else:
                # For 3+ people, use left/center/right or numbered
                if i == 0:
                    position = "Leftmost person"
                elif i == len(self.faces) - 1:
                    position = "Rightmost person"
                else:
                    position = f"Person #{i+1}"
            
            descriptions.append({
                'number': i + 1,
                'position': position,
                'coordinates': (center_x, center_y),
                'coord_string': f"({center_x:.3f}, {center_y:.3f})"
            })
        
        return descriptions
    
    def interactive_selection(self):
        """Simple interactive selection interface"""
        num_faces = self.detect_faces()
        
        if num_faces == 0:
            print("❌ No faces detected")
            print("💡 Try: Better lighting, face closer to camera, frontal angle")
            print("🔧 Fallback: Use manual --bounding-box x,y coordinates")
            return None
        
        if num_faces == 1:
            # Auto-select single face
            desc = self.get_face_descriptions()[0]
            print("✅ One face detected - using automatically")
            print(f"📍 Coordinates: {desc['coord_string']}")
            return desc['coordinates']
        
        # Multiple faces - show selection interface
        print(f"🔍 Analyzing faces...")
        print(f"🎭 {num_faces} faces detected\n")
        
        # Show ASCII layout
        print(self.create_ascii_layout())
        print()
        
        # Show numbered options
        descriptions = self.get_face_descriptions()
        for desc in descriptions:
            print(f"[{desc['number']}] {desc['position']:<15} {desc['coord_string']}")
        
        print("[i] Visual selection mode")
        print("[q] Cancel")
        print()
        
        # Get user choice
        while True:
            try:
                choice = input("Choose face (1-{}): ".format(num_faces)).strip().lower()
                
                if choice == 'q' or choice == 'quit':
                    print("Selection cancelled")
                    return None
                
                elif choice == 'i' or choice == 'interactive':
                    return self.visual_selection()
                
                elif choice.isdigit():
                    face_num = int(choice)
                    if 1 <= face_num <= num_faces:
                        selected = descriptions[face_num - 1]
                        print(f"✅ Selected Face {face_num}")
                        print(f"📍 Coordinates: {selected['coord_string']}")
                        return selected['coordinates']
                    else:
                        print(f"❌ Please choose 1-{num_faces}")
                
                else:
                    print("❌ Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\nSelection cancelled")
                return None
            except EOFError:
                print("\nSelection cancelled")
                return None
    
    def visual_selection(self):
        """OpenCV visual selection interface"""
        print("🖼️  Opening visual selection...")
        print("   Click on any face to select it")
        print("   Press ENTER to confirm, ESC to cancel")
        
        if not hasattr(cv2, 'namedWindow'):
            print("❌ Visual mode not available (no display)")
            return None
        
        window_name = "Face Selection - Click to Select"
        cv2.namedWindow(window_name)
        cv2.setMouseCallback(window_name, self._mouse_callback)
        
        self.selected_face_idx = None
        
        while True:
            display_img = self._draw_faces()
            cv2.imshow(window_name, display_img)
            
            key = cv2.waitKey(30) & 0xFF
            
            if key == ord('\r') or key == ord('\n'):  # Enter
                break
            elif key == 27:  # ESC
                self.selected_face_idx = None
                break
        
        cv2.destroyAllWindows()
        
        if self.selected_face_idx is not None:
            descriptions = self.get_face_descriptions()
            selected = descriptions[self.selected_face_idx]
            print(f"✅ Selected Face {selected['number']}")
            print(f"📍 Coordinates: {selected['coord_string']}")
            return selected['coordinates']
        
        print("No face selected")
        return None
    
    def _mouse_callback(self, event, x, y, flags, param):
        """Handle mouse clicks in visual selection"""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Check which face was clicked
            for i, (fx, fy, fw, fh) in enumerate(self.faces):
                if fx <= x <= fx + fw and fy <= y <= fy + fh:
                    self.selected_face_idx = i
                    print(f"Selected Face {i + 1}")
                    return
    
    def _draw_faces(self):
        """Draw face rectangles with numbers for visual selection"""
        img = self.original_img.copy()
        
        for i, (x, y, w, h) in enumerate(self.faces):
            # Color - yellow for normal, green for selected
            color = (0, 255, 0) if self.selected_face_idx == i else (0, 255, 255)
            thickness = 3 if self.selected_face_idx == i else 2
            
            # Draw face rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
            
            # Face number
            label = f"Face {i + 1}"
            
            # Label background
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
            cv2.rectangle(img, (x, y - 35), (x + label_size[0] + 10, y), color, -1)
            
            # Label text
            cv2.putText(img, label, (x + 5, y - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
            
            # Coordinates
            center_x = (x + w/2) / img.shape[1]
            center_y = (y + h/2) / img.shape[0]
            coord_text = f"({center_x:.3f}, {center_y:.3f})"
            cv2.putText(img, coord_text, (x, y + h + 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        # Instructions
        instructions = "Click face to select | ENTER confirm | ESC cancel"
        cv2.putText(img, instructions, (10, img.shape[0] - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return img
    
    def auto_select_best(self):
        """Auto-select the best face (largest, most centered)"""
        num_faces = self.detect_faces()
        
        if num_faces == 0:
            return None
        
        if num_faces == 1:
            desc = self.get_face_descriptions()[0]
            return desc['coordinates']
        
        # For multiple faces, select the largest one
        largest_idx = 0
        largest_area = 0
        
        for i, (x, y, w, h) in enumerate(self.faces):
            area = w * h
            if area > largest_area:
                largest_area = area
                largest_idx = i
        
        descriptions = self.get_face_descriptions()
        selected = descriptions[largest_idx]
        print(f"🤖 Auto-selected largest face (Face {selected['number']})")
        print(f"📍 Coordinates: {selected['coord_string']}")
        return selected['coordinates']

def select_face(image_path, mode='interactive', use_enhanced=True):
    """
    Main face selection function with enhanced recognition
    
    Args:
        image_path: Path to image file
        mode: 'interactive' or 'auto'
        use_enhanced: Use enhanced deepface recognition if available
    
    Returns:
        Tuple of (x, y) coordinates or None if cancelled
    """
    try:
        if use_enhanced and ENHANCED_RECOGNITION:
            selector = EnhancedFaceSelector(image_path)
            
            if mode == 'auto':
                return selector.auto_select_best()
            else:
                return selector.interactive_selection_with_recognition()
        else:
            # Fallback to simple selector
            selector = SimpleFaceSelector(image_path)
            
            if mode == 'auto':
                return selector.auto_select_best()
            else:
                return selector.interactive_selection()
            
    except ImportError:
        print("❌ OpenCV not available. Install with: pip install opencv-python")
        return None
    except Exception as e:
        print(f"❌ Error in face selection: {e}")
        return None


def find_face_by_label(image_path, label):
    """
    Find face by label using recognition
    
    Args:
        image_path: Path to image file
        label: Face label to find
    
    Returns:
        Tuple of (x, y) coordinates or None if not found
    """
    try:
        if not ENHANCED_RECOGNITION:
            print("❌ Face recognition requires DeepFace library")
            return None
        
        selector = EnhancedFaceSelector(image_path)
        return selector.find_face_by_label(label)
        
    except Exception as e:
        print(f"❌ Error in face recognition: {e}")
        return None


def label_faces_interactive(image_path):
    """
    Interactive face labeling for building recognition database
    
    Args:
        image_path: Path to image file
        
    Returns:
        Number of faces labeled
    """
    try:
        if not ENHANCED_RECOGNITION:
            print("❌ Face labeling requires DeepFace library")
            return 0
        
        selector = EnhancedFaceSelector(image_path)
        faces = selector.detect_and_recognize_faces()
        
        if not faces:
            print("❌ No faces detected for labeling")
            return 0
        
        unknown_faces = [f for f in faces if not f['is_known']]
        
        if not unknown_faces:
            print("✅ All faces already labeled")
            return 0
        
        print(f"🏷️  Found {len(unknown_faces)} unknown face(s)")
        print("🧠 Enhanced face recognition enabled")
        print(selector.create_enhanced_ascii_layout())
        print()
        
        descriptions = selector.get_enhanced_face_descriptions()
        for desc in descriptions:
            if not desc['is_known']:
                print(f"[{desc['number']}] {desc['description']:<20} {desc['status']}")
                if desc['demographics']:
                    print(f"    {desc['demographics']}")
        
        print("\nReady to label faces...")
        selector._label_unknown_faces()
        
        return len(unknown_faces)
        
    except Exception as e:
        print(f"❌ Error in face labeling: {e}")
        return 0

def preview_faces(image_path):
    """Preview faces without selection"""
    try:
        selector = SimpleFaceSelector(image_path)
        num_faces = selector.detect_faces()
        
        if num_faces == 0:
            print("❌ No faces detected")
            return
        
        print(f"🔍 Detected {num_faces} face(s)")
        print(selector.create_ascii_layout())
        print()
        
        descriptions = selector.get_face_descriptions()
        for desc in descriptions:
            print(f"[{desc['number']}] {desc['position']:<15} {desc['coord_string']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python face_selector.py <image_path> [mode]")
        print("Modes: interactive (default), auto, preview")
        sys.exit(1)
    
    image_path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'interactive'
    
    if mode == 'preview':
        preview_faces(image_path)
    else:
        result = select_face(image_path, mode)
        if result:
            print(f"\n🎯 Use: --bounding-box {result[0]:.3f},{result[1]:.3f}")