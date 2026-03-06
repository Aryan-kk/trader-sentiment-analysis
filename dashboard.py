import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Performance vs Market Sentiment Dashboard")

# load datasets
sentiment = pd.read_csv("data/fear_greed_index.csv")
trades = pd.read_csv("data/historical_data.csv")

# convert date
trades['date'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True).dt.date
sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# merge
data = pd.merge(trades, sentiment, on="date", how="inner")

st.subheader("Dataset Preview")
st.write(data.head())

# sentiment distribution
st.subheader("Market Sentiment Distribution")

fig, ax = plt.subplots()

sns.countplot(x="classification", data=data, ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)

# profit analysis
st.subheader("Trader Profit vs Market Sentiment")

fig2, ax2 = plt.subplots()

sns.boxplot(
    x="classification",
    y="Closed PnL",
    data=data,
    ax=ax2
)

plt.xticks(rotation=45)

st.pyplot(fig2)