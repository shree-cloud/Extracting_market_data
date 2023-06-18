import streamlit as st
import pandas as pd
from datetime import datetime
import os
import glob
import time

output_files = []

st.title("Money Laundering Prediction")
st.markdown("Upload the input data")


def test_function(df):
    df.drop('class', axis=1, inplace=True)

    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M")
    output_file = f"output_{timestamp}.csv"  
    df.to_csv(output_file, index=False)
    output_files.append(output_file)
    return output_file

def main():
    if st.button("Initiate Training"):
        # initiate_training_pipeline()
        pass

    uploaded_file = st.file_uploader("Upload Input File", type="csv")

    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
        @st.cache_data
        def load_data():
            df = pd.read_csv(uploaded_file)
            return df
        
        df = load_data()

        if st.checkbox('show Raw Data', False):
            st.subheader('Raw Data')
            st.write(df)

        output_file_path = test_function(df)

        st.write("Training pipeline completed!")

        with open(output_file_path, "rb") as file:
            btn = st.download_button(
                label="Download",
                data=file,
                file_name="modified_dataframe.csv",
                mime="text/csv"
            )
        

        modified_dataframe = pd.read_csv(output_file_path)
        
        if st.checkbox('show Modified Data', False):
            st.subheader('Modified Data')
            st.write(modified_dataframe)
        

if __name__ == "__main__":
    main()
