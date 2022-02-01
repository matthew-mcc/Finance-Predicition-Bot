# Finance Prediction Bots
**DISCLAIMER: **
Do not use these bots for financial advice. They are machine learning and artificial predictions that have no guarantees in beating the market or making returns.

This project is a collection of Machine learning, web-scraping and artificial intelligence programs directed at analyzing stock data, making predictions and gathering information about the stock market and specific stocks. 

__Clustering.py:__\
This program is used to obtain years worth of opening and closing values for dow 30 companies. SKlearn was then used to create a normalizer and clustering model using k-mean clustering to open a pipeline on a normalizer, and after clustering and data normalization, opening and closing values are predicted.
__Price_Prediction.py:__\
  This program takes in 5-10 years worth of data from a singular stock and then trains a Machine Learning model to attempt to model how accurate the Machine Learning bot would have been over this time period.
__Stock_Screener.py:__\
  This program is used to find out the best performing n number of stocks based on some criteria set by the program (peg_ratio, moving values, prices, 52 week highs and lows etc...). 


# Software / libraries used:
- Python 3.9
- Matplotlib - _Python_
- Numpy - _Python_
- Pandas - _Python_
- Tensorflow Machine Learning - _Python_
- SkLearn - _Python_
- Scipy - _Python_
- Yahoo Finance - _Yahoo.com_


# ___USAGE___
1. Run each of the above 3 .py files (in no particular order). 
2. Currently there is no UI, so it is required to update the parameters and values in the code.

# Versions:
Currently in Beta version 1.0.

# Further implementation
Further implementation ideas include:
- Creating a UI.
- Training the model longer and with better models.
- Combining all three programs into one.
# Sources:
https://www.tensorflow.org/ \
https://www.youtube.com/c/NeuralNine
