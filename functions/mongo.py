import streamlit as st
import pymongo
from mongoengine import *
import datetime

client=pymongo.MongoClient(**st.secrets["mongo"])
@st.cache(ttl=600)
def load_mongo(db):
          disconnect()
          connect(db)
          
 