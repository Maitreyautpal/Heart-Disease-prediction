
❤️ Heart Disease Prediction System

A Machine Learning–powered web application that predicts the risk of heart disease based on patient health parameters.
The project compares multiple ML models and selects the Logistic Regression model as the best final model with 92.59% accuracy.

Application is deployed using Streamlit, and trained model is saved using Joblib (.pkl).

🚀 Live Demo
👉  https://heart-disease-prediction-v4tyhu6hshw5aenpzyvxw7.streamlit.app/

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
Number of vessels fluro	Number of major vessels colored by fluoroscopy
Thallium	Thallium stress test result

🎯 Target Variable

Heart Disease → 1 = Disease Present, 0 = No Disease

🔧 Feature Scaling

MinMax Scaling applied on numeric features:

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

🧠 Model Performance Comparison

Below are the results of all trained models:

⭐ Final Selected Model — Logistic Regression

Accuracy: 0.9259

Confusion Matrix
[[32,  1],
 [ 3, 18]]

##Classification Report:
              precision    recall  f1-score   support

           0       0.91      0.97      0.94        33
           1       0.95      0.86      0.90        21

    accuracy                           0.93        54
   macro avg       0.93      0.91      0.92        54
weighted avg       0.93      0.93      0.93        54


Weighted Accuracy: 92%

🏅 Other Models Performance
🔹 KNN

Accuracy: 0.8518

[[28,  5],
 [ 3, 18]]

🔹 SVC

Accuracy: 0.8148

[[28,  5],
 [ 5, 16]]

🔹 Decision Tree

Accuracy: 0.7037

[[22, 11],
 [ 5, 16]]

🔹 Naive Bayes

Accuracy: 0.9074

[[32,  1],
 [ 4, 17]]

🔹 XGBoost

Accuracy: 0.8703

[[31, 2],
 [ 5, 16]]

🔹 Random Forest

Accuracy: 0.8333

[[25, 5],
 [ 4, 20]]

Cross Validation

Mean CV Accuracy: 0.8262

GridSearchCV Best Result
Best Accuracy: 0.8522
Best Params:
max_depth=None
min_samples_leaf=4
min_samples_split=2
n_estimators=300

🏆 Conclusion

Among all models:

Model	Accuracy
Decision Tree	70%
SVC	81%
Random Forest	83%
KNN	85%
XGBoost	87%
Naive Bayes	90%
⭐ Logistic Regression (FINAL)	92.59% ✔️

👉 Logistic Regression performs the best with:

-Highest accuracy

-Best balanced precision & recall

-Stable performance

-Lower overfitting risk

So it is selected as the final deployed model.

💾 Model Saving

Model, scaler and feature columns are saved using Joblib:

import joblib as jb
jb.dump(model_lc,'Heart-Disease_model.pkl')
jb.dump(scaler,'scaler.pkl')
jb.dump(X.columns.to_list(),'columns.pkl')

🌐 Deployment

Streamlit UI created

Hosted successfully

Mobile & desktop compatible

📌 Tech Stack

Python

Scikit-Learn

Pandas / Numpy

Streamlit

Joblib

XGBoost

🎯 Use Case

Early heart disease risk screening

Medical decision support

Health analytics

🙌 BY:
Maitreya
💼 Aspiring Machine Learning Engineer
📫 Feel free to connect!
