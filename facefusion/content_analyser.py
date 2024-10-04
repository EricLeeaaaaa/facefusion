from functools import lru_cache

import cv2
import numpy
from tqdm import tqdm

from facefusion import inference_manager, state_manager, wording
from facefusion.download import conditional_download_hashes, conditional_download_sources
from facefusion.filesystem import resolve_relative_path
from facefusion.thread_helper import conditional_thread_semaphore
from facefusion.typing import Fps, InferencePool, ModelOptions, ModelSet, VisionFrame
from facefusion.vision import count_video_frame_total, detect_video_fps, get_video_frame, read_image

MODEL_SET : ModelSet = {}
PROBABILITY_LIMIT = 0.80
RATE_LIMIT = 10
STREAM_COUNTER = 0

def get_inference_pool() -> InferencePool:
    return {}

def clear_inference_pool() -> None:
    pass

def get_model_options() -> ModelOptions:
    return {}

def pre_check() -> bool:
    return True

def analyse_stream(vision_frame : VisionFrame, video_fps : Fps) -> bool:
    return False

def analyse_frame(vision_frame : VisionFrame) -> bool:
    return False

def forward(vision_frame : VisionFrame) -> float:
    return 0.0

def prepare_frame(vision_frame : VisionFrame) -> VisionFrame:
    return vision_frame

@lru_cache(maxsize = None)
def analyse_image(image_path : str) -> bool:
    return False

@lru_cache(maxsize = None)
def analyse_video(video_path : str, start_frame : int, end_frame : int) -> bool:
    return False
