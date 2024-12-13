import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données utilisateurs
lesDonneesDesComptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "administrateur",
        },
    }
}

# Configuration de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire
)

authenticator.login()


def menu():
    with st.sidebar:
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        st.write(f"Bonjour {st.session_state['username']} !\n  Bienvenue 👋")
        st.image(
            "https://i.ibb.co/Ky1X36J/87182348-10222001005955480-8937443002964508672-n.jpg"
        )
        selection = option_menu(
            menu_title=None, options=["Accueil", "Photos"], default_index=0
        )
        authenticator.logout("Déconnexion")
    return selection


link1 = "https://i.ibb.co/q9PvP6T/Z9-D-2914-scaled.jpg"
link2 = "https://images.squarespace-cdn.com/content/v1/5f931cbffe1da91af483fe93/d6c89625-f4b6-472b-a2a1-ca45a60720e4/rowing-web.jpg"
link3 = "https://i.ibb.co/3Y821zs/257371732-10227167452953426-3873435735623571116-n.jpg"


def album():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(link1)
        st.header("Team corporate")
    with col2:
        st.image(link2)
        st.header("Sunrise")
    with col3:
        st.image(link3)
        st.header("Memories")


if st.session_state["authentication_status"]:
    selection = menu()
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.title("Bienvenue sur mon album d'une ancienne passion")
        album()


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplie")
