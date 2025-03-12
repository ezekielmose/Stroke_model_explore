import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/ezekielmose/StrokeModel/main/your_file.csv"  # Update with the correct URL
    dataset = pd.read_csv(url)
    

    # checking for the null values
    dataset.isnull().sum()
    # calculating the mean for bmi column to do imputation
    stroke_data = dataset.bmi.mean()
    dataset1 = dataset.fillna(stroke_data)
    dataset1.isnull().sum()
    # drop the id column 
    dataset2 = dataset1.drop(columns='id', axis=1)

    # summary statstics
    dataset2.describe().T
    return dataset2


dataset3 = load_data()


def show_explore_page():

    st.title("Model Dashboard")

    # PIE CHART
    st.write("Pie Chart")
    value_counts_wt = dataset3.work_type.value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(value_counts_wt, labels=value_counts_wt.index, shadow= True, autopct="%1.f%%")
    ax1.axis("equal")
    st.pyplot(fig1)

    st.markdown("<hr style='border:3px solid black'>", unsafe_allow_html=True)

    # SCATTER PLOT
    fig1, ax1 = plt.subplots()
    st.write("Scatter plot for age vs bmi")
    st.scatter_chart(x='age', y='bmi', data=dataset3)

    #st.pyplot(fig1)

    st.markdown("<hr style='border:3px solid black'>", unsafe_allow_html=True)
    # count unique values
    value_counts_gender = dataset3.gender.value_counts()
    st.bar_chart(data=value_counts_gender)
    


if __name__ == "__main__":
    show_explore_page()
