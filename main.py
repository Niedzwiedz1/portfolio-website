import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Lukasz Niewadzi")
    bio = """
    Surveyor working in UK with a demonstrated history in the Infrastructure industry. 
    Skilled in Rail, UAV, BIM surveys. Good knowledge of using Leica Total Station, Amberg Measuring Device, 
    Terrestrial Laser Scanner and GPS instruments. Bachelor's degree focused in Surveying Technology/Surveying at 
    University of Agriculture in Krakow.
    """
    st.info(bio)

content1 = """
Bellow you can find some of the apps I have build in Python.
            """
st.write(content1)
