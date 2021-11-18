
import streamlit as st
from bokeh.io import show
from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models import CheckboxButtonGroup, RadioButtonGroup,CheckboxGroup,Dropdown
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from streamlit_lottie import st_lottie
import extra_streamlit_components as stx
import requests
from st_btn_select import st_btn_select
from streamlit_ace import st_ace
from mongoengine import *

def iconin(x):
          return(f'''<i class="material-icons" style="font-size: 90px">{x}</i></b>''')


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
                    
                    hh='''<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">'''
                    st.markdown(hh,unsafe_allow_html=True)
                    st.markdown('<i class="material-icons">face</i>', unsafe_allow_html=True)
                    st.markdown('<i class="material-icons">face</i>', unsafe_allow_html=True)
                    st.markdown(iconin("face"), unsafe_allow_html=True)


                    #page = st_btn_select(
                    ## The different pages
                    #('home', 'about', 'docs', 'playground','face'),
                    ## Enable navbar
                    #nav=False,
                    ## You can pass a formatting function. Here we capitalize the options
                    #format_func=lambda name: iconin(name),
                    #)
#                    
                    # create plot
                    p = figure(tools="lasso_select")
                    cds = ColumnDataSource(
                    data={
                    "x": [1, 2, 3, 4],
                    "y": [4, 5, 6, 7],
                    }
                    )
                    p.circle("x", "y", source=cds)

                    # define events
                    cds.selected.js_on_change(
                    "indices",
                    CustomJS(
                    args=dict(source=cds),
                    code="""
                    document.dispatchEvent(
                              new CustomEvent("YOUR_EVENT_NAME", {detail: {your_data: "goes-here"}})
                    )
                    """
                    )
                    )

                    # result will be a dict of {event_name: event.detail}
                    # events by default is "", in case of more than one events pass it as a comma separated values
                    # event1,event2 
                    # debounce is in ms
                    # refresh_on_update should be set to False only if we dont want to update datasource at runtime
                    # override_height overrides the viewport height
                    result = streamlit_bokeh_events(
                    bokeh_plot=p,
                    events="YOUR_EVENT_NAME",
                    key="foo",
                    refresh_on_update=False,
                    override_height=600,
                    debounce_time=500)

                    # use the result
                    #st.write(result)

                    ##### costum
                    st.header("Location")
                    loc_button = Button(label="Get Location")
                    loc_button.js_on_event("button_click", CustomJS(code="""
                        navigator.geolocation.getCurrentPosition(
                            (loc) => {
                                document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
                            }
                        )
                        """))
                    result = streamlit_bokeh_events(
                        loc_button,
                        events="GET_LOCATION",
                        key="get_location",
                        refresh_on_update=False,
                        override_height=75,
                        debounce_time=0)

                    if result:
                        if "GET_LOCATION" in result:
                            st.write(result.get("GET_LOCATION"))
                    #### button
                    st.header("button")
                    button = Button(label="Nun")
                    button.js_on_event("Nun",CustomJS(code=''' 
                                                      document.dispatchEvent(new CustomEvent("Nun", {detail: "hi"}))
                                                      '''
                                                      ))
                    result2 = streamlit_bokeh_events(
                        button,
                        events="Nun",
                        key="b",
                        refresh_on_update=True,
                        override_height=75,
                        debounce_time=0)
                    if result2:
                              if "Nun" in result:
                                      st.write(result.get("Nun"))

