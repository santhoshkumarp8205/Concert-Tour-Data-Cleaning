import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)

pd.set_option('display.width', None)

pd.set_option('display.max_columns', None)




dt = pd.read_csv("D:\\Datasets\\END TO END SALESSTORE DATA\\SuperStoreOrders - SuperStoreOrders.csv")
a = ['order_date','ship_date','year']
dt[a] = dt[a].apply(lambda x: pd.to_datetime(x,format="mixed"))
# print(dt.columns)
# print(dt.info())

dt["year"]=dt["year"].dt.year
dt["sales"] = dt["sales"].str.replace(",","").astype(int)
dt["price"] = np.divide(dt["sales"],dt["quantity"]).astype("int")
print(dt.head(50))




