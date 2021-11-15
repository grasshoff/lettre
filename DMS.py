from optparse import TitledHelpFormatter
import streamlit as st 
from warnings import filterwarnings
filterwarnings('ignore')
from functions.mongo import *
from functions.ggbuttons import *
from functions.scenes import *

if 'scene' not in st.session_state:
              st.session_state['scene'] = []


logotext="lettre.<sub>digital</sub>"
st.sidebar.markdown(f'<div style="font-size: 3em">{logotext}</div>',unsafe_allow_html=True)

st.sidebar.title("Management")
st.session_state.scene=st.sidebar.selectbox("tasks",["titel","isbn","vlb","news","adressen","components","examples"])



scenes={
          "examples": Examples,
          "titel": Titel,
          "isbn": ISBN,
          "vlb": VLB, 
          "news": News,
          "components": Components,
          "adressen": Adressen, 
          "finanz": Finanz,
          }
t=scenes[st.session_state.scene]()
