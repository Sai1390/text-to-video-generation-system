from pathlib import Path

import cv2
import torch


# Adapted from: https://github.com/huggingface/diffusers/blob/main/src/diffusers/utils/testing_utils.py
def convert_to_video(video_frames: list, fps: int, filename: str) -> str:
    """Convert from numpy array of frame to webm"""
    Path("./outputs").mkdir(parents=True, exist_ok=True)
    output_video_path = f"./outputs/{filename}.webm"
    fourcc = cv2.VideoWriter_fourcc(*"VP90")
    h, w, c = video_frames[0].shape
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=(w, h))
    for i in range(len(video_frames)):
        img = cv2.cvtColor(video_frames[i], cv2.COLOR_RGB2BGR)
        video_writer.write(img)
    return output_video_path


def get_device() -> str:
    """Get string of torch accelerator"""
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"
