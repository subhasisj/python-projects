from training.training import Training 
from validation.validation_controller import ValidationController
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

    app_mode = st.sidebar.selectbox("Choose the app mode",["Explore Data", "Load and Validate Data","Train the model", "Inference"])
    if app_mode == "Explore Data":
        path = st.text_input('CSV file path',value = './data/combined/hypothyroid.csv')
        if path:
            explore_data(path)
            
    elif app_mode == "Load and Validate Data":
        st.header('Load and Validate Data')
        st.markdown('''
        We will load the data using a batch of training files.
        - The validation steps will include
            - Validating the data schema from JSON files
            - Preprocessing:
                - Cleaning the data by handling missing Values
                - Balancing unbalanced Classes 
        
        Please select the base folder that contains the Schema for Training Files and the path to the training files in order to continue.
        ''')
        schema_folder_path = os.path.join('.','data','schema')
        training_schema_path = file_selector(folder_path=schema_folder_path,text = 'Select the Training file schema')
        st.write(f'You selected `%s`' %training_schema_path)
        if st.checkbox('Show Schema'):
            st.write(json.loads(open(training_schema_path).read()))
        
        data_path = os.path.join('.','data')
        training_file_path = file_selector(folder_path = data_path,text = 'Select Training files path')
        st.write('You selected `%s`' % training_file_path)
        if st.checkbox('Show Files'):
            st.info('Files to train:')
            st.write([file for file in os.listdir(training_file_path) if os.path.isfile(os.path.join(training_file_path, file))])

        if st.button('Start Validation'):
            validation_controller = ValidationController(training_file_path,training_schema_path)
            validation_controller.start_validation()

    elif app_mode == "Train the model":
        st.header('Model Training')
        st.markdown('''
        We will now load the data from the stored database from the previous step.
        The training steps will include   
        - Clustering the data
        - Model training on several algorithms and finding appropriate Model for each cluster
        
        Please select the base folder that contains the Schema for Training Files DB in order to continue.
        ''')

        db_folder_path = os.path.join('.','data','Training_Batch_Files','training_db')
        db_file = file_selector(folder_path=db_folder_path,text = 'Select the Training DB')
        st.write(f'You selected `%s`' %db_file)
        
        preprocessor_path = os.path.join('.','artifacts','preprocessing')
        saved_preprocessor = file_selector(folder_path=preprocessor_path,text = 'Select the saved Preprocessor')
        st.write(f'You selected `%s`' %saved_preprocessor)

        if st.button('Begin Training'):
            training = Training(db_file,saved_preprocessor)
            with st.spinner('Starting training now, please wait....'):
                training.begin_training()
            
        
        
    elif app_mode == "Inference":
        uploaded_file = st.file_uploader("Choose a file", type=['txt', 'jpg'])
        # if uploaded_file is not None:
            # do stuff
        # readme_text.empty()
        # run_the_app()


if __name__ == '__main__':
    main()
    
    