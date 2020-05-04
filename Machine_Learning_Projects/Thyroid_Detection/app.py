from training.training import Training
import streamlit as st
import pandas as pd
from src.exploration import explore_data
from src.file_selector import file_selector
import os
import json


# import ptvsd
# print('Waiting for debugger attach')
# ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
# ptvsd.wait_for_attach()

# ./data/combined/hypothyroid.csv
def main():
    st.sidebar.title('Classify Thryoid Type')
    st.sidebar.header("What to do ?")

    app_mode = st.sidebar.selectbox("Choose the app mode",["Explore Data", "Train the model", "Inference"])
    if app_mode == "Explore Data":
        path = st.text_input('CSV file path',value = './data/combined/hypothyroid.csv')
        if path:
            explore_data(path)
            
    elif app_mode == "Train the model":
        st.markdown('''
        We will train the model using a batch of training files.
        - The preprocessing steps will include
            - Validating the data schema from JSON files
            - Cleaning the data by handling missing Values
            - Sampling Classes 
        
        Please select the base folder that contains the Schema for Training Files and the path to the training files in order to continue.
        ''')
        schema_folder_path = os.path.join('.','data','schema')
        training_schema_path = file_selector(folder_path=schema_folder_path,text = 'Select the Training file schema')
        st.write(f'You selected `%s`' %training_schema_path)
        st.write(json.loads(open(training_schema_path).read()))
        
        data_path = os.path.join('.','data')
        training_file_path = file_selector(folder_path = data_path,text = 'Select Training files path')
        st.write('You selected `%s`' % training_file_path)
        st.info('Files to train:')
        st.write([file for file in os.listdir(training_file_path) if os.path.isfile(os.path.join(training_file_path, file))])

        # st.button('Start Training')
        if st.button('Start Training'):
            training = Training(training_file_path,training_schema_path)
            training.start_training()
        # readme_text.empty()
        # st.code(get_file_content_as_string("app.py"))
    # elif app_mode == "Run the app":
        # readme_text.empty()
        # run_the_app()


if __name__ == '__main__':
    main()
    
    