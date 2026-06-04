# 🎨 NeuralArt AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/PyTorch-2.7-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/AdaIN-Neural%20Style%20Transfer-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Gradio-6.16-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/HuggingFace-Live-yellow?style=for-the-badge">
</p>

<h2 align="center">
Transform Ordinary Photos into Stunning Artwork using Neural Style Transfer
</h2>

<p align="center">
🚀 Powered by AdaIN • PyTorch • Gradio • Hugging Face
</p>

<p align="center">
<a href="https://harshitpundir-neuralart.hf.space">
  <img src="https://img.shields.io/badge/🚀%20Launch%20Demo-LIVE-success?style=for-the-badge">
</a>
</p>

---

## 🌟 Overview

NeuralArt AI is a Deep Learning based Neural Style Transfer application that converts ordinary photographs into artistic masterpieces.

The project uses **Adaptive Instance Normalization (AdaIN)** to combine the content of one image with the artistic style of another image while preserving visual quality and structure.

Built completely using **PyTorch**, deployed on **Hugging Face Spaces**, and wrapped in a modern **Gradio UI**.

---

## ✨ Features

* 🎨 Neural Style Transfer using AdaIN
* 🖼️ Upload Content & Style Images
* 🎛️ Adjustable Style Strength
* ⚡ Fast PyTorch Inference
* 🌈 Modern Interactive UI
* ☁️ Hugging Face Deployment
* 📥 Download Generated Artwork
* 🚀 Real-Time Processing

---

## 🚀 Live Demo

### Try NeuralArt AI

👉 https://harshitpundir-neuralart.hf.space

---

## 📸 Application Preview

### Home Screen

> Add screenshot here

```text
assets/home.png
```

### Style Transfer Result

> Add screenshot here

```text
assets/result.png
```

---

## 🧠 How It Works

```text
Content Image
       │
       ▼
   VGG Encoder
       │
       ▼
Content Features
       │
       ▼
AdaIN Layer ◄────── Style Features
       │
       ▼
 Decoder Network
       │
       ▼
Stylized Artwork
```

---

## 🏗️ Model Pipeline

1. Upload a Content Image
2. Upload a Style Image
3. Extract Deep Features using VGG Encoder
4. Apply Adaptive Instance Normalization (AdaIN)
5. Decode Features into Stylized Image
6. Download Final Artwork

---

## 📊 Project Highlights

| Feature                 | Status |
| ----------------------- | ------ |
| AdaIN Implementation    | ✅      |
| PyTorch Model           | ✅      |
| Interactive Gradio UI   | ✅      |
| Hugging Face Deployment | ✅      |
| Style Strength Control  | ✅      |
| Open Source             | ✅      |

---

## 🛠️ Tech Stack

### Deep Learning

* PyTorch
* AdaIN
* VGG Encoder
* Decoder Network

### Frontend

* Gradio
* HTML
* CSS

### Deployment

* Hugging Face Spaces
* Hugging Face Hub

---

## 📂 Project Structure

```text
NeuralArt/
│
├── app.py
├── train.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── utils/
│   ├── __init__.py
│   ├── models.py
│   └── utils.py
│
├── examples/
│   ├── brad_pitt.jpg
│   ├── picasso_seated_nude_hr.jpg
│   ├── sketch.png
│   ├── stylized_brad_pitt.jpg
│   └── stylized_brad_pitt (1).jpg
│
├── content_data/
├── style_data/
├── static/
├── templates/
├── experiment/
│
└── Demo_IO_Images/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Harshit-pundir/NeuralArt.git
cd NeuralArt
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🎯 Usage

1. Upload a Content Image
2. Upload a Style Image
3. Adjust Style Strength
4. Click **Generate Masterpiece**
5. Download Generated Artwork

---

## 🔮 Future Improvements

* 🎭 Multiple Style Presets
* ⚡ GPU Acceleration
* 📦 Batch Processing
* 📱 Mobile Optimization
* 🖼️ Style Gallery
* 👤 User Authentication
* 🎨 AI Recommended Styles

---

## 👨‍💻 Author

### Harshit Pundir

B.Tech Computer Science Student
AI / ML Enthusiast

🔗 GitHub: https://github.com/Harshit-pundir

🤗 Hugging Face: https://huggingface.co/harshitpundir

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates future development and helps the project reach more developers.

---

<p align="center">
Made with ❤️ using PyTorch, AdaIN and Hugging Face
</p>
