import streamlit as st
import pandas as pd
import numpy as np


## Title of the component 
st.title("My First Streamlit App")

## Displaying a simple text
st.write("Hello, welcome to my first Streamlit app!")

## Displaying a dataframe
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})

## Display the dataframe in the app
st.write("Here is a simple dataframe:")
st.write(df)


## Displaying a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)