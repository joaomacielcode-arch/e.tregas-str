import streamlit as st
import pandas as pd
import time
import numpy as np
import folium
from folium import plugins
from streamlit_folium import folium_static
from streamlit_folium import st_folium

st.set_page_config(page_title="Entregando...", page_icon=":material/delivery_truck_speed:",initial_sidebar_state='collapsed')

st.video('./anims/univ.mp4', autoplay=True)