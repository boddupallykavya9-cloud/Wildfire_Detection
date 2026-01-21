# 🔥 Wildfire Detection Using Deep Learning

## 📌 Overview
This project detects wildfires from images using a Convolutional Neural Network (CNN).
A Streamlit web app is provided for real-time image upload and prediction.

## 🧠 Tech Stack
- Python
- TensorFlow / Keras
- Streamlit
- OpenCV
- NumPy

---

## 📂 Project Structure

wildfire_project/
├── app.py
├── train.py
├── wildfire_model_cleaned.h5   (only if < 100MB)
├── requirements.txt
├── data_split/
│   ├── train/
│   │   └── .gitkeep
│   ├── val/
│   │   └── .gitkeep
│   └── test/
│       └── .gitkeep
├── .gitignore
└── README.md

---

## 📊 Dataset
The dataset is **not included** in this repository due to size and licensing constraints.

🔗 Kaggle Dataset Link:  
https://www.kaggle.com/datasets/XXXXXXXX/wildfire-detection

### How to use the dataset
1. Download the dataset from Kaggle
2. Extract it
3. Place images inside the `data_split/` folder:
https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/wildfire-detection.git
cd wildfire-detection

### Step 2: Create a Virtual Environment

```bash
python -m venv wildfire_env

### Step 3: Activate the Virtual Environment

**Windows (PowerShell):**
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\wildfire_env\Scripts\Activate.ps1

**Windows (CMD):**
wildfire_env\Scripts\activate

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt

### Step 4: Run the Streamlit App
```bash
streamlit run app.py

The application will open in your browser at:  
👉 http://localhost:8501

---

## 🔥 Features
- Upload an image and detect **Wildfire / No Wildfire**
- Deep Learning-based CNN classifier
- Interactive Streamlit web interface
- Scalable for real-time alert integration
- Clean and modular project structure

---

## 🧪 Model Training (Optional)
To retrain the model using your own dataset:
```bash
python train.py
The trained model will be saved locally as an .h5 file 

## ⚠️ Important Notes
- The dataset is intentionally excluded from this repository
- `wildfire_env/` is a local virtual environment and must not be uploaded to GitHub
- Large model files can be excluded if size limits are exceeded

---

## 👤 Author
**Your Name**  
GitHub: https://github.com/boddupallykavya9-cloud 
Email: boddupallykavya9@gmail.com
