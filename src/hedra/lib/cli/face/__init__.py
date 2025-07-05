"""
Face detection and selection utilities for Hedra CLI.
"""

"""
Face detection and selection utilities for Hedra CLI.
"""

# Face detection is optional - import only when needed
__all__ = []

def lazy_import_face_detection():
    """Lazy import face detection modules to avoid TensorFlow overhead."""
    global DeepFaceRecognizer, FaceSelector, EnhancedFaceSelector, SimpleFaceSelector, FaceMemory
    
    try:
        from .deepface_recognizer import DeepFaceRecognizer
        from .face_selector import EnhancedFaceSelector, SimpleFaceSelector
        from .face_memory import FaceMemory
        
        # Alias for backwards compatibility
        FaceSelector = EnhancedFaceSelector
        
        return True
    except ImportError as e:
        import warnings
        warnings.warn(f"Face detection dependencies not available: {e}")
        return False

# Only attempt import if explicitly requested
FACE_DETECTION_AVAILABLE = False

def get_face_detector():
    """Get face detector with lazy loading."""
    global FACE_DETECTION_AVAILABLE
    if not FACE_DETECTION_AVAILABLE:
        FACE_DETECTION_AVAILABLE = lazy_import_face_detection()
    
    if FACE_DETECTION_AVAILABLE:
        return DeepFaceRecognizer()
    return None

def get_face_selector():
    """Get face selector with lazy loading."""
    global FACE_DETECTION_AVAILABLE
    if not FACE_DETECTION_AVAILABLE:
        FACE_DETECTION_AVAILABLE = lazy_import_face_detection()
    
    if FACE_DETECTION_AVAILABLE:
        return FaceSelector()
    return None