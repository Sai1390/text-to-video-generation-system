# Text-to-Video Generation System

https://github.com/user-attachments/assets/aa2410cb-74ad-4913-be55-ae23fbac73d1


A **Streamlit** app that leverages the [ModelScope text-to-video diffusion model](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis) to generate video clips from text prompts. Users can customize video length, frames per second (fps), and dimensions. The system is optimized to run on devices with 4GB video cards, CPUs, and Apple M chips.

## **Built with:**
- [Huggingface Diffusers](https://github.com/huggingface/diffusers) 🧨
- [PyTorch](https://github.com/pytorch/pytorch)
- [Streamlit](https://github.com/streamlit/streamlit)

## Project Overview
This application allows users to generate videos from text prompts using a diffusion-based model. It offers flexibility in terms of the video output, enabling adjustments in parameters like video length, fps, and resolution. The underlying model is pre-trained, and users can easily interact with the interface provided via the Streamlit app.

## Reference Paper

This project is based on the following research paper:

**[Make-A-Video: Text-to-Video Generation without Text-Video Data](https://arxiv.org/pdf/2209.14792)**  
*By: Uriel Singer, Adam Polyak, Thomas Hayes, Trevor Darrell, Yaniv Taigman*  
Published on *arXiv, 2022*.

You can read the full paper [here](https://arxiv.org/pdf/2209.14792).

---

## **Installation**

Before installing, ensure you have a working installation of [git](https://git-scm.com/downloads) and [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). If you have an Nvidia graphics card, it's recommended to install [CUDA](https://developer.nvidia.com/cuda-downloads) to optimize performance.

### **Steps:**

1. **Open a terminal** on your machine. For Windows users, use the Anaconda Prompt.

2. **Clone this repository:**

    ```bash
    git clone https://github.com/Sai1390/text-to-video-generation-system.git
    ```

3. **Navigate to the project folder:**

    ```bash
    cd text-to-video-generation-system
    ```

4. **Create and activate the conda environment:**

    ```bash
    conda env create -f environment.yaml
    conda activate t2v
    ```

---

## **Running the Application**

To start the app, ensure you're in the `text-to-video-generation-system` folder and follow these steps:

```bash
conda activate t2v
streamlit run app.py
```

This will automatically open the app in your default web browser.

> **Note:** The first time you run the app, it will download the necessary models from Huggingface, which may take a few minutes (10-15 mins).

## **Requirements**
- Conda v4.x.x
- Git v2.x.x
- Nvidia GPU with at least 4GB VRAM (optional but recommended)
- CUDA (for GPU acceleration)
