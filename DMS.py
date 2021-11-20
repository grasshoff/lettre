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
st.session_state.scene=st.sidebar.selectbox("Aufgaben",["titel","news","adressen","components","examples"])
scenes={
          "examples": Examples,
          "titel": Titel,
          "news": News,
          "components": Components,
          "adressen": Adressen
          }
t=scenes[st.session_state.scene]()


connect("lettre",host="mongodb+srv://gg:gg123456@cluster0.jvjxr.mongodb.net")


def ad_aktuell(ad_feld):
          nadr=list(Adressen.objects())
          na=[n.name for n in nadr]
          with ad_feld:
                    st.write("Anzahl",len(nadr))
          return(na)

if st.session_state.scene=="adressen":
          st.title("Adressen")
          ad_feld=st.empty()
          na=ad_aktuell(ad_feld)
          col1,col2,col3,col4,col5=st.columns([1,1,1,1,6])
          with col1:
                    if st.button("Neu"):
                              d=Adressen.objects(name="neu")
                              if d:
                                        pass
                              else:
                                        document=Adressen(name="neu").save()
                                        ad_aktuell(ad_feld)
          with col2:
                    if st.button("Del"):
                              Adressen.objects(name="neu").delete()
          with col3:
                    if st.button("Export"):
                              document.export()
#          with col4:
#                    if st.button("akualisieren"):
#                              Adressen(name="neu")
          sel=st.selectbox("Auswahl Nachname",na)
          st.write("---")
          st.write("**Textfelder**")
          for document in Adressen.objects(name=sel):
                    document.edit_document()
                    document.save()
                    ad_aktuell(ad_feld)





