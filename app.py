import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Chargement du modèle (à remplacer par le chargement de votre modèle entraîné)
# Pour cet exemple, nous allons créer un modèle factice
model = LogisticRegression()
model.coef_ = np.array([[0.1, 0.2, -0.1, 0.05, 0.01]])
model.intercept_ = np.array([0])
scaler = StandardScaler()

st.title('Application de Prédiction de Crédit')

# Création des sliders pour les entrées de l'utilisateur
age = st.slider('Âge', 18, 100, 25)
income = st.slider('Revenu Annuel', 10000, 100000, 30000)
debt_to_income = st.slider('Ratio Dette/Revenu', 0.0, 1.0, 0.2)
previous_default = st.selectbox('Défaut de Paiement Précédent', options=[0, 1])
employment_length = st.slider('Durée d\'Emploi (années)', 0, 20, 2)

# Prédiction
user_input = np.array([[age, income, debt_to_income, previous_default, employment_length]])
user_input_scaled = scaler.transform(user_input)  # Assurez-vous de scaler les entrées comme lors de l'entraînement
prediction = model.predict(user_input_scaled)

if st.button('Prédire'):
    if prediction[0] == 1:
        st.write('Crédit Approuvé')
    else:
        st.write('Crédit Non Approuvé')
