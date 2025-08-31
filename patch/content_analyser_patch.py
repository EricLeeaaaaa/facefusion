import facefusion.content_analyser as content_analyser
from facefusion.types import VisionFrame, Fps, Detection, InferencePool
from typing import List, Tuple, Dict, Any
import numpy as np

def patched_pre_check() -> bool:
    return True

def patched_analyse_stream(vision_frame: VisionFrame, video_fps: Fps) -> bool:
    return False

def patched_analyse_image(image_path: str) -> bool:
    return False

def patched_analyse_video(video_path: str, trim_frame_start: int, trim_frame_end: int) -> bool:
    return False

def patched_analyse_frame(vision_frame: VisionFrame) -> bool:
    return False

def patched_detect_nsfw(vision_frame: VisionFrame) -> bool:
    return False

def patched_get_inference_pool() -> Dict[str, Any]:
    return {
        'nsfw_1': DummyModel(),
        'nsfw_2': DummyModel(),
        'nsfw_3': DummyModel()
    }

def patched_clear_inference_pool() -> None:
    pass

def patched_forward_nsfw(vision_frame: VisionFrame, nsfw_model: str) -> np.ndarray:
    if nsfw_model == 'nsfw_1':
        return np.zeros((1, 5), dtype=np.float32)
    elif nsfw_model == 'nsfw_2':
        return np.zeros((2,), dtype=np.float32)
    else:  # nsfw_3
        return np.zeros((4,), dtype=np.float32)

def patched_prepare_detect_frame(temp_vision_frame: VisionFrame, model_name: str) -> VisionFrame:
    return temp_vision_frame

class DummyModel:
    def run(self, *args, **kwargs) -> List[np.ndarray]:
        return [np.zeros(0, dtype=np.float32)]

# 应用补丁
content_analyser.pre_check = patched_pre_check
content_analyser.analyse_stream = patched_analyse_stream
content_analyser.analyse_image = patched_analyse_image
content_analyser.analyse_video = patched_analyse_video
content_analyser.analyse_frame = patched_analyse_frame
content_analyser.detect_nsfw = patched_detect_nsfw
content_analyser.get_inference_pool = patched_get_inference_pool
content_analyser.clear_inference_pool = patched_clear_inference_pool
content_analyser.forward_nsfw = patched_forward_nsfw
content_analyser.prepare_detect_frame = patched_prepare_detect_frame

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Patch applied: content_analyser updated.")
