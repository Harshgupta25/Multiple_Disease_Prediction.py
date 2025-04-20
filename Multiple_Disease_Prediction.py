# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 01:59:52 2025

@author: Harsh Gupta
"""
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

diabetes _model = pickle.load(open("C:/Users/Harsh Gupta/OneDrive/Desktop/Multiple Disease Prediction System/saved models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/Harsh Gupta/OneDrive/Desktop/Multiple Disease Prediction System/saved models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/Harsh Gupta/OneDrive/Desktop/Multiple Disease Prediction System/saved models/parkinsons_model.sav", 'rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                            ['Diabetes Prediction',
                             'heart Disease Prediction',
                             'Parkinsons Prediction' ],
                            default_index = 0)
