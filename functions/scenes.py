from bokeh.io import show
from bokeh.models import CheckboxButtonGroup, RadioButtonGroup,CheckboxGroup,CustomJS,Dropdown
from streamlit_bokeh_events import streamlit_bokeh_events
from streamlit_lottie import st_lottie
import extra_streamlit_components as stx
from st_btn_select import st_btn_select
import streamlit as st
import yaml
from streamlit_ace import st_ace

class ISBN():
          def __init__(self):
                    self.name=""

class Titel():
          def __init__(self):
                    self.name=""
class VLB():
          def __init__(self):
                    self.name=""
class News():
          def __init__(self):
                    self.name=""
class Adressen():
          def __init__(self):
                    self.name=""
class Components():
          def __init__(self):
                    self.name=""
class Finanz():
          def __init__(self):
                    st.markdown("./finanz/software.md")

class Examples():
          def __init__(self):
                    ## material
                    loadmaterial='''<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">'''
                    st.markdown(loadmaterial,unsafe_allow_html=True)
                    ## icon
                    #st.sidebar.markdown(iconin("insert_chart"),unsafe_allow_html=True)
                    ## stepper
                    val = stx.stepper_bar(steps=["Ready", "G", "Go"])
                    ## hori radio
                    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                    st.radio(label = 'Radio buttons', options = ['R1','R2','R3'])
                    ## button selection
                    selection = st_btn_select(('option 1', 'option 2', 'option 3'))
                    ## top buttons
                    page = st_btn_select(
                    ('home', 'about', 'docs', 'playground'),
                    nav=True,
                    format_func=lambda name: name.capitalize(),
                    )
                    ## lotti
                    def load_lottieurl(url: str):
                              r = requests.get(url)
                              if r.status_code != 200:
                                        return None
                              return r.json()

                    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
                    #lottie_url="https://assets7.lottiefiles.com/datafiles/nEcNvHOihy2iUQL/data.json"
                    lottie_json = load_lottieurl(lottie_url)
                    st_lottie(lottie_json,width=233)
