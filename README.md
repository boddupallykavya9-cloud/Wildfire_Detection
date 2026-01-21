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
[https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset]

### How to use the dataset
1. Download the dataset from Kaggle
2. Extract it
3. Place images inside the `data_split/` folder:

data_split/
├── train/
├── val/
└── test/

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/wildfire-detection.git
cd wildfire-detection

### Step 2: Create Virtual Environment
python -m venv wildfire_env

Step 3: Activate Virtual Environment
Windows (PowerShell):

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\wildfire_env\Scripts\Activate.ps1

####Windows (CMD):

wildfire_env\Scripts\activate

###Step 4: Install Dependencies

pip install -r requirements.txt

###Step 5: Run the Streamlit App

streamlit run app.py

## 🌐 Running the App
The app will open at:
👉 http://localhost:8501

## 🔥 Features
- Upload image → Predict **Fire / No Fire**
- CNN-based deep learning model
- Interactive Streamlit UI
- Easily extendable to real alert systems
- Optional visualization support

## ⚠️ Notes
- `wildfire_env/` is a local virtual environment and should not be uploaded to GitHub
- Model file is optional — retraining is supported via `train.py`

## 👤 Author
**Boddupally Kavya**  
GitHub: https://github.com/boddupallykavya9-cloud  
Email: boddupallykavya9@gmail.com
