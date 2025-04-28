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


## References for SmartReco 
16.1 Research Papers / Concepts
•	Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook — Springer
•	Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix Factorization Techniques for Recommender Systems. IEEE Computer
•	Schafer, J.B., Frankowski, D., Herlocker, J., Sen, S. (2007). Collaborative Filtering Recommender Systems. In: The Adaptive Web
16.2 Deployment References
•	Gunicorn: Python WSGI HTTP Server for UNIX
https://gunicorn.org/
•	Render.com: Easy cloud hosting for Flask apps
https://render.com/
•	Heroku: PaaS platform for quick deployments
https://www.heroku.com/
  
