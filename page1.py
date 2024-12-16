import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Tableau de Bord Interactif avec Streamlit")

st.header("Options")

# Chargement des données
uploaded_file = st.file_uploader("Télécharger un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header("Filtrage des Données")
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Sélectionnez les colonnes à afficher", columns, default=columns)

    st.header("Visualisation des Données")
    chart_type = st.selectbox(
        "Choisissez un type de graphique",
        ["Tableau", "Histogramme", "Graphique en barres", "Graphique linéaire", "Diagramme circulaire"]
    )

    st.write("## Aperçu des Données")
    st.dataframe(df[selected_columns])

    if chart_type == "Tableau":
        st.write("## Données Filtrées")
        st.dataframe(df[selected_columns])

    elif chart_type == "Histogramme":
        st.write("## Histogramme")
        x_column = st.selectbox("Sélectionnez la colonne des abscisses (X)", selected_columns)
        plt.figure(figsize=(10, 4))
        sns.histplot(df[x_column], kde=True)
        st.pyplot(plt)

    elif chart_type == "Graphique en barres":
        st.write("## Graphique en barres")
        x_column = st.selectbox("Sélectionnez la colonne des abscisses (X)", selected_columns)
        y_column = st.selectbox("Sélectionnez la colonne des ordonnées (Y)", selected_columns)
        plt.figure(figsize=(10, 4))
        sns.barplot(x=x_column, y=y_column, data=df)
        st.pyplot(plt)

    elif chart_type == "Graphique linéaire":
        st.write("## Graphique linéaire")
        x_column = st.selectbox("Sélectionnez la colonne des abscisses (X)", selected_columns)
        y_column = st.selectbox("Sélectionnez la colonne des ordonnées (Y)", selected_columns)
        plt.figure(figsize=(10, 4))
        sns.lineplot(x=x_column, y=y_column, data=df)
        st.pyplot(plt)

    elif chart_type == "Diagramme circulaire":
        st.write("## Diagramme circulaire")
        label_column = st.selectbox("Sélectionnez la colonne des labels", selected_columns)
        value_column = st.selectbox("Sélectionnez la colonne des valeurs", selected_columns)
        plt.figure(figsize=(8, 8))
        plt.pie(df[value_column], labels=df[label_column], autopct='%1.1f%%')
        st.pyplot(plt)

else:
    st.write("Téléchargez un fichier CSV pour commencer.")
