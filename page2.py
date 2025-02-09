import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, mean_squared_error

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

def select_model(y):
    model_name = st.selectbox("Choisissez un modèle", ["Random Forest", "Logistic Regression", "SVM"])
    if model_name == "Random Forest":
        n_estimators = st.slider("Nombre d'arbres", 10, 200, 100)
        model = RandomForestClassifier(n_estimators=n_estimators) if y.nunique() < 10 else RandomForestRegressor(n_estimators=n_estimators)
    elif model_name == "Logistic Regression":
        C = st.slider("Paramètre C", 0.01, 10.0, 1.0)
        model = LogisticRegression(C=C, max_iter=1000)
    elif model_name == "SVM":
        kernel = st.selectbox("Type de noyau", ["linear", "rbf", "poly"])
        model = SVC(kernel=kernel)
    return model

def train_model(model, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    if y.nunique() < 10:
        st.write("Score de précision :", accuracy_score(y_test, y_pred))
    else:
        st.write("Erreur quadratique moyenne :", mean_squared_error(y_test, y_pred))
    return model
def save_model(model):
    with open("trained_model.pkl", "wb") as f:
        pickle.dump(model, f)
    st.success("Modèle sauvegardé avec succès !")

def main():
    st.title("Application d'entraînement de modèles de Machine Learning")
    df = load_data()
    if df is not None:
        features, target = select_features_target(df)
        if features and target:
            X = df[features]
            y = df[target]
            model = select_model(y)
            if st.button("Entraîner le modèle"):
                trained_model = train_model(model, X, y)
                if st.button("Sauvegarder le modèle"):
                    save_model(trained_model)

if __name__ == "__main__":
    main()
