import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

import glob

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
filepath = glob.glob("diary/*.txt")
from pathlib import Path

st.title("Diary tony")
st.subheader("Positivity")

pos=[]
days=[]
neg=[]
for file in filepath:
    text = open(file, "r")
    content = text.read()
    # df =pd.read_csv(file)

    file_name=Path(file)
    filename = file_name.stem
    dt=datetime.datetime.strptime(filename, '%Y-%m-%d').strftime( "%b%d")
    # print(dt)
    days.append(dt)
    # print(f"{filename} \n  {df}")
    indecators = analyzer.polarity_scores(content)
    # positivity_append
    positive = indecators["pos"]
    pos.append(positive)
    # negative_append
    negative = indecators["neg"]
    neg.append(negative)
    print(indecators)

figure = px.line(x=days, y=pos, labels={"x":"Days", "y":"Positive"})
st.plotly_chart(figure)

st.subheader("Negativity")

figure_neg = px.line(x=days, y=neg, labels={"x":"Days", "y":"Negativity"})
st.plotly_chart(figure_neg)

