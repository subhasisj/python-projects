import pandas as pd
import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
from sklearn.utils import resample
from imblearn.over_sampling import SMOTENC,RandomOverSampler,KMeansSMOTE
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def explore_data(path):

    df = load_data(path)
    if st.checkbox('Show Data'):
        st.dataframe(df.head(10))
    df_copy = df.copy()
    df_copy = analyze_and_clean(df_copy)

    

    

def analyze_and_clean(df):
    if st.button('Analyze Data') :
        with st.spinner("Processing data..."):
            st.write(df.describe())
            st.warning('Missing values (?):')
            _ = find_missing_values(df)
        # if find_missing_values(df) & st.button('Replace ? with NaN values'):
            # st.write(df)
            with st.spinner("Cleaning Data..."): 
                df = df.drop(['TBG'],axis =1)
                df = df.drop(['TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured'],axis =1)
                df = replace_with_nan(df)
                _ = find_missing_values(df)
                st.success('Missing Values Replaced with NaN')
                with st.spinner("Mapping Categorical Values..."):
                    df = map_categorical_values(df)
                    st.success('Categoricals Mapped')
                    with st.spinner("Cleaning Data..."):
                        st.write(df['referral_source'].unique())
                        df = pd.get_dummies(df, columns=['referral_source'])
                        st.success('One-Hot Encoding Unique Values in "Referrals"')
                        df = encode_target_class(df)
                        st.success('Target "Class" Encoded')
                        with st.spinner('Imputing Missing Values'):
                            df = impute_missing_values(df)
                            st.success('Missing Values Imputed')
                            st.write(df)
                            with st.spinner('Plotting Distributions'):   
                                plot_distributions(df)
                                st.text('Plotting Normalized Distribution')
                                # plot_distributions(df,normalize=True)
                                st.success('Analysis Completed.')
    return df

def impute_missing_values(data):
    imputer=KNNImputer(n_neighbors=3, weights='uniform',missing_values=np.nan)
    new_array=imputer.fit_transform(data) 
    new_data=pd.DataFrame(data=np.round(new_array), columns=data.columns)
    return new_data

def encode_target_class(df):
    label_encoder = LabelEncoder()
    df['Class'] =label_encoder.fit_transform(df['Class'])
    return df

@st.cache
def load_data(path):
    with st.spinner("Processing data..."):
        df = pd.read_csv(path)
    # loading.text('Data Loaded Successfully..')
        st.write(df)
    return df

        
def map_categorical_values(data):

    data['sex'] = data['sex'].map({'F' : 0, 'M' : 1})

    # except for 'Sex' column all the other columns with two categorical data have same value 'f' and 't'.
    # so instead of mapping indvidually, let's do a smarter work
    for column in data.columns:
        if  len(data[column].unique())==2:
            data[column] = data[column].map({'f' : 0, 't' : 1})
    return data

def replace_with_nan(df):
    for column in df.columns:
        count = df[column][df[column]=='?'].count()
        if count!=0:
            df[column] = df[column].replace('?',np.nan)
    return df

def find_missing_values(df):
    value_present=False
    for column in df.columns:
        count = df[column][df[column]=='?'].count()
        if count!=0:
            value_present = True
            st.write(column, df[column][df[column]=='?'].count())
    return value_present

def plot_distributions(df,normalize=False):
    columns = ['age','TSH','T3','TT4','T4U','FTI']
    for column in columns:
        st.subheader(f'Distribution for {column}')
        if normalize:
            hist_values = np.histogram(np.log(df[column]), bins=50, )[0]
        else:
            hist_values = np.histogram(df[column], bins=50, )[0]
        st.bar_chart(hist_values)

    # fig = go.Figure()
    # for column in columns:
    #     if normalize:
    #         df[column] = np.log(df[column])
    #         fig = px.histogram(df, x=column, nbins=50, title= f'{column} Distribution')
    #         # fig.add_trace(go.Histogram(x=np.log(df[column])))
    #     else:
    #         # fig.add_trace(go.Histogram(x=df[column]))
    #         fig = px.histogram(df, x=column, nbins=50, title= f'{column} Distribution')
    #     fig.update_layout(
    #         height=500,
    #         width=700,
    #         title_text=f"{column} Distribution")
    #     st.plotly_chart(fig)    

