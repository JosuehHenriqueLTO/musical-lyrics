import requests
import streamlit as st

def search_lyric(artist, music):
    endpoint = f"https://api.lyrics.ovh/v1/{artist}/{music}"
    response = requests.get(endpoint)
    lyric = response.json()['lyrics'] if response.status_code == 200 else ""
    return lyric

st.title("Letras de músicas")

artist = st.text_input("Digite o nome do artista/banda: ", key="artist")
music = st.text_input("Digite o nome da música: ", key="music")
search = st.button("Pesquisar")

if search:
    lyric = search_lyric(artist, music)
    if lyric:
        st.text(lyric)
    else:
        st.error("Perdão, não encontramos nada...")