# Trader Performance vs Market Sentiment Analysis

## Executive Summary

This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and profitability using Hyperliquid trading data.

The analysis investigates whether trader performance and behavior change across different sentiment regimes. In addition to exploratory data analysis, trader segmentation using clustering and a simple predictive model were implemented to better understand trading patterns.

---

## Objective

The objective of this project is to analyze the relationship between market sentiment (Fear vs Greed) and trader performance.

The analysis focuses on identifying patterns in trading behavior, profitability, and trade activity under different sentiment conditions to derive actionable trading insights.

---

## Datasets

Two datasets were used in this analysis:

1. **Bitcoin Fear & Greed Index**
   - Contains daily market sentiment classification (Fear / Greed / Extreme Fear / Extreme Greed / Neutral)

2. **Hyperliquid Historical Trader Data**
   - Includes trade-level information such as:
   - Account
   - Execution price
   - Trade size
   - Side (Buy/Sell)
   - Timestamp
   - Closed Profit and Loss (PnL)
   - Transaction details

---

## Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Analysis Performed

The following analysis steps were conducted:

- Data loading and preprocessing
- Missing value and duplicate checks
- Timestamp conversion and alignment of datasets by date
- Sentiment vs trader performance analysis
- Trade frequency analysis under different sentiment conditions
- Profitability analysis
- Behavioral analysis of trade sizes and trader activity

---

## Key Insights

1. **Trader profitability varies depending on market sentiment.**  
   Higher profits tend to appear during Greed and Extreme Greed market conditions.

2. **Trading activity increases during Fear and Extreme Greed periods.**  
   This suggests that market volatility encourages more trading activity.

3. **Trade sizes tend to increase during Greed periods.**  
   Traders appear to take larger positions when market confidence is higher.

---

## Strategy Recommendations

Based on the analysis, the following strategies may improve trading performance:

1. **Reduce trade size during Fear periods** to manage downside risk during uncertain market conditions.

2. **Increase trading activity cautiously during Greed periods** to capitalize on bullish market momentum.

---

## Bonus Analysis

Additional advanced analysis was performed to enhance the project:

### Trader Clustering

K-Means clustering was used to segment traders based on behavioral characteristics such as:

- Trade size
- Profitability

This helped identify different trading behavior patterns and trader archetypes.

### Predictive Modeling

A simple Logistic Regression model was implemented to predict whether a trade would be profitable based on trade characteristics and sentiment-related features.

This provides a preliminary approach to forecasting trader profitability.

---

## Repository Structure
