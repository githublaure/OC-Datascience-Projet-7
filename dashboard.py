import streamlit as st

st.title('Credit Approval Prediction')

# Permettre à l'utilisateur de saisir ses propres données
age = st.slider('Age', 18, 100, 25)
income = st.number_input('Income', value=30000)

# Supposons que vous ayez une fonction pour prédire
if st.button('Predict'):
    prediction = model.predict([[age, income, ...]])  # Ajoutez les autres champs nécessaires
    st.write('Credit Approved' if prediction[0] == 1 else 'Credit Denied')
