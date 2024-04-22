import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
st.title('Plot polynomial graph')
col1, col2, col3 = st.columns([1, 1, 2], gap='medium')

with col1:
    st.header('Inputs')
    min_x = st.number_input('Lower bound x', value=-5)
    max_x = st.number_input('Upper bound x', value=5)
    power = st.slider('Degree of polynomial', 1, 3)


with col2:
    st.header('Coefficients')
    x0 = st.number_input('Intercept', value=0)
    x1 = st.number_input('$x$', value=0)
    x2 = 0
    x3 = 0
    if power > 1:
        x2 = st.number_input('$x^2$', value=0)
    if power == 3:
        x3 = st.number_input('$x^3$', value=0)
    
    st.text('')
    clicked = st.button('Draw!')

    x = np.linspace(min_x, max_x, 100)
    y = x0 + x1*x + x2*x**2 + x3*x**3

if clicked:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(0, color='grey', linewidth=.5)
    ax.axvline(0, color='grey', linewidth=.5)

    with col3:
        st.header('Graph')
        st.pyplot(fig)
