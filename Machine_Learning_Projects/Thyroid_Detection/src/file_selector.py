import os
import streamlit as st

def file_selector(folder_path='./data/',text='Select file path'):
    folders = [folder for folder in os.listdir(folder_path) ]
    selected_folder = st.selectbox(text, folders)
    return f'{os.path.join(folder_path, selected_folder)}'

