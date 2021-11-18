from streamlit_lottie import st_lottie
import extra_streamlit_components as stx
from st_btn_select import st_btn_select
import streamlit as st
from streamlit_ace import st_ace
from mongoengine import *
import datetime

class ISBN(Document):
          def __init__(self):
                    self.name=""

class Titel(Document):
          def __init__(self):
                    self.name=""
class VLB(Document):
          def __init__(self):
                    self.name=""
class News(Document):
          def __init__(self):
                    self.name=""
class Components(Document):
          def __init__(self):
                    self.name=""

class Adressen(Document):
          vorname = StringField()
          name = StringField()
          email = StringField()
          tel = StringField()
          titel = StringField()
          ort = StringField()
          plz = StringField()
          strasse = StringField()
          kategorie = ListField(StringField(max_length=30))
          buch = StringField()
          reihe = StringField()
          notiz = StringField()
          link_url = StringField()
          image = ImageField()
          date_modified = DateTimeField(default = datetime.datetime.utcnow)
          
                    
          def edit_document(self):
                    '''
                    fields=d._fields: dict of fields in a document
                    lf=list(fields.keys()): list aller felder
                    f=lf[0] field
                    d[f] value of field f
                    b= d[f].__class__ == type(None) : boolean of type None for a field value
                    bs= isinstance(d[f],str): boolean of type of field value ist str
                    '''
                    icol=3
                    col1,col2,col3 = st.columns(icol)
                    idx=0
                    for ix,f in enumerate(self._fields):
                              bdf=isinstance(self[f],str)
                              tt=self[f].__class__ == type(None)
                              if bdf or tt:
                                        idx+=1
                                        if (idx % icol)==0:
#                                                  st.write(0,(idx % icol),idx)
                                                  self[f]=col1.text_input(f,value=self[f],key=idx)
                                        if (idx % icol)==1:
#                                                  st.write(1,(idx % icol),idx)
                                                  self[f]=col2.text_input(f,value=self[f],key=idx)          
                                        if (idx % icol)==2:
#                                                  st.write(2,(idx % icol),idx)
                                                  self[f]=col3.text_input(f,value=self[f],key=idx)          
                    



          
          
          
