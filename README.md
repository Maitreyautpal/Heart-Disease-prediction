❤️ Heart Disease Prediction System

A Machine Learning–powered web application that predicts the risk of Heart Disease based on patient health parameters.
Multiple Advance ML models were trained, evaluated & compared — and Logistic Regression was selected as the best model with 92.59% accuracy.

✔ Built with Python & Scikit-Learn

✔ Streamlit Web Application

✔ Model Saved Using Joblib (.pkl)

✔ Fully Deployment Ready

🚀 Live Demo

👉 https://heart-disease-prediction-v4tyhu6hshw5aenpzyvxw7.streamlit.app/

🚀 Project Features

✔️ Data Preprocessing

✔️ Feature Scaling (MinMaxScaler)

✔️ Multiple ML Models Trained & Compared

✔️ Cross Validation & Hyperparameter Tuning

✔️ Best Model Selection

✔️ Confusion Matrix & Classification Report

✔️ Streamlit Web App

✔️ Deployment Ready

📂 Dataset Features
    (Dataset : Heart_Disease_Prediction.csv by kaggle platform)

    Feature	Description

    Age	Patient’s age in years
    Sex	1 = Male, 0 = Female
    Chest pain type	0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic
    BP	Resting Blood Pressure (mmHg)
    Cholesterol	Serum cholesterol (mg/dl)
    FBS over 120	Fasting blood sugar > 120 mg/dl (1=True, 0=False)
    EKG results	Resting Electrocardiographic results
    Max HR	Maximum Heart Rate achieved
    Exercise angina	Exercise induced angina (1=yes, 0=no)
    ST depression	Depression induced by exercise
    Slope of ST	Peak exercise ST segment slope
    Number of vessels fluro	Major vessels colored by fluoroscopy
    Thallium	Thallium stress test result

🎯 Target Variable

    Heart Disease

    1 = Disease Present

    0 = No Disease

🔧 Feature Scaling

    MinMax Scaling applied:

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

🧠 Model Performance Comparison
⭐ Final Selected Model — Logistic Regression

Accuracy: 92.59%

✔ Confusion Matrix
 
     [[32,  1],
     [ 3, 18]]

✔ Classification Report

              precision    recall  f1-score   support
           0       0.91      0.97      0.94        33
           1       0.95      0.86      0.90        21
    accuracy                           0.93        54
   macro avg       0.93      0.91      0.92        54
weighted avg       0.93      0.93      0.93        54


Weighted Accuracy: 92%

🏅 Other Models Performance

    Model	Accuracy
    Decision Tree	70%
    SVC	81%
    Random Forest	83%
    KNN	85%
    XGBoost	87%
    Naive Bayes	90%
⭐  Logistic Regression (Final)	92.59%

✔ Cross Validation

   Mean CV Accuracy: 0.8262

✔ GridSearchCV Best Parameters

   Best Accuracy : 0.8522
   Best Params:
   n_estimators = 300
   min_samples_leaf = 4
   min_samples_split = 2
   max_depth = None

💾 Model Saving

    import joblib as jb
    jb.dump(model_lc,'Heart-Disease_model.pkl')
    jb.dump(scaler,'scaler.pkl')
    jb.dump(X.columns.to_list(),'columns.pkl')

🌐 Deployment

    Streamlit UI Created

    Hosted Successfully

    Mobile + Desktop Compatible

📌 Tech Stack

    Python

    Scikit-Learn

    Pandas / NumPy

    Streamlit

    Joblib

    XGBoost

🎯 Use Cases

   Early Heart Disease Screening

   Medical Decision Support

   Health Analytics

🙌 Author

   Maitreya Utpal
   💼 Aspiring Machine Learning Engineer
   📫 Feel free to connect!
