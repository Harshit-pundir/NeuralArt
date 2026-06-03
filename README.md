# 🎨 NeuralArt

NeuralArt is a Flask and PyTorch powered Neural Style Transfer web application that uses **Adaptive Instance Normalization (AdaIN)** to transform content images into artistic masterpieces. Users can upload content and style images, adjust style intensity, and generate high-quality stylized artwork through an intuitive web interface.

---

## 🚀 Features

* Upload content and style images
* Adjustable style strength control
* Real-time neural style transfer
* Download generated stylized images
* Modern and responsive UI
* Powered by AdaIN architecture
* Fast inference using PyTorch

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* PyTorch
* TorchVision

### Frontend

* HTML5
* CSS3
* JavaScript

### Deep Learning

* Adaptive Instance Normalization (AdaIN)
* VGG Encoder
* Custom Decoder Network

---

## 📂 Project Structure

```text
ai-nst-project/
│
├── NST_Code/
│   ├── app.py
│   ├── utils/
│   ├── templates/
│   ├── static/
│   ├── content_data/
│   ├── style_data/
│   └── experiment/
│
├── Demo_IO_Images/
├── requirements.txt
├── README.md
└── Procfile.txt
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

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python NST_Code/app.py
```

Open:

```text
http://localhost:5000
```

in your browser.

---

## 🖼️ How It Works

1. Upload a content image.
2. Upload a style image.
3. Adjust style strength using the slider.
4. Click **Transfer Style**.
5. Download the generated stylized image.

---

## 📸 Sample Result

Input Content Image + Style Image → NeuralArt → Stylized Output

(Add screenshots here)

---

## 🔮 Future Improvements

* Multiple artistic style presets
* GPU acceleration support
* User authentication
* Image gallery and history
* Cloud deployment

---

## 👨‍💻 Author

**Harshit Pundir**

B.Tech CSE Student | AI/ML Enthusiast

GitHub: https://github.com/Harshit-pundir

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
