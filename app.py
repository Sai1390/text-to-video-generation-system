
import argparse

import streamlit as st

from lib.generate import generate
from lib.util import convert_to_video, get_device


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--device",
        choices=["cuda", "mps", "cpu"],
        help="Override device",
    )
    args = parser.parse_args()
    device = args.device if args.device is not None else get_device()

    st.set_page_config(
        page_title="    ",
        page_icon="🎥",
        layout="wide",
        menu_items={
            
            "About": "# Text TO Video 🎥 \n A user-friendly Streamlit app for running a text-to-video diffusion model. It enables users to input text prompts, customize key visual parameters, and generate high-quality, coherent video outputs based on the input text.",
        },
    )
    st.write("# Text TO Video 🎥")
    col_left, col_right = st.columns(2)

    with col_left:
        st.info(
            "Customize your video settings below, then click 'Generate' to create a unique video clip based on your input text.",
            icon="ℹ️",
        )
        prompt = st.text_area("Prompt")

        # Number inputs
        num_sub_col_1, num_sub_col_2, num_sub_col_3, num_sub_col_4 = st.columns(4)
        frames = num_sub_col_1.number_input(
            label="Number of total frames", min_value=1, max_value=999999, value=16
        )
        n_fps = num_sub_col_2.number_input(
            label="Frames per second (fps)", min_value=1, max_value=999999, value=8
        )
        steps = num_sub_col_3.number_input(
            label="Number of inference steps", min_value=1, max_value=999999, value=50
        )
        seed = num_sub_col_4.number_input(
            label="Seed", min_value=1, max_value=999999, value=42
        )

        # Dim inputs
        dim_sub_col_1, dim_sub_col_2 = st.columns(2)
        height = dim_sub_col_1.slider(
            label="Height", min_value=16, max_value=1024, value=256, step=8
        )
        width = dim_sub_col_2.slider(
            label="Width", min_value=16, max_value=1024, value=256, step=8
        )

        with st.expander("Optimizations", expanded=True):
            st.markdown(f"**Device:** `{device}`")
            cpu_offload = st.checkbox(
                "Enable CPU offloading",
                value=True if device == "cuda" else False,
                disabled=True if device == "cpu" else False,
            )
            attention_slice = st.checkbox(
                "Enable attention slicing (slow)",
                value=True if device == "mps" else False,
                disabled=True if device == "cpu" else False,
            )

        if st.button("Generate", use_container_width=True):
            with st.spinner("Generating..."):
                raw_video = generate(
                    prompt=prompt,
                    num_frames=int(frames),
                    num_steps=int(steps),
                    seed=int(seed),
                    height=height,
                    width=width,
                    device=device,
                    cpu_offload=cpu_offload,
                    attention_slice=attention_slice,
                )
                video = convert_to_video(
                    video_frames=raw_video,
                    fps=int(n_fps),
                    filename=f"{prompt.replace(' ', '_').lower()}-{seed}",
                )

            with col_right:
                st.video(video)


if __name__ == "__main__":
    main()
