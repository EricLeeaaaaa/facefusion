import facefusion.processors.choices as choices
from facefusion.processors.types import FaceSwapperSet, FaceSwapperModel
from typing import List

# 保留原始的 face_swapper_set 以便参考或恢复（如果需要）
# original_face_swapper_set = choices.face_swapper_set.copy()

# 创建新字典
patched_face_swapper_set: FaceSwapperSet = {
	'hyperswap_1a_256': [ '256x256', '512x512', '768x768', '1024x1024' ],
	'hyperswap_1b_256': [ '256x256', '512x512', '768x768', '1024x1024' ],
	'hyperswap_1c_256': [ '256x256', '512x512', '768x768', '1024x1024' ],
    'inswapper_128': ['128x128', '256x256', '384x384', '512x512', '768x768', '1024x1024'],
    'inswapper_128_fp16': ['128x128', '256x256', '384x384', '512x512', '768x768', '1024x1024']
}

# 创建只包含所需模型键的新列表
patched_face_swapper_models: List[FaceSwapperModel] = list(patched_face_swapper_set.keys())

# 应用 patch
choices.face_swapper_set = patched_face_swapper_set
choices.face_swapper_models = patched_face_swapper_models

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Patch applied: face_swapper_set and face_swapper_models updated.")
