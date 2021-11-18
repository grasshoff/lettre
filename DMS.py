import streamlit as st 
import pandas as pd
import ast
from functions.mongo import *
from functions.ggbuttons import *
from functions.lettre_classes import *
from functions.lettre_examples import *
if 'scene' not in st.session_state:
              st.session_state['scene'] = []


logotext="lettre.<sub>digital</sub>"
st.sidebar.markdown(f'<div style="font-size: 3em">{logotext}</div>',unsafe_allow_html=True)

st.sidebar.title("Management")
st.session_state.scene=st.sidebar.selectbox("Aufgaben",["titel","isbn","vlb","news","adressen","components","examples"])
scenes={
          "examples": Examples,
          "titel": Titel,
          "isbn": ISBN,
          "vlb": VLB, 
          "news": News,
          "components": Components,
          "adressen": Adressen
          }
t=scenes[st.session_state.scene]()


connect("lettre",host="mongodb+srv://gg:gg123456@cluster0.jvjxr.mongodb.net")


if st.session_state.scene=="adressen":
          st.title("Adressen")
          nadr=list(Adressen.objects())
          na=[n.name for n in nadr]
          st.write("Anzahl",len(nadr))
          col1,col2,col3,col4,col5=st.columns([1,1,1,1,6])
          with col1:
                    if st.button("Neu"):
                              document=Adressen(name="neu").save()
          with col2:
                    if st.button("Del"):
                              Adressen.objects(name="neu").delete().save()
          with col3:
                    if st.button("Export"):
                              document.export()
          with col4:
                    if st.button("akualisieren"):
                              Adressen(name="neu")
          sel=st.selectbox("Auswahl Nachname",na)
          st.write("---")
          st.write("**Textfelder**")
          for document in Adressen.objects(name=sel):
                    document.edit_document()
                    document.save()





