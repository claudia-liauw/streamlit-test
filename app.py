import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Compounding interest calculator')
col1, col2 = st.columns([1, 2], gap='medium')

with col1:
    amount = st.number_input('Principal amount', min_value=0)
    ir = st.number_input('Interest rate (% p.a.)', value=np.nan, min_value=0., max_value=100.)*0.01
    monthly = st.number_input('Monthly contributions', min_value=0)
    interval = st.radio('Preferred unit of time', ['Months', 'Years'])
    if interval == 'Months':
        time_input = st.number_input('Holding time (months)', min_value=0)
        time = time_input
    elif interval == 'Years':
        time_input = st.number_input('Holding time (years)', min_value=0)
        time = time_input*12
    clicked = st.button('Calculate')

if clicked:
    with col2:
        amount_list = [amount]
        for i in range(time):
            amount = (amount + monthly)*(1+ir/12)
            amount_list.append(amount)
        st.markdown(f'**Amount after {time_input} {interval}**: ${amount:.2f}')

        fig, ax = plt.subplots()
        if interval == 'Months':
            ax.plot(range(time+1), amount_list, marker='o')
        else:
            ax.plot(range(time_input+1), amount_list[::12], marker='o')
        ax.set_xlabel(interval)
        ax.set_title('Amount over time')
        st.pyplot(fig)