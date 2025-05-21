# 🧠 OCR Image Text Extractor

A Python-based Optical Character Recognition (OCR) tool to extract text from images using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). This project supports both PIL-based and OpenCV-based image preprocessing for improved accuracy.

---

## 🚀 Features

- Extracts text from images using [pytesseract](https://pypi.org/project/pytesseract/)
- Dual preprocessing methods: **PIL** (Python Imaging Library) and **OpenCV**
- Contrast enhancement, binarization, blurring, dilation/erosion for noise reduction
- Supports multiple languages via Tesseract's language packs
- Command-line interface for quick usage

---

## 🛠️ Requirements

- Python 3.6+
- Tesseract OCR (must be installed and optionally linked in your environment)

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/HappySR/ocr-image-text-extractor.git
cd ocr-image-text-extractor
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Install Tesseract OCR:**

* **Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install tesseract-ocr
```

* **Mac (Homebrew):**

```bash
brew install tesseract
```

* **Windows:**
  Download and install from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
  Note the path to the `tesseract.exe` for use in the script.

---

## 🖼️ Usage

```bash
python ocr_script.py path/to/image.jpg
```

### Optional arguments:

* `--tesseract` or `-t`: Path to the Tesseract executable (required if not in PATH)
* `--lang` or `-l`: Language for OCR (default: `eng`)
* `--no-cv2`: Use PIL-based preprocessing instead of OpenCV

### Example:

```bash
python ocr_script.py sample.png --lang eng --tesseract "C:/Program Files/Tesseract-OCR/tesseract.exe"
```

---

## 📂 Project Structure

```
ocr-image-text-extractor/
├── ocr_script.py           # Main script with OCRProcessor class and CLI
├── README.md               # README file
├── requirements.txt        # Required Python packages
```

---

## 📌 Notes

* OpenCV-based preprocessing generally yields better OCR accuracy for noisy images.
* Tesseract supports multiple languages, but the relevant language data must be installed.
* For best results, ensure the input image has good contrast and minimal background noise.

---

## 🧪 Sample Output

```
--- OCR Result ---
This is a sample text extracted
from an image using OCR!
------------------
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [pytesseract](https://github.com/madmaze/pytesseract)
* [Pillow](https://python-pillow.org/)
* [OpenCV](https://opencv.org/)

```
