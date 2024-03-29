import streamlit as st
import pandas as pd


st.write(" # ***DataFrame and table function***")

st.write("---")
tabel= pd.DataFrame({"Column 1": [1,2,3,4,5,6,7,8,9], "Column 2": [11,12,13,14,15,16,17,18,19],"Column 3": [21,22,23,24,25,26,27,28,29]})

st.write(" ## **Table Function**")
st.table(tabel)
st.write("---")

st.dataframe(tabel)