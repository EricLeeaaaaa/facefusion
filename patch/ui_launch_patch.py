import facefusion.uis.layouts.default as default_layout
import gradio
import facefusion.state_manager as state_manager

def patched_run(ui: gradio.Blocks) -> None:
    ui.launch(
        favicon_path='facefusion.ico',
        inbrowser=state_manager.get_item('open_browser'),
        share=True,
        server_port=8805
    )

# 替换原始的 run 函数
default_layout.run = patched_run

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Patch applied: default_layout updated for Gradio sharing.")