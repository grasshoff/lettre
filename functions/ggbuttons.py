import streamlit as st 
from inspect import getmembers
from types import FunctionType
from st_btn_select import st_btn_select

def attributes(obj):
    disallowed_names = {
      name for name, value in getmembers(type(obj)) 
        if isinstance(value, FunctionType)}
    return {
      name: getattr(obj, name) for name in dir(obj) 
        if name[0] != '_' and name not in disallowed_names and hasattr(obj, name)}

def iconin(x):
          return(f'''<i class="material-icons" style="font-size: 90px">{x}</i></b>''')
    
def style_button_row(clicked_button_ix, n_buttons):
          def get_button_indices(button_ix):
                    return {
                              'nth_child': button_ix,
                              'nth_last_child': n_buttons - button_ix + 1
                    }

          clicked_style = """
          div[data-testid*="stHorizontalBlock"] > div:nth-child(%(nth_child)s):nth-last-child(%(nth_last_child)s) button {
                    border-color: rgb(255, 75, 75);
                    color: rgb(255, 75, 75);
                    box-shadow: rgba(255, 75, 75, 0.5) 0px 0px 0px 0.2rem;
                    outline: currentcolor none medium;
          }
          """
          unclicked_style = """
          div[data-testid*="stHorizontalBlock"] > div:nth-child(%(nth_child)s):nth-last-child(%(nth_last_child)s) button {
                    pointer-events: none;
                    cursor: not-allowed;
                    opacity: 0.65;
                    filter: alpha(opacity=65);
                    -webkit-box-shadow: none;
                    box-shadow: none;
          }
          """
          style = ""
          for ix in range(n_buttons):
                    ix += 1
                    if ix == clicked_button_ix:
                              style += clicked_style % get_button_indices(ix)
                    else:
                              style += unclicked_style % get_button_indices(ix)
          st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)
          
          
