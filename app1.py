import streamlit as st
from Strokes_models3 import main
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))


if page == "Predict":
    main()
else:
    show_explore_page()