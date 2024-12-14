import streamlit as st
import pandas as pd
import numpy as np

# Judul Dashboard
st.title("Dashboard dengan streamlit")

# Menambahkan slider
slider_value = st.slider("pilih nilai:", 0, 100, 50)

# Menampilkan data
st.write(f"nilai yang dipilih: {slider_value}")

# membuat dataFrame
data = pd.DataFrame(
    np.random.rand(10, 2),
    columns=['kolom 1', 'kolom 2']
)

# Menampilkan DataFrame
st.write("Data Acak:")
st.dataframe(data)

# Menambahkan grafik
st.line_chart(data)