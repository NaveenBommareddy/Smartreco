# SmartReco - AI-Powered Product Recommendation Web App

SmartReco is a Python Flask web application that simulates an e-commerce website.  
It tracks user interactions and provides personalized product recommendations in real-time using machine learning (SVD algorithm from Surprise library).

---

## 🚀 Features
- Dynamic product listing page
- Live user interaction tracking (clicks, views)
- Personalized top-N product recommendations
- Machine Learning model (SVD) retrains after each interaction
- Clean Bootstrap 5 frontend design
- Easy deployment on Render.com, Heroku, or other cloud platforms

---

## 🛠️ Built With
- Python 3.8+
- Flask
- Pandas
- Scikit-Surprise
- Bootstrap 5
- SQLite (for lightweight storage)

---

## 📂 Folder Structure
smartreco_website/
├── app.py
├── model.py
├── db.py
├── data/
│   ├── products.csv
│   └── interactions.csv
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── recommendations.html
│   ├── admin.html (optional)
├── static/(optional)
│   ├── style.css
│   └── images/
├── requirements.txt
└── README.md
