import streamlit as st
import pandas as pd

st.title("Page 2")
st.write("Bienvenue sur la Page 2. Cette page est réservée aux utilisateurs avec le rôle 2.")

def load_data() -> pd.DataFrame | None:
    uploaded_file = st.file_uploader("Téléchargez votre fichier CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Aperçu des données :", df.head())
        return df
    return None

def select_features_target(df: pd.DataFrame) -> tuple[list[str], str]:
    features = st.multiselect("Sélectionnez les features", df.columns.tolist())
    target = st.selectbox("Sélectionnez la variable cible", df.columns.tolist())
    return features, target
