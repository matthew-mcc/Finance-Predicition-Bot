import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from yahoo_fin import stock_info as si


companies_dow30 = si.tickers_dow()
clusters = 5
start = dt.datetime.now() - dt.timedelta(days=365 * 2)
end = dt.datetime.now()

data = web.DataReader(list(companies_dow30), 'yahoo', start, end)

open_values = np.array(data["Open"].T)
close_values = np.array(data["Close"].T)
daily_movements = closevalues = open_values

normalizer = Normalizer()
clustering_model = KMeans(n_clusters=clusters, max_iter=1000)
pipeline = make_pipeline(normalizer, clustering_model)
pipeline.fit(daily_movements)
clusters = pipeline.predict(daily_movements)

results = pd.DataFrame({
    "clusters": clusters,
    "tickers": list(companies_dow30)
}).sort_values(by=["clusters"], axis=0)

print(results)