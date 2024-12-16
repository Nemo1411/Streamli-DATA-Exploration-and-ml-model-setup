import streamlit as st
from st_pages import Page, show_pages, add_page

def set_role():
    # Fonction de rappel pour enregistrer la sélection du rôle dans l'état de session
    st.session_state.role = st.session_state._role

def login():
    st.selectbox(
        "Sélectionnez votre rôle:",
        [None, "DataManager", "Manager", "Admin"],
        key="_role",
        on_change=set_role,
    )

def authenticated_menu():
    # Récupération du rôle actuel
    role = st.session_state.role

    # Liste des pages avec conditions de visibilité en fonction des rôles
    pages = [
        {"path": "presentation.py", "title": "Presentation", "icon": "material/activity", "roles": ["DataManager", "Manager", "Admin"]},
        {"path": "page1.py", "title": "Data Exploration", "icon": "material/bug_report", "roles": ["DataManager", "Admin"]},
        {"path": "page2.py", "title": "Data assembly", "icon": "material/bug_report", "roles": ["Manager", "Admin"]},
    ]

    # Affichage des pages en fonction du rôle
    show_pages([
        Page(page["path"], title=page["title"], icon=page["icon"]) 
        for page in pages if role in page["roles"]
    ])

# Déclenchement du menu d'authentification ou du menu principal
if "role" not in st.session_state or st.session_state.role is None:
    login()  # Appel de la fonction de connexion si aucun rôle n'est défini
else:
    authenticated_menu()  # Menu principal pour les utilisateurs authentifiés
