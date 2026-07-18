#Pandas


import pandas as pd
import numpy as np
from fontTools.varLib.instancer import names

# #Series
# #1 dimensional data
# dt = [50,60,70]
# s = pd.Series(data = dt)
# print(s)
# """
# #output
# 0    50
# 1    60
# 2    70
# dtype: int64
# """
#
#
#
# dt = [100,200,300,400]
# idx = [2,3,4,5] #len of data = len of index --> list or array used for make serious
# c = pd.Series(data = dt,dtype=int,index=idx,copy=True,name="sample")
# print(c)
# """
# #output:
# 2    100
# 3    200
# 4    300
# 5    400
# Name: sample, dtype: int64
# """
#
#
# dt = [100,200,300,400]
# idx = [2,3,4,5,6,7] #len of data = len of index --> list or array used for make serious
# c = pd.Series(data = dt,dtype=int,index=idx,copy=True,name="sample")
# print(c)
# """
# #output:
# ValueError: Length of values (4) does not match length of index (6)
# """
#
#
#
# #dtype = object
# dt = [100.2,200,"sss",400]
# c = pd.Series(data = dt)
# print(c)
# """
# #output
# 0    100.2
# 1      200
# 2      sss
# 3      400
# dtype: object
# """
#
#
#
#
# dt = [100,"sss",300,400]
# idx =  [100,200,"sss",400]
# c = pd.Series(data = dt,index=idx)
# print(c)
# """
# #output:
# 100    100
# 200    sss
# sss    300
# 400    400
# dtype: object
# """
#
#
# #dict to Series
# dic = {"name":"santhosh","age": 21,"native":"apm"}
# s = pd.Series(dic)
# print(s)
# """
# #output:
# name      santhosh
# age             21
# native         apm
# dtype: object
# """
#
#
#
# #dict didn't have an index, keys was taken as index as default
# dic = {"name":"santhosh","age": 21,"native":"apm"}
# idx = [100,200,300]
# s = pd.Series(data=dic,index=idx)
# print(s)
# """
# #output:
# 100    NaN
# 200    NaN
# 300    NaN
# dtype: object
# """
#
#
#
#
# dic = {"name":"santhosh","age": 21,"native":"apm"}
# idx = ["name","age","native"]
# s = pd.Series(data=dic,index=idx)
# print(s)
# """
# #output:
# name      santhosh
# age             21
# native         apm
# dtype: object
# """
#
#
#
# #index will search the value for that key by dict
# dic = {"name":"santhosh","age": 21,"native":"apm"}
# idx = ["name","native","age"]
# s = pd.Series(data=dic,index=idx)
# print(s)
# """
# #output:
# name      santhosh
# native         apm
# age             21
# dtype: object
# """
#
#
#
#
# '''
# index will search the value for that key by dict but the value didn't in the dict so NAN
# will be produced
# '''
# dic = {"name":"santhosh","age": 21,"native":"apm"}
# idx = ["name",33,"native","age",22]
# s = pd.Series(data=dic,index=idx)
# print(s)
# """
# #output:
# name      santhosh
# 33             NaN
# native         apm
# age             21
# 22             NaN
# dtype: object
# """
#
#
#
#
# #Sort by index wise and data wise
# dic = {"name":"santhosh","age": 21,"native":"apm",55:"zzz"}
# s = pd.Series(data=sorted(dic))
# print(s)
# """
# #output:
# Traceback (most recent call last):
#   File "D:\ds\python files\pandas\pandas_py.py", line 158, in <module>
#     s = pd.Series(data=sorted(dic))
# TypeError: '<' not supported between instances of 'int' and 'str'
# """
#
# #overcome by below way
# dic = {"name":"santhosh","zage": "22","native":"apm","55":"zzz"}
# s = pd.Series(dic)
# print(s.sort_index())
# """
# #output:
# 55             zzz
# name      santhosh
# native         apm
# zage            22
# dtype: object
# """
#
# print(s.sort_values())
# """
# #output
# zage            22
# native         apm
# name      santhosh
# 55             zzz
# dtype: object
# """
#
#
#
# #just reference
# dic = {"name":"santhosh","zage": "22","native":"apm","55":"zzz"}
# s = pd.Series(data = sorted(dic),index = sorted(dic.values()))
# print(s)
# """
# #output:
# 22              55
# apm           name
# santhosh    native
# zzz           zage
# dtype: object
# """
#
#
# #indexing and slicing
# """
# loc: It is a label-based accessor used to retrieve data by its name or index label.
#
# iloc: It is an integer-based accessor used to retrieve data by its numerical position starting from 0.
# """
# dic = {"name":"santhosh","zage": 22,"native":"apm",55:"zzz"}
# s = pd.Series(dic)
# # print(s[0]) #warning to access by position
# print(s["name"])
# print(s.iloc[0]) #access by position
# print(s.loc["name"]) #access by index label
# print(s.loc[55]) #access by index label but index label is not there so error
#
#
# # first value is inclusive and second value is exclusive
# print(s[0:2])
# """
# #output:
# name      santhosh
# zage            22
# dtype: object
# """
#
#
#
#
# print(s["zage":55])
# """
# #output:
# zage       22
# native    apm
# 55        zzz
# dtype: object
# """
#
#
#
#
# print(s["name":"native"])
# """
# #output:
# name      santhosh
# zage            22
# native         apm
# dtype: object
# """
#
#
# print(s[1:3])
# """
# #output:
# zage       22
# native    apm
# dtype: object
# """
#
#
# print(s[2:300])
# """
# #output:
# native    apm
# 55        zzz
# dtype: object
# """
#
#
#
#
# #indexing by our own index
# data = [100,200,300,400]
# idx = ["a","b","c","d"]
# s = pd.Series(data=data,index=idx)
# print(s[["a","c","d"]])
# """
# #output:
# a    100
# c    300
# d    400
# dtype: int64
# """
#
#
#
# print(s[["a","a","a"]])
# """
# #output:
# a    100
# a    100
# a    100
# dtype: int64
# """
#
#
#
# dic = {"name":"santhosh","zage": 22,"native":"apm",55:"zzz"}
# s = pd.Series(dic,name="sample")
#
# print(s.keys())#only for dict like series
# #Index(['name', 'zage', 'native', 55], dtype='object')
#
#
# print(s.values)
# #['santhosh' 22 'apm' 'zzz']
#
#
# print(s.items())
# #<zip object at 0x000001BD07173FC0>
#
#
# c = s.items()
# print(list(c))
# #[('name', 'santhosh'), ('zage', 22), ('native', 'apm'), (55, 'zzz')]
#
#
# print(s.shape)
# #(4,)
#
#
# print(s.ndim)
# #1
#
#
# print(s.nbytes)
# #32
#
#
# print(s.size)
# #4
#
# print(s.empty)
# #False
#
#
# print(s.index)
# #Index(['name', 'zage', 'native', 55], dtype='object')
#
#
# print(s.dtype)
# #object
#
#
# print(s.name)
# #sample
#
#
# print(s.is_unique)
# #True
#
#
# print(s.array)
# """
# #output:
# <NumpyExtensionArray>
# ['santhosh', 22, 'apm', 'zzz']
# Length: 4, dtype: object
# """
#
#
#
#
# #DataFrame
# dt = list("apple")
# c = pd.DataFrame(dt)
# print(c)
# """
# #output
#    0
# 0  a
# 1  p
# 2  p
# 3  l
# 4  e
# """
#
#
#
#
#
#
# dt = ["santhosh","kumar","saker","ravi"]
# c = pd.DataFrame(data = dt,dtype=object,index=[1,2,3,4],columns=["name"])
# print(c)
# """
# #output
#        name
# 1  santhosh
# 2     kumar
# 3     saker
# 4      ravi
# """
#
#
#
#
# """
# dt = ["santhosh","kumar","saker","ravi"]
# c = pd.DataFrame(data = dt,dtype=object,index=[1,2,3,4],columns=["name","age"])
# print(c)
#
# #output:
# Traceback (most recent call last):
#   File "D:\data science\pandas_py.py", line 403, in <module>
#     c = pd.DataFrame(data = dt,dtype=object,index=[1,2,3,4],columns=["name","age"])
#   File "D:\ds\python files\learning\.venv\lib\site-packages\pandas\core\\frame.py", line 871, in __init__
#     mgr = ndarray_to_mgr(
#   File "D:\ds\python files\learning\.venv\lib\site-packages\pandas\core\internals\construction.py", line 336, in ndarray_to_mgr
#     _check_values_indices_shape_match(values, index, columns)
#   File "D:\ds\python files\learning\.venv\lib\site-packages\pandas\core\internals\construction.py", line 420, in _check_values_indices_shape_match
#     raise ValueError(f"Shape of passed values is {passed}, indices imply {implied}")
# ValueError: Shape of passed values is (4, 1), indices imply (4, 2)
# """
#
#
#
# dt = ["santhosh","kumar","saker","ravi"]
# c = pd.DataFrame(data = dt,dtype=object,index=list(range(1,len(dt)+1)),columns=["name"])
# print(c)
# """
# #output
#        name
# 1  santhosh
# 2     kumar
# 3     saker
# 4      ravi
# """
#
#
# #dic to DataFrame --> we didn't mention the columns
# dt = {"name":"santhosh","age":23,"native":"apm"} #keys are column name and values will data for that column
# row_id = np.arange(1,len(dt)+1)*100
# c = pd.DataFrame(data = dt,index = row_id)
# print(c)
# """
# #output:
#          name  age native
# 100  santhosh   23    apm
# 200  santhosh   23    apm
# 300  santhosh   23    apm
# """
#
#
#
# #dic of list
# dt = {
#     "name": ["santhosh", "kumar", "ravi", "murali", "jack","ttt"],
#     "age": [23, 45, 32, 45, 32,90],
#     "number": [83, 96, 18, 24, 40,87]
# }
# column = ["name","native","age"]
# df = pd.DataFrame(dt,columns=column)
# df.index = np.arange(1, len(df) + 1)
# print(df)
# """
# #output:
#        name native  age
# 1  santhosh    NaN   23
# 2     kumar    NaN   45
# 3      ravi    NaN   32
# 4    murali    NaN   45
# 5      jack    NaN   32
# 6       ttt    NaN   90
# """
#
#
#
# dt = {
#     "name": ["santhosh", "kumar", "ravi", "murali", "jack","ttt"],
#     "age": [23, 45, 32, 45, 32,90],
#     "number": [83, 96, 18, 24, 40,87]
# }
# df = pd.DataFrame(dt)
# df.index = list("santho")
# print(df)
# """
# #output:
#       name  age  number
# s  santhosh   23      83
# a     kumar   45      96
# n      ravi   32      18
# t    murali   45      24
# h      jack   32      40
# o       ttt   90      87
# """
#
#
#
#
# #list of dict
# dt = [{"name":"santhosh","age":21,"number":83},{"name":"nithish","age":23},{"age":50},{"name":"raj","age":54,"number":43},{}]
# df = pd.DataFrame(dt)
# print(df)
# """
# #output:
#        name   age  number
# 0  santhosh  21.0    83.0
# 1   nithish  23.0     NaN
# 2       NaN  50.0     NaN
# 3       raj  54.0    43.0
# 4       NaN   NaN     NaN
# """
#
#
#
#
#
#
# dt = [{"name":"santhosh","age":21,"number":83},{"name":"nithish","age":23},{"age":50},{"name":"raj","age":54,"number":43},{}]
# df = pd.DataFrame(dt)
# df.index = df.index = [f"row {i}" for i in range(1, len(df) + 1)]
# print(df)
# """
# #output:
#            name   age  number
# row 1  santhosh  21.0    83.0
# row 2   nithish  23.0     NaN
# row 3       NaN  50.0     NaN
# row 4       raj  54.0    43.0
# row 5       NaN   NaN     NaN
# """
#
#
#
#
#
# dt = [{"name":"santhosh","age":21,"number":83},{"name":"nithish","age":23},{"age":50},{"name":"raj","age":54,"number":43},{}]
# df = pd.DataFrame(dt,columns=["name","age","native","number"])
# df.index = df.index = [f"row {i}" for i in range(1, len(df) + 1)]
# print(df)
# """
# #output:
#            name   age  native  number
# row 1  santhosh  21.0     NaN    83.0
# row 2   nithish  23.0     NaN     NaN
# row 3       NaN  50.0     NaN     NaN
# row 4       raj  54.0     NaN    43.0
# row 5       NaN   NaN     NaN     NaN
# """
#
#
# #dic to series
# dt = {"name":pd.Series(["santhosh","kumar","saker","ravi"],[30,40,50,60]),"NNN":pd.Series(["santhosh","kumar","saker","ravi"],[30,400,500,600])}
# df = pd.DataFrame(dt)
# print(df)
# """
# #output:
#          name       NNN
# 30   santhosh  santhosh
# 40      kumar       NaN
# 50      saker       NaN
# 60       ravi       NaN
# 400       NaN     kumar
# 500       NaN     saker
# 600       NaN      ravi
# """
#
#
#
#
#
# dt = {"name":pd.Series(["santhosh","kumar","saker","ravi"],[30,40,50,60]),"NNN":pd.Series(["santhosh","kumar","saker","ravi"],[30,400,500,600])}
# df = pd.DataFrame(dt)
# print(df["name"])
# """
# #output:
# 30     santhosh
# 40        kumar
# 50        saker
# 60         ravi
# 400         NaN
# 500         NaN
# 600         NaN
# Name: name, dtype: object
# """
#
#
#
# print(df["NNN"])
# """
# #output:
# 30     santhosh
# 40          NaN
# 50          NaN
# 60          NaN
# 400       kumar
# 500       saker
# 600        ravi
# Name: NNN, dtype: object
# """
#
#
# #indexing from dataframe with rows and columns
# dt = {"name":["santhosh","kumar","ram","sam","jhon"],"age":[21,22,23,21,24],"marks":[320,440,220,315,200]}
# df = pd.DataFrame(data = dt)
# df.index = [f"Row{i}" for i in range(1,len(df)+1)]
# print(df)
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row3       ram   23    220
# Row4       sam   21    315
# Row5      jhon   24    200
# """
#
#
# #row indexing by using loc --> last value is inclusive
# print(df.loc["Row3"])
# """
# #output:
# name     ram
# age       23
# marks    220
# Name: Row3, dtype: object
# """
#
#
# print(df.loc["Row3":"Row4"])
# """
# #output:
#       name  age  marks
# Row3   ram   23    220
# Row4   sam   21    315
# """
#
#
#
# print(df.loc["Row1":"Row5":2])
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row3       ram   23    220
# Row5      jhon   24    200
# """
#
#
#
# print(df.loc[["Row1","Row5","Row3"]])
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row5      jhon   24    200
# Row3       ram   23    220
# """
#
#
# print(df.loc[["Row1"],["name"]])
# """
# #output:
#           name
# Row1  santhosh
# """
#
#
# print(df.loc[["Row1"],"name":"marks"])
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# """
#
# print(df.loc["Row2":"Row5","name":"marks"])
# """
# #output:
#        name  age  marks
# Row2  kumar   22    440
# Row3    ram   23    220
# Row4    sam   21    315
# Row5   jhon   24    200
# """
#
#
# print(df.loc[df["marks"]>250])
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row4       sam   21    315
# """
#
#
#
# print(df.loc[df["marks"]>250,"name":"age"])
# """
# #output:
#           name  age
# Row1  santhosh   21
# Row2     kumar   22
# Row4       sam   21
# """
#
#
#
# print(df.loc[df["age"] <= 21,"name":"age"])
# """
# #output:
#           name  age
# Row1  santhosh   21
# Row4       sam   21
# """
#
#
#
# #row indexing by using iloc --> last value is exclusive
# print(df.iloc[2])
# """
# #output:
# name     ram
# age       23
# marks    220
# Name: Row3, dtype: object
# """
#
#
#
# print(df.iloc[2:6])
# """
# #output:
#       name  age  marks
# Row3   ram   23    220
# Row4   sam   21    315
# Row5  jhon   24    200
# """
#
#
# print(df.iloc[1:4:2])
# """
# #output:
#        name  age  marks
# Row2  kumar   22    440
# Row4    sam   21    315
# """
#
#
#
# print(df.iloc[[3,4,1]])
# """
# #output:
#        name  age  marks
# Row4    sam   21    315
# Row5   jhon   24    200
# Row2  kumar   22    440
# """
#
#
#
# print(df.iloc[[2],[1]])
# """
# #output:
#       age
# Row3   23
# """
#
#
# target = df.columns[2]
# print(df.loc[df[target]>250]) #filtering by using only loc because we want to access the column by name
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row4       sam   21    315
# """
#
#
#
#
# #adding new column
# df["result"] = ["pass" if i>250 else "fail" for i in df["marks"]]
# print(df)
# """
# #output:
#           name  age  marks result
# Row1  santhosh   21    320   pass
# Row2     kumar   22    440   pass
# Row3       ram   23    220   fail
# Row4       sam   21    315   pass
# Row5      jhon   24    200   fail
# """
#
#
# #example2
# df["grade"] = ["A" if i>350 else "B" if i>250 else "C" for i in df["marks"]]
# print(df)
# """
# #output:
#           name  age  marks result grade
# Row1  santhosh   21    320   pass     B
# Row2     kumar   22    440   pass     A
# Row3       ram   23    220   fail     C
# Row4       sam   21    315   pass     B
# Row5      jhon   24    200   fail     C
# """
#
#
#
# df["summary"] = ["bad" if i < 250 else "good" if 250 > i < 300 else "excellent" for i in df["marks"]]
# print(df)
# """
# #output:
#           name  age  marks result grade    summary
# Row1  santhosh   21    320   pass     B  excellent
# Row2     kumar   22    440   pass     A  excellent
# Row3       ram   23    220   fail     C        bad
# Row4       sam   21    315   pass     B  excellent
# Row5      jhon   24    200   fail     C        bad
# """
#
#
#
# #update the value of existing row
# df.loc["Row3","name"] = "suresh"
# print(df)
# """
# #output:
#           name  age  marks result grade    summary
# Row1  santhosh   21    320   pass     B  excellent
# Row2     kumar   22    440   pass     A  excellent
# Row3    suresh   23    220   fail     C        bad
# Row4       sam   21    315   pass     B  excellent
# Row5      jhon   24    200   fail     C        bad
# """
#
#
# df.loc["Row3","marks"] = 260
# print(df)
# """
# #output:
#           name  age  marks result grade    summary
# Row1  santhosh   21    320   pass     B  excellent
# Row2     kumar   22    440   pass     A  excellent
# Row3    suresh   23    260   fail     C        bad
# Row4       sam   21    315   pass     B  excellent
# Row5      jhon   24    200   fail     C        bad
# """
#
#
#
# df["summary"] = ["bad" if i < 250 else "good" if 250 < i < 300 else "excellent" for i in df["marks"]]
# print(df)
# """
# #output:
#           name  age  marks result grade    summary
# Row1  santhosh   21    320   pass     B  excellent
# Row2     kumar   22    440   pass     A  excellent
# Row3    suresh   23    260   fail     C       good
# Row4       sam   21    315   pass     B  excellent
# Row5      jhon   24    200   fail     C        bad
# """
#
#
#
# #update the existing index of row
# df["Row3":"Row5"] = [["suresh",23,260,"fail","C","good"],["raju",24,200,"fail","C","bad"],["kumar",22,440,"pass","A","excellent"]]
# print(df)
# """
# #output:
#           name  age  marks result grade    summary
# Row1  santhosh   21    320   pass     B  excellent
# Row2     kumar   22    440   pass     A  excellent
# Row3    suresh   23    260   fail     C       good
# Row4      raju   24    200   fail     C        bad
# Row5     kumar   22    440   pass     A  excellent
# """
#
#
# #del the column
# del df["summary"]
# print(df)
# """
# #output:
#           name  age  marks result grade
# Row1  santhosh   21    320   pass     B
# Row2     kumar   22    440   pass     A
# Row3    suresh   23    260   fail     C
# Row4      raju   24    200   fail     C
# Row5     kumar   22    440   pass     A
# """
#
#
# df.pop("grade")
# print(df)
# """
# #output:
#           name  age  marks result
# Row1  santhosh   21    320   pass
# Row2     kumar   22    440   pass
# Row3    suresh   23    260   fail
# Row4      raju   24    200   fail
# Row5     kumar   22    440   pass
# """
#
#
# #this function only slicing the dataframe by using index label so it didn't delete the data permanently
# trn = df.truncate(before = "Row2",after = "Row4",axis = 0)
# print(trn)
# """
# #output:
#         name  age  marks result
# Row2   kumar   22    440   pass
# Row3  suresh   23    260   fail
# Row4    raju   24    200   fail
# """
#
#
# """
# this function by column slicing at first we sort the column by index wise
# then we slice the dataframe by using column index label and it didn't delete the data permanently
#
# but
#
# df["age":"result"] this is best way to slice the dataframe by column index label because
# it is more readable and we didn't sort the column by index wise
# """
# df_sort = df.sort_index(axis=1)
# trn = df_sort.truncate(before = "age",after = "result",axis = 1)
# print(trn)
# """
# #output:
#       age  marks      name result
# Row1   21    320  santhosh   pass
# Row2   22    440     kumar   pass
# Row3   23    260    suresh   fail
# Row4   24    200      raju   fail
# Row5   22    440     kumar   pass
# """
#
#
#
# drp = df.drop(labels="result",axis = 1) #it is permanently delete the column but axis = 1 is mandatory to delete the column
# print(drp)
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row3    suresh   23    260
# Row4      raju   24    200
# Row5     kumar   22    440
# """
#
#
#
# #delete a rows
# drp = df.drop(labels="Row3",axis = 0,inplace=False) #it is permanently delete the row but axis = 0 is mandatory to delete the row
# print(drp)
# """
# #output:
#           name  age  marks result
# Row1  santhosh   21    320   pass
# Row2     kumar   22    440   pass
# Row4      raju   24    200   fail
# Row5     kumar   22    440   pass
# """
#
#
# drp = df.drop(labels="marks",axis = 1,inplace=False) #it is permanently delete the row but axis = 0 is mandatory to delete the row
# print(drp)
# """
# #output:
#           name  age result
# Row1  santhosh   21   pass
# Row2     kumar   22   pass
# Row3    suresh   23   fail
# Row4      raju   24   fail
# Row5     kumar   22   pass
# """
#
# print(df) #after drop the row3 it is not deleted permanently because we used inplace = False
# """
#           name  age  marks result
# Row1  santhosh   21    320   pass
# Row2     kumar   22    440   pass
# Row3    suresh   23    260   fail
# Row4      raju   24    200   fail
# Row5     kumar   22    440   pass
# """
#
# # del df.loc["Row4":"Row5"] # this will only delete the columns by quick way
# # print(df)
#
# """
# #difference between drop, pop, truncate and del
#
# 1. drop()
# Definition: A highly flexible Pandas function used to remove specific rows or columns from a DataFrame based on their labels.
#
# Key Feature: It does not modify the original DataFrame unless you explicitly set inplace=True.
#
# Direction: Can remove both Rows (axis=0) and Columns (axis=1).
#
# 2. pop()
# Definition: A Pandas function that permanently deletes a single column from the DataFrame and simultaneously returns that deleted column data.
#
# Key Feature: It modifies the original DataFrame immediately and allows you to store the removed column into a new variable.
#
# Direction: Strictly works on Columns only.
#
# 3. del
# Definition: A standard, built-in Python keyword used to quickly and permanently delete a single column from a DataFrame in-place.
#
# Key Feature: It directly modifies the original DataFrame and does not return any data.
#
# Direction: Strictly works on Columns only.
#
# 4. truncate()
# Definition: A Pandas function used to slice (crop) a DataFrame based on an index boundary limit using before and after thresholds.
#
# Key Feature: It never deletes anything from the original DataFrame; it just creates a sliced copy. The index must be sorted.
#
# Direction: Can slice both Rows (axis=0) and Columns (axis=1).
# """
#
#
# #adding(append) new rows and columns
# dt = {"name":["santhosh","kumar","ram","sam","jhon"],"age":[21,22,23,21,24],"marks":[320,440,220,315,200]}
# df1 = pd.DataFrame(data = dt)
# df1.index = [f"Row{i}" for i in range(1,len(df1)+1)]
# print(df1)
#
# dt1 = [{"name":"suresh","age":25,"marks":260},{"name":"raju","age":24,"marks":200},{"name":"kumaran","age":22,"marks":440}]
# df2 = pd.DataFrame(dt1)
# df2.index = [f"Row{i}" for i in range(1,len(df2)+1)]
# print(df2)
#
#
# apd = df1._append(df2,ignore_index=True)
# print(apd)
# """
# #output:
#        name  age  marks
# 0  santhosh   21    320
# 1     kumar   22    440
# 2       ram   23    220
# 3       sam   21    315
# 4      jhon   24    200
# 5    suresh   25    260
# 6      raju   24    200
# 7   kumaran   22    440
# """
#
#
#
# apd = df1._append(df2,ignore_index=False)
# print(apd)
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row3       ram   23    220
# Row4       sam   21    315
# Row5      jhon   24    200
# Row1    suresh   25    260
# Row2      raju   24    200
# Row3   kumaran   22    440
# """
#
#
#
#
# apd = df1._append(df2,ignore_index=True)
# apd.index = [f"Row{i}" for i in range(1,len(apd)+1)]
# print(apd)
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row3       ram   23    220
# Row4       sam   21    315
# Row5      jhon   24    200
# Row6    suresh   25    260
# Row7      raju   24    200
# Row8   kumaran   22    440
# """
#
#
# #to append a rows by using concate function
# apd = pd.concat([df1,df2],ignore_index=True)
# print(apd)
# """
# #output:
#        name  age  marks
# 0  santhosh   21    320
# 1     kumar   22    440
# 2       ram   23    220
# 3       sam   21    315
# 4      jhon   24    200
# 5    suresh   25    260
# 6      raju   24    200
# 7   kumaran   22    440
# """
#
#
# apd = pd.concat([df1,df2],ignore_index=False)
# print(apd)
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# Row3       ram   23    220
# Row4       sam   21    315
# Row5      jhon   24    200
# Row1    suresh   25    260
# Row2      raju   24    200
# Row3   kumaran   22    440
# """
#
#
#
# """
# #difference between append and concat
# 1. concat() (The Multi-Directional Joiner)
# Definition:
#  A highly powerful and efficient Pandas function used to combine
#  multiple DataFrames or Series along a particular axis (either rows or columns).
#
# Direction:
#  It can combine data vertically (one below the other using axis=0) as well as
#  horizontally (side-by-side using axis=1).
#
# Flexibility:
#  It accepts a list of multiple DataFrames [df1, df2, df3] at the same time,
#  making it faster and optimized for memory.
#
# 2. append() (The Old Row Adder - Deprecated)
# Definition:
#  An older DataFrame method specifically designed to append rows of another DataFrame or
#  dictionary to the end of the current DataFrame.
#
# Direction:
#  It strictly worked vertically (Rows only, axis=0). It did not support horizontal combination.
#
# Limitation:
#  It was highly inefficient because every time you appended a row,
#  Pandas would create a brand new copy of the DataFrame in memory. (Hence, it was removed in recent versions).
# """
#
#
#
#
# dt = {"name":["santhosh","kumar","ram","sam","jhon"],"age":[21,22,23,21,24],"marks":[320,440,220,315,200]}
# df1 = pd.DataFrame(data = dt)
# df1.index = [f"Row{i}" for i in range(1,len(df1)+1)]
#
# print(df1.ndim)
# #2
#
# print(df1.keys())
# #Index(['name', 'age', 'marks'], dtype='object')
#
# print(df1.index)
# #Index(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], dtype='object')
#
# print(df1.items())
# #<generator object DataFrame.items at 0x00000223DD0920A0>
#
# a = df1.items()
# print(list(a))
# """
# #output:
# Name: age, dtype: int64), ('marks', Row1    320
# Row2    440
# Row3    220
# Row4    315
# Row5    200
# Name: marks, dtype: int64)]
# """
#
#
# print(df1.size)
# #15
#
#
#
# #np.random
# print(np.random.random())
# #0.2626403039683569
#
#
# print(np.random.random(4))
# #[0.93555423 0.94235086 0.17635614 0.64542373]
#
#
# print(np.random.rand(5))
# #[0.08223108 0.52004528 0.78278151 0.58430844 0.98203   ]
#
#
#
# print(np.random.randn(5))
# #[ 0.1942409  -1.07908292 -0.58153052 -1.86264069 -0.77505834]
#
#
#
# print(np.random.randint(4))
# #3
#
#
#
# print(np.random.randint(low=5,high=15))
# #11
#
#
#
# print(np.random.randint(low=5,high=20,size=5))
# #[ 8 16 15 19 18]
#
#
#
# #series with functionality
# dt = pd.Series(data = np.random.rand(5))
# dt.index = [f"row {x}" for x in range(1,len(dt)+1)]
#
# print(dt)
# print(dt.axes)
# """
# #output:
# row 1  0.601669
# row 2  0.513271
# row 3  0.112193
# row 4  0.745790
# row 5  0.373940
# [Index(['row 1', 'row 2', 'row 3', 'row 4', 'row 5'], dtype='object')]
# """
#
#
#
#
# dt = pd.Series(data = np.random.rand(5))
#
# # print(dt)
# print(dt.axes)
# """
# #output:
#
# [RangeIndex(start=0, stop=5, step=1)]
# """
#
#
# dt = pd.Series(data = np.random.rand(5),index=[1,2,3,4,5])
# print(dt.axes)
# #[Index([1, 2, 3, 4, 5], dtype='int64'),]
#
#
#
# dt = pd.Series(data = np.random.rand(5),index=[1,2,3,4,5])
# print(dt.empty)
# #False
#
#
#
#
# dt = pd.Series(data = np.random.rand(10))
# dt.index = [f"row {x}" for x in range(1,len(dt)+1)]
# print(dt.head(6))
# """
# #row 1    0.763200
# row 2    0.329758
# row 3    0.533077
# row 4    0.688162
# row 5    0.793377
# row 6    0.503935
# dtype: float64
# """
#
# print(dt.tail(6))
# """
# #output:
# row 5     0.583286
# row 6     0.807256
# row 7     0.937154
# row 8     0.797710
# row 9     0.437199
# row 10    0.043932
# dtype: float64
# """
#
#
#
# dt = pd.Series(data = np.random.rand(3))
# dt.index = [f"row {x}" for x in range(1,len(dt)+1)]
# print(type(dt))
# #<class 'pandas.core.series.Series'>
#
#
#
#
# #DataFrame with functionality
# dt = pd.DataFrame(data = np.random.rand(5))
# dt.index = [f"row {x}" for x in range(1,len(dt)+1)]
# dt.columns = ["marks"]
# print(dt)
# """
# #output:
#           marks
# row 1  0.021893
# row 2  0.558742
# row 3  0.989736
# row 4  0.700096
# row 5  0.967897
# """
#
#
# dt = {"name":["santhosh","kumar","ram","sam","jhon"],"age":[21,22,23,21,24],"marks":[320,440,220,315,200]}
# df = pd.DataFrame(data = dt)
# df.index = [f"Row{i}" for i in range(1,len(df)+1)]
# print(df.values)
# """
# #output:
# [['santhosh' 21 320]
#  ['kumar' 22 440]
#  ['ram' 23 220]
#  ['sam' 21 315]
#  ['jhon' 24 200]]
# """
#
#
#
#
# print(df.index)
# #Index(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], dtype='object')
#
#
# print(df.columns)
# #Index(['name', 'age', 'marks'], dtype='object')
#
#
#
# print(df.axes)  # -->  columns and index is called axes
# #[Index(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], dtype='object'), Index(['name', 'age', 'marks'], dtype='object')]
#
#
# print(df.shape)
# #(5, 3)
#
#
# print(df.size)
# #15
#
#
# print(df.ndim)
# #2
#
#
# print(df.T)#transpose
# """
# #output:
#            Row1   Row2 Row3 Row4  Row5
# name   santhosh  kumar  ram  sam  jhon
# age          21     22   23   21    24
# marks       320    440  220  315   200
# """
#
#
#
# print(df.head(2))
# """
# #output:
#           name  age  marks
# Row1  santhosh   21    320
# Row2     kumar   22    440
# """
#
#
#
# print(df.tail(2))
# """
# #output:
#       name  age  marks
# Row4   sam   21    315
# Row5  jhon   24    200
# """
#
# #descriptive statistics
#
# #for clarification
# dt = {"marks":pd.Series([1,2,3,4,5]),"age":pd.Series([20,40,34,41,25])}
# df = pd.DataFrame(data = dt)
# df.index = [f"row {x}" for x in range(1,len(df)+1)]
#
# print(df)
# """
# #output:
#        marks  age
# row 1      1   20
# row 2      2   40
# row 3      3   34
# row 4      4   41
# row 5      5   25
# """
#
#
# print(df["marks"])
# print(type(df["marks"]))
# """
# #output:
# row 1    1
# row 2    2
# row 3    3
# row 4    4
# row 5    5
# Name: marks, dtype: int64
# <class 'pandas.core.series.Series'>
# """
#
#
#
# #this is 2 dimensional data so that was a DataFrame
# print(df[["marks"]])
# print(type(df[["marks"]]))
# """
# #output:
#        marks
# row 1      1
# row 2      2
# row 3      3
# row 4      4
# row 5      5
# <class 'pandas.core.frame.DataFrame'>
# """
#
#
#
# #skipna
# dt = {"marks":pd.Series([1,2,3,4,5]),"age":pd.Series([20,40,34,41,np.nan])}
# df = pd.DataFrame(data = dt)
# df.index = [f"row {x}" for x in range(1,len(df)+1)]
#
#
#
# print(df.sum(skipna = False))
# """
# this will not skip the nan so that was not be function the operation properly
#
# #output:
# marks    15.0
# age       NaN
# dtype: float64
# """
#
#
# print(df.sum(skipna = True))
# """
# this will skip the nan so that was be function the operation properly
#
# #output:
# marks     15.0
# age      135.0
# dtype: float64
# """
#
#
#
#
# dt = {"name":["santhosh","naveen","suresh","mahesh","ravi"],"marks":[50,25,36,49,58,],"age":[20,40,34,41,25]}
# df = pd.DataFrame(data = dt)
# df.index = [f"row {x}" for x in range(1,len(df)+1)]
# print(df)
# """
# #output:
#            name  marks  age
# row 1  santhosh     50   20
# row 2    naveen     25   40
# row 3    suresh     36   34
# row 4    mahesh     49   41
# row 5      ravi     58   25
# """
#
#
# #pd.mean()
# #print(df.mean()) --> this is error only numeric columns
# print(df[["marks","age"]].mean())
# """
# #output:
# marks    43.6
# age      32.0
# dtype: float64
# """
#
#
#
# print(df["marks"].mean())
# #43.6
#
#
#
# #axis = 1
# print(df[["marks","age"]].mean(axis=0,skipna=True))
# """
# #output:
# marks    43.6
# age      32.0
# dtype: float64
# """
#
#
#
# #axis = 0
# print(df[["marks","age"]].mean(axis=1,skipna=True))
# """
# #output:
# row 1    35.0
# row 2    32.5
# row 3    35.0
# row 4    45.0
# row 5    41.5
# dtype: float64
# """
#
#
#
#
#
# #pd.median()
# #print(df.median()) --> this is error only numeric columns
# print(df[["marks","age"]].median())
# """
# #output:
# marks    49.0
# age      34.0
# dtype: float64
# """
#
#
#
#
# print(df["marks"].median())
# #49.0
#
#
#
# #axis = 1
# print(df[["marks","age"]].median(axis=1,skipna=True))
# """
# #output:
# row 1    35.0
# row 2    32.5
# row 3    35.0
# row 4    45.0
# row 5    41.5
# dtype: float64
# """
#
#
#
# #axis = 0
# print(df[["marks","age"]].median(axis=0,skipna=True))
# """
# #output:
# marks    49.0
# age      34.0
# dtype: float64
# """
#
#
#
#
#
#
#
# dt = {"name":["santhosh","naveen","santhosh","mahesh","naveen"],"marks":[50,25,36,49,58,],"age":[20,40,34,41,25]}
# df = pd.DataFrame(data = dt)
# df.index = [f"row {x}" for x in range(1,len(df)+1)]
#
#
# #pd.mode()
# print(df.mode())
# """
# #output:
#        name  marks  age
# 0  santhosh     25   20
# 1       NaN     36   25
# 2       NaN     49   34
# 3       NaN     50   40
# 4       NaN     58   41
# """
#
#
# print(df[["name"]].mode())
# """
# #output:
#        name
# 0    naveen
# 1  santhosh
# """
#
#
#
#
#
#
# #axis = 1
# print(df[["name"]].mode(axis=1))
# """
# #output:
#               0
# row 1  santhosh
# row 2    naveen
# row 3  santhosh
# row 4    mahesh
# row 5    naveen
# """
#
#
#
# #axis = 0
# print(df[["name"]].mode(axis = 0))
# """
# #output:
#        name
# 0    naveen
# 1  santhosh
# """
#
#
# #pd.std()
# # print(df.std()) #given only numeric
# print(df[["age","marks"]].std())
# """
# #output:
# age       9.246621
# marks    13.049904
# dtype: float64
# """
#
#
#
# print(df[["age","marks"]].std(axis = 1))
# """
# #output:
# row 1    21.213203
# row 2    10.606602
# row 3     1.414214
# row 4     5.656854
# row 5    23.334524
# dtype: float64
# """
#
#
#
#
# print(df[["age","marks"]].std(axis = 0))
# """
# #output:
# age       9.246621
# marks    13.049904
# dtype: float64
# """
#
#
#
# #df.min()
# print(df.min())
# """
# #output:
# name     mahesh
# marks        25
# age          20
# dtype: object
# """
#
#
#
# print(df[["marks","age"]].min())
# """
# #output:
# marks    25
# age      20
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].min(axis=1))
# """
# #output:
# row 1    20
# row 2    25
# row 3    34
# row 4    41
# row 5    25
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].min(axis=0))
# """
# #output:
# marks    25
# age      20
# dtype: int64
# """
#
#
#
# #df.max()
# print(df.max())
# """
# #output:
# name     santhosh
# marks          58
# age            41
# dtype: object
# """
#
#
#
# print(df[["marks","age"]].max())
# """
# #output:
# marks    58
# age      41
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].max(axis=1))
# """
# #output:
# row 1    50
# row 2    40
# row 3    36
# row 4    49
# row 5    58
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].max(axis=0))
# """
# #output:
# marks    58
# age      41
# dtype: int64
# """
#
#
#
# #df.sum()
# print(df.sum())
# """
# #output:
# name     santhoshnaveensanthoshmaheshnaveen
# marks                                   218
# age                                     160
# dtype: object
# """
#
#
#
#
#
# print(df[["marks","age"]].sum())
# """
# #output:
# dtype: object
# marks    218
# age      160
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].sum(axis=1))
# """
# #output:
# row 1    70
# row 2    65
# row 3    70
# row 4    90
# row 5    83
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].sum(axis=0))
# """
# #output:
# marks    218
# age      160
# dtype: int64
# """
#
#
#
#
# #df.prod()
# # print(df.prod()) --> str column have in this df
# """
# #output:
# error
# """
#
#
#
#
#
# print(df[["marks","age"]].prod())
# """
# #output:
# marks    127890000
# age       27880000
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].prod(axis=1))
# """
# #output:
# row 1    1000
# row 2    1000
# row 3    1224
# row 4    2009
# row 5    1450
# dtype: int64
# """
#
#
#
# print(df[["marks","age"]].sum(axis=0))
# """
# #output:
# marks    218
# age      160
# dtype: int64
# """
#
#
#
# #df.cumsum()
# print(df.cumsum())
# """
# #output:
#                                      name  marks  age
# row 1                            santhosh     50   20
# row 2                      santhoshnaveen     75   60
# row 3              santhoshnaveensanthosh    111   94
# row 4        santhoshnaveensanthoshmahesh    160  135
# row 5  santhoshnaveensanthoshmaheshnaveen    218  160
# """
#
#
#
# print(df[["marks","age"]].cumsum(axis = 1)) #in categorical data type doesnt accepted for this row_wise calculation
# """
# #output:
#        marks  age
# row 1     50   70
# row 2     25   65
# row 3     36   70
# row 4     49   90
# row 5     58   83
# """
#
#
#
# print(df[["marks","age"]].cumsum(axis = 0))
# """
# #output:
#        marks  age
# row 1     50   20
# row 2     75   60
# row 3    111   94
# row 4    160  135
# row 5    218  160
# """
#
#
#
#
# print(df.cumsum(axis = 0))
# """
# #output:
#                                      name  marks  age
# row 1                            santhosh     50   20
# row 2                      santhoshnaveen     75   60
# row 3              santhoshnaveensanthosh    111   94
# row 4        santhoshnaveensanthoshmahesh    160  135
# row 5  santhoshnaveensanthoshmaheshnaveen    218  160
# """
#
#
#
# #df.cumprod()
# # print(df.cumprod()) #this cumprod and prod doesnt support catogorical value
# """
# #output:
#  error
# """
#
#
#
# print(df[["marks","age"]].cumprod(axis = 1)) #in categorical data type doesnt accepted for this row_wise calculation
# """
# #output:
#        marks   age
# row 1     50  1000
# row 2     25  1000
# row 3     36  1224
# row 4     49  2009
# row 5     58  1450
# """
#
#
#
# print(df[["marks","age"]].cumprod(axis = 0))
# """
# #output:
#            marks       age
# row 1         50        20
# row 2       1250       800
# row 3      45000     27200
# row 4    2205000   1115200
# row 5  127890000  27880000
# """
#
#
#
#
# #df.cummin()
# print(df.cummin())
# """
# #output:
# row 1  santhosh     50   20
# row 2    naveen     25   20
# row 3    naveen     25   20
# row 4    mahesh     25   20
# row 5    mahesh     25   20
# """
#
#
#
# print(df[["marks","age"]].cummin(axis = 1))
# """
# #output:
#        marks  age
# row 1     50   20
# row 2     25   25
# row 3     36   34
# row 4     49   41
# row 5     58   25
# """
#
#
#
# print(df[["marks","age"]].cummin(axis = 0))
# """
# #output:
#        marks  age
# row 1     50   20
# row 2     25   20
# row 3     25   20
# row 4     25   20
# row 5     25   20
# """
#
#
#
#
# #df.cummax()
# print(df.cummax())
# """
# #output:
#            name  marks  age
# row 1  santhosh     50   20
# row 2  santhosh     50   40
# row 3  santhosh     50   40
# row 4  santhosh     50   41
# row 5  santhosh     58   41
# """
#
#
#
# print(df[["marks","age"]].cummax(axis = 1))
# """
# #output:
#        marks  age
# row 1     50   50
# row 2     25   40
# row 3     36   36
# row 4     49   49
# row 5     58   58
# """
#
#
#
# print(df[["marks","age"]].cummax(axis = 0))
# """
# #output:
#        marks  age
# row 1     50   20
# row 2     50   40
# row 3     50   40
# row 4     50   41
# row 5     58   41
# """
#
#
#
#
#
# #df.describe()
# print(df.describe())
# """
# #output:
#           marks        age
# count   5.000000   5.000000
# mean   43.600000  32.000000
# std    13.049904   9.246621
# min    25.000000  20.000000
# 25%    36.000000  25.000000
# 50%    49.000000  34.000000
# 75%    50.000000  40.000000
# max    58.000000  41.000000
# """
#
#
#
#
# print(df.describe(include="object"))
# """
# #output:
#             name
# count          5
# unique         3
# top     santhosh
# freq           2
# """
#
#
#
#
# print(df.describe(include="number")) #default as number
# """
# #output:
#            marks        age
# count   5.000000   5.000000
# mean   43.600000  32.000000
# std    13.049904   9.246621
# min    25.000000  20.000000
# 25%    36.000000  25.000000
# 50%    49.000000  34.000000
# 75%    50.000000  40.000000
# max    58.000000  41.000000
# """
#
#
#
#
#
# print(df.describe(include="all"))
# """
# #output:
#             name      marks        age
# count          5   5.000000   5.000000
# unique         3        NaN        NaN
# top     santhosh        NaN        NaN
# freq           2        NaN        NaN
# mean         NaN  43.600000  32.000000
# std          NaN  13.049904   9.246621
# min          NaN  25.000000  20.000000
# 25%          NaN  36.000000  25.000000
# 50%          NaN  49.000000  34.000000
# 75%          NaN  50.000000  40.000000
# max          NaN  58.000000  41.000000
# """
#
#
#
#
# print(df.info())
# """
# #output:
# <class 'pandas.core.frame.DataFrame'>
# Index: 5 entries, row 1 to row 5
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   name    5 non-null      object
#  1   marks   5 non-null      int64
#  2   age     5 non-null      int64
# dtypes: int64(2), object(1)
# memory usage: 160.0+ bytes
# """
#
#
#
#
# #reindexing --> extracting the data by using reindexing
# dt = {"name":["santhosh","naveen","santhosh","mahesh","naveen"],"marks":[50,25,36,49,58,],"age":[20,40,34,41,25]}
# df = pd.DataFrame(data = dt)
# df.index = [f"row {x}" for x in range(1,len(df)+1)]
#
#
# print(df.reindex(index=["row 2","row 3","row 4","row 5"],columns=["name","marks","age"]))
# """
# #output:
#         name  marks  age
# row 2  naveen     25   40
# row 3  santhosh   36   34
# row 4  mahesh     49   41
# row 5  naveen     58   25
# """
#
#
#
# print(df.reindex(index=["row 2","row 3"],columns=["name","marks","age"]))
# """
# #output:
#         name  marks  age
# row 2  naveen     25   40
# row 3  santhosh   36   34
# """
#
#
#
# #date_range
# """
# date_range(start=None, end=None, periods=None, freq=None, tz=None, name = None,
# inclusive = [none(default),"left","right"]) -> 'DatetimeIndex'
# """
#
#
# print(pd.date_range(start="2024-01-01",end="2024-01-10"))
# """
# #output:
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
#                '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
#                '2024-01-09', '2024-01-10'],
#               dtype='datetime64[ns]', freq='D')
#
# """
#
#
#
#
#
# print(pd.date_range(start="2024-01-01",end="2024-01-10",freq="2D"))
# """
# #output:
# DatetimeIndex(['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-07',
#                '2024-01-09'],
#               dtype='datetime64[ns]', freq='2D')
# """
#
#
#
#
#
# print(pd.date_range(start="2024-01-01",end="2024-01-10",periods=5))
# """
# #output:
# DatetimeIndex(['2024-01-01 00:00:00', '2024-01-03 06:00:00',
#                '2024-01-05 12:00:00', '2024-01-07 18:00:00',
#                '2024-01-10 00:00:00'],
#               dtype='datetime64[ns]', freq=None)
# """
#
#
#
#
# print(pd.date_range(start="2024-01-01",periods=5))
# """
# #output:
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
#                '2024-01-05'],
#               dtype='datetime64[ns]', freq='D')
# """
#
#
#
# print(pd.date_range(start="2024-01-01",end="2024-05-10",freq="ME"))
# """
# #output:
# DatetimeIndex(['2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30'], dtype='datetime64[ns]', freq='ME')
# """
#
#
#
# print(pd.date_range(start="2024-01-01",end="2027-05-10",freq="YE"))
# """
# #output:
# DatetimeIndex(['2024-12-31', '2025-12-31', '2026-12-31'], dtype='datetime64[ns]', freq='YE-DEC')
# """
#
#
#
#
# #pd.bdate_range()
# print(pd.bdate_range(start="2024-01-01",end="2024-01-10"))
# """
# #output:
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03',
# '2024-01-04', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'], dtype='datetime64[ns]', freq='B')
# """
#
#
# print(pd.bdate_range(start="2024-01-01",end="2024-01-10",freq="B"))
# """
# #outpot:
# DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
#                '2024-01-05', '2024-01-08', '2024-01-09', '2024-01-10'],
#               dtype='datetime64[ns]', freq='B')
# """
#
#
# #inclusive left means it will include the start date and exclude the end date
# print(pd.date_range(start="2024-01-01",end="2024-05-10",freq="ME",inclusive="left",))
# """
# #output:
# DatetimeIndex(['2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30'], dtype='datetime64[ns]', freq='ME')
# """
#
#
#
#
# #inclusive right means it will include the end date and exclude the start date
# print(pd.date_range(start="2024-01-01",end="2024-05-10",freq="ME",inclusive="right",))
# """
# #output:
# DatetimeIndex(['2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30'], dtype='datetime64[ns]', freq='ME')
# """
#
#
#
#
# print(pd.date_range(start="2024-01-01",end="2024-05-10",freq="ME",inclusive="right",tz="Asia/Kolkata",))
# """
# #output:
# DatetimeIndex(['2024-01-31 00:00:00+05:30', '2024-02-29 00:00:00+05:30',
#                '2024-03-31 00:00:00+05:30', '2024-04-30 00:00:00+05:30'],
#               dtype='datetime64[ns, Asia/Kolkata]', freq='ME')
# """
#
#
# #np.linspace()
# """
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# """
# print(np.linspace(start=1,stop=10,num=5))
# """
# #output:
# [ 1.    3.25  5.5   7.75 10.  ]
# """
#
#
# print(np.linspace(start=1,stop=10,num=5,retstep=True))
# """
# #output:
# (array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ]), np.float64(2.25))
# """
#
#
# print(np.linspace(start=1,stop=10,num=5,retstep=True,endpoint=False))#deafault endpoint is true
# """
# #output:
# (array([1. , 2.8, 4.6, 6.4, 8.2]), np.float64(1.8))
# """
#
#
#
# print(np.linspace(start=1,stop=10,num=5,retstep=True,endpoint=False,dtype=int))
# """
# #output:
# (array([1, 2, 4, 6, 8]), 1)
# """
#
#
#
#
#
# #np.random.choice()
# """
# np.random.choice(a, size=None, replace=True, p=None)
# """
#
# print(np.random.choice(a=[1,2,3,4,5],size=3))
# """
# #output:
# [4 1 5]
# """
#
# print(np.random.choice(a=10,size=20,replace=True))
# """
# #output:
# [0 2 9 7 4 1 0 9 1 7 3 4 3 0 5 7 7 8 0 6]
# """
#
#
#
#
# print(np.random.choice(a=10,size=10,replace=False))#not allow duplicate value
# """
# #output:
# [7 5 6 2 0 3 4 8 9 1]
# """
#
#
# '''
# #this is error because we have only 10 unique value but we are asking for 20 unique value
# print(np.random.choice(a=10,size=20,replace=False))
# """
# #output:
# Traceback (most recent call last):
#   File "D:\data science\pandas_py.py", line 2319, in <module>
#     print(np.random.choice(a=10,size=20,replace=False))
#   File "numpy/random/mtrand.pyx", line 1020, in numpy.random.mtrand.RandomState.choice
# ValueError: Cannot take a larger sample than population when 'replace=False'
# """
# '''
#
#
#
# """
# #np.random.normal()
# normal(loc=0.0(mean), scale=1.0(std), size=None)
# """
#
# print(np.random.normal(loc=20,scale=5,size=20))
# """
# #output:
# [16.3859627  22.73337949 16.45225121 22.59252583 16.21810323 18.5909121
#  21.32180669 19.428193   26.80531604 19.47581099 17.31342691 27.02123385
#  15.2688603  27.57874309 18.74041    24.58988466 23.24377545 21.92940601
#  21.25859915 24.71423048]
# """
#
#
#
#
# print(np.random.normal(loc=20,scale=1,size=5)) #loc = mean , scale = std
# """
# #output:
# [20.31147749 19.87986815 20.53954317 21.72979476 19.14937962]
# """
#
#
#
#
# #pd.reindex_like()
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = pd.DataFrame(np.random.rand(3,3))
#
# print(df2.reindex_like(df1))
# """
# #output:
#           0         1         2
# 0  0.169872  0.473724  0.604926
# 1  0.244977  0.735822  0.219087
# 2  0.258946  0.354788  0.989120
# 3       NaN       NaN       NaN
# 4       NaN       NaN       NaN
# 5       NaN       NaN       NaN
# """
#
#
#
#
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = pd.DataFrame(np.random.rand(3,3))
#
# print(df1.reindex_like(df2))
# """
# #output:
#           0         1         2
# 0  0.066114  0.665288  0.566742
# 1  0.644090  0.869426  0.157592
# 2  0.943383  0.399405  0.117285
# """
#
#
#
# #method = "ffill"
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = pd.DataFrame(np.random.rand(3,3))
#
# print(df2.reindex_like(df1,method="ffill"))
# """
# #output:
#           0         1         2
# 0  0.208854  0.177916  0.373119
# 1  0.687332  0.388487  0.253343
# 2  0.436709  0.445742  0.215437
# 3  0.436709  0.445742  0.215437
# 4  0.436709  0.445742  0.215437
# 5  0.436709  0.445742  0.215437
# """
#
#
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = pd.DataFrame(np.random.rand(3,3))
#
# print(df2.reindex_like(df1,method="ffill",limit=1))
# """
# #output:
#           0         1         2
# 0  0.194318  0.917082  0.800802
# 1  0.975280  0.306201  0.619709
# 2  0.223003  0.437426  0.051665
# 3  0.223003  0.437426  0.051665
# 4       NaN       NaN       NaN
# 5       NaN       NaN       NaN
# """
#
#
#
# #method = "bfill"
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = df1.reindex(columns=[0,1,2],index=[0,2,4])
#
# print(df2.reindex_like(df1,method="bfill"))
# """
# #output:
#           0         1         2
# 0  0.349119  0.500937  0.907477
# 1  0.292003  0.174602  0.581891
# 2  0.292003  0.174602  0.581891
# 3  0.814880  0.551867  0.946080
# 4  0.814880  0.551867  0.946080
# 5       NaN       NaN       NaN
# """
#
#
#
#
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = df1.reindex(columns=[0,1,2],index=[0,4])
#
# print(df2.reindex_like(df1,method="bfill",limit=2))
# """
# #output:
#           0         1         2
# 0  0.325073  0.351274  0.706251
# 1       NaN       NaN       NaN
# 2  0.365672  0.868124  0.092570
# 3  0.365672  0.868124  0.092570
# 4  0.365672  0.868124  0.092570
# 5       NaN       NaN       NaN
# """
#
#
#
#
# #method = "nearest"
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = df1.reindex(columns=[0,1,2],index=[0,4])
#
# print(df2.reindex_like(df1,method="nearest",limit=2))
# """
# #output:
#           0         1         2
# 0  0.268052  0.482816  0.751824
# 1  0.268052  0.482816  0.751824
# 2  0.280461  0.175685  0.297410
# 3  0.280461  0.175685  0.297410
# 4  0.280461  0.175685  0.297410
# 5  0.280461  0.175685  0.297410
# """
#
#
#
#
# df1 = pd.DataFrame(np.random.rand(6,3))
# df2 = df1.reindex(columns=[0,1,2],index=[0,2,3,4,5]) #if the one column is nan means they take "bfill"
#
# print(df2.reindex_like(df1,method="nearest"))
# """
# #output:
#           0         1         2
# 0  0.480335  0.230811  0.070362
# 1  0.222026  0.711838  0.830346
# 2  0.222026  0.711838  0.830346
# 3  0.057101  0.927541  0.931704
# 4  0.222220  0.305875  0.412891
# 5  0.034171  0.047512  0.460949
# """
#
#
#
# #pd.rename()
# df1 = pd.DataFrame(np.random.rand(6,3),columns=list("ABC"))
# print(df1)
# print("="*100)
# print(df1.rename(columns={"A":"AB","B":"CE","C":"FG"},index={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"}))
# """
# #output:
#           A         B         C
# 0  0.074676  0.912899  0.762901
# 1  0.664263  0.070213  0.724781
# 2  0.702920  0.104481  0.839584
# 3  0.684203  0.096566  0.202066
# 4  0.473234  0.910731  0.604382
# 5  0.016449  0.810360  0.362388
# ====================================================================================================
#          AB        CE        FG
# 0  0.074676  0.912899  0.762901
# A  0.664263  0.070213  0.724781
# B  0.702920  0.104481  0.839584
# C  0.684203  0.096566  0.202066
# D  0.473234  0.910731  0.604382
# E  0.016449  0.810360  0.362388
# """
#
#
#
#
# df1 = pd.DataFrame(np.random.rand(6,3),columns=list("ABC"))
# print(df1)
# print("="*100)
# print(df1.rename({"A":"AB","B":"CE","C":"FG"},axis=1))
# print(df1.rename({1:"A",2:"B",3:"C",4:"D",5:"E",6:"F"},axis=0))
# """
# #output:
#           A         B         C
# 0  0.733506  0.134603  0.175905
# 1  0.773853  0.006587  0.952403
# 2  0.410143  0.626551  0.989941
# 3  0.518076  0.559219  0.411425
# 4  0.634776  0.222532  0.460240
# 5  0.497962  0.253881  0.313134
# ====================================================================================================
#          AB        CE        FG
# 0  0.733506  0.134603  0.175905
# 1  0.773853  0.006587  0.952403
# 2  0.410143  0.626551  0.989941
# 3  0.518076  0.559219  0.411425
# 4  0.634776  0.222532  0.460240
# 5  0.497962  0.253881  0.313134
#           A         B         C
# 0  0.733506  0.134603  0.175905
# A  0.773853  0.006587  0.952403
# B  0.410143  0.626551  0.989941
# C  0.518076  0.559219  0.411425
# D  0.634776  0.222532  0.460240
# E  0.497962  0.253881  0.313134
# """
#
#
#
# dt = {"Name":["santhosh","kumar","muthu","mani","murugan","karthi"],"Age":[21,22,24,21,25,20],"marks":[40,56,72,35,54,22]}
# df = pd.DataFrame(data = dt)
# df.index = [x for x in range(1,len(df)+1)]
# print(df)
#
#
#
# for i in df.values:
#     print(i)
#
# """
# #output:
# ['santhosh' 21 40]
# ['kumar' 22 56]
# ['muthu' 24 72]
# ['mani' 21 35]
# ['murugan' 25 54]
# ['karthi' 20 22]
# """
#
#
#
#
# for i in df.keys():
#     print(i)
#
# """
# #output:
# Name
# Age
# marks
# """
#
#
#
#
# for col,val in df.items():
#     print(col,"\n",val)
#     print("==="*30)
#
# """
# #output:
# Name
#  1    santhosh
# 2       kumar
# 3       muthu
# 4        mani
# 5     murugan
# 6      karthi
# Name: Name, dtype: object
# ==========================================================================================
# Age
#  1    21
# 2    22
# 3    24
# 4    21
# 5    25
# 6    20
# Name: Age, dtype: int64
# ==========================================================================================
# marks
#  1    40
# 2    56
# 3    72
# 4    35
# 5    54
# 6    22
# Name: marks, dtype: int64
# ==========================================================================================
# """
#
#
#
#
#
#
#
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"maths":[45,57,66,35,42],"science":[62,45,78,98,66],"chemisty":[89,76,56,89,55]}
# df = pd.DataFrame(data = dt)
#
#
#
# """
# #iterrows
# this iterrows were given as the result by row by row to the dataframe
# """
# for i in df.iterrows():
#     print(i)
# """
# #output:
# (0, name        santhosh
# maths             45
# science           62
# chemisty          89
# Name: 0, dtype: object)
# (1, name        raj
# maths        57
# science      45
# chemisty     76
# Name: 1, dtype: object)
# (2, name        muthu
# maths          66
# science        78
# chemisty       56
# Name: 2, dtype: object)
# (3, name        kumar
# maths          35
# science        98
# chemisty       89
# Name: 3, dtype: object)
# (4, name        mani
# maths         42
# science       66
# chemisty      55
# Name: 4, dtype: object)
# """
#
#
#
# """
# #itertupes
# this itertupes were given as the result by row by row into a tuple in the dataframe
# """
# for i in df.itertuples():
#     print(i)
# """
# #output:
# Pandas(Index=0, name='santhosh', maths=45, science=62, chemisty=89)
# Pandas(Index=1, name='raj', maths=57, science=45, chemisty=76)
# Pandas(Index=2, name='muthu', maths=66, science=78, chemisty=56)
# Pandas(Index=3, name='kumar', maths=35, science=98, chemisty=89)
# Pandas(Index=4, name='mani', maths=42, science=66, chemisty=55)
# """
#
#
#
# #index = False
# for i in df.itertuples(index=False):
#     print(i)
# """
# #output:
# Pandas(name='santhosh', maths=45, science=62, chemisty=89)
# Pandas(name='raj', maths=57, science=45, chemisty=76)
# Pandas(name='muthu', maths=66, science=78, chemisty=56)
# Pandas(name='kumar', maths=35, science=98, chemisty=89)
# Pandas(name='mani', maths=42, science=66, chemisty=55)
# """
#
#
#
#
# for key,value in df.items(): #instead of iteritems()
#     print(key,"\n",value)
# """
# #output:
# name
#  0    santhosh
# 1         raj
# 2       muthu
# 3       kumar
# 4        mani
# Name: name, dtype: object
# maths
#  0    45
# 1    57
# 2    66
# 3    35
# 4    42
# Name: maths, dtype: int64
# science
#  0    62
# 1    45
# 2    78
# 3    98
# 4    66
# Name: science, dtype: int64
# chemisty
#  0    89
# 1    76
# 2    56
# 3    89
# 4    55
# Name: chemisty, dtype: int64
# """
#
#
#
#
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"maths":[45,57,66,35,42],"science":[62,45,78,98,66],"chemisty":[89,76,56,89,55]}
# df = pd.DataFrame(data = dt,index=list("acbba"))
# """
# print(df.sort_values())
#
# #output:
# Traceback (most recent call last):
#   File "D:\data science\pandas_py.py", line 2748, in <module>
#     print(df.sort_values())
# TypeError: DataFrame.sort_values() missing 1 required positional argument: 'by'
# """
#
#
# print(df.sort_values(by=["maths"]))
# """
# #output:
#        name  maths  science  chemisty
# b     kumar     35       98        89
# a      mani     42       66        55
# a  santhosh     45       62        89
# c       raj     57       45        76
# b     muthu     66       78        56
# """
#
#
# print(df.sort_values(by=["name"])) #follow lexograpically to sorted
# """
# #output:
#        name  maths  science  chemisty
# b     kumar     35       98        89
# a      mani     42       66        55
# b     muthu     66       78        56
# c       raj     57       45        76
# a  santhosh     45       62        89
# """
#
#
#
#
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"salary":[200000,120000,55000,100000,45000],"age":[21,21,25,23,20]}
# df = pd.DataFrame(data = dt,index=list("acbba"))
# print(df.sort_values(by=["salary"]))
# """
# #output:
#        name  salary  age
# a      mani   45000   20
# b     muthu   55000   25
# b     kumar  100000   23
# c       raj  120000   21
# a  santhosh  200000   21
# """
#
#
#
# print(df.sort_values(by=["salary","age"],ascending=False))
# """
# #output:
#        name  salary  age
# a  santhosh  200000   21
# c       raj  120000   21
# b     kumar  100000   23
# b     muthu   55000   25
# a      mani   45000   20
# """
#
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"salary":[200000,120000,np.nan,100000,45000],"age":[21,21,25,23,20]}
# df = pd.DataFrame(data = dt,index=list("acbba"))
# print(df.sort_values(by=["salary","age"],ascending=False,na_position="first")) #where NaN will placed (first or last)
# """
# #output:
#        name    salary  age
# b     muthu       NaN   25
# a  santhosh  200000.0   21
# c       raj  120000.0   21
# b     kumar  100000.0   23
# a      mani   45000.0   20
# """
#
#
#
#
# print(df.sort_values(by=["salary","age"],ascending=False,na_position="last",kind="quicksort"))
# """
# #output:
#        name    salary  age
# a  santhosh  200000.0   21
# c       raj  120000.0   21
# b     kumar  100000.0   23
# a      mani   45000.0   20
# b     muthu       NaN   25
# """
#
#
#
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"salary":[200000,120000,np.nan,100000,45000],"age":[21,21,25,23,20]}
# df = pd.DataFrame(data = dt,index=list("acbba"))
#
#
#
# #sort_index()
# print(df.sort_index(axis=0))
# """
# #output:
#        name    salary  age
# a  santhosh  200000.0   21
# a      mani   45000.0   20
# b     muthu       NaN   25
# b     kumar  100000.0   23
# c       raj  120000.0   21
# """
#
#
# print(df.sort_index(axis=1))
# """
# #output:
#    age      name    salary
# a   21  santhosh  200000.0
# c   21       raj  120000.0
# b   25     muthu       NaN
# b   23     kumar  100000.0
# a   20      mani   45000.0
# """
#
#
# print(df.sort_index(axis=0,ascending=False))
# """
# #output:
#        name    salary  age
# c       raj  120000.0   21
# b     muthu       NaN   25
# b     kumar  100000.0   23
# a  santhosh  200000.0   21
# a      mani   45000.0   20
# """
#
#
#
# #get_dummies() --> for ml purpose
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"salary":[200000,120000,np.nan,100000,45000],"age":[21,21,25,23,20]}
# df = pd.DataFrame(data = dt)
# print(pd.get_dummies(df["name"])) #--> dont give like these {df["name"].get_dummies()}
# """
# #output:
#    kumar   mani  muthu    raj  santhosh
# 0  False  False  False  False      True
# 1  False  False  False   True     False
# 2  False  False   True  False     False
# 3   True  False  False  False     False
# 4  False   True  False  False     False
# """
#
#
# #pd.str
# dt = {"name":["santhosh","raj","muthu","kumar","mani"],"salary":[200000,120000,np.nan,100000,45000],"age":[21,21,25,23,20]}
# df = pd.DataFrame(data = dt)
#
#
# print(df["name"].str.contains("muthu"))
# """
# #output:
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# Name: name, dtype: bool
# """
#
#
# print(df["name"].str.contains("suresh"))
# """
# #output:
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# Name: name, dtype: bool
# """
#
#
#
# dt = {"name":["santhosh kumar","raj pandi","muthu","kumar","mani"],"mail":["santhosh@gmail","raj@gmail","muthu@gmail","kumar@gmail","mani@gmail"]}
# df = pd.DataFrame(data = dt)
# print(df["mail"].str.replace("@","#"))
# """
# #output:
# Name: name, dtype: bool
# 0    santhosh#gmail
# 1         raj#gmail
# 2       muthu#gmail
# 3       kumar#gmail
# 4        mani#gmail
# Name: mail, dtype: str
# """
#
#
#
# print(df["mail"].str.replace("@","1"))
# """
# #output:
# 0    santhosh1gmail
# 1         raj1gmail
# 2       muthu1gmail
# 3       kumar1gmail
# 4        mani1gmail
# Name: mail, dtype: str
# """
#
#
#
# #repeat()
# print(df["mail"].str.repeat(2))
# """
# #output:
# 0    santhosh@gmailsanthosh@gmail
# 1              raj@gmailraj@gmail
# 2          muthu@gmailmuthu@gmail
# 3          kumar@gmailkumar@gmail
# 4            mani@gmailmani@gmail
# Name: mail, dtype: str
# """
#
#
#
#
# #startswith
# print(df["mail"].str.startswith("s"))
# """
# #OUTPUT:
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# Name: mail, dtype: bool
# """
#
#
#
#
# print(df["mail"].str.startswith("S")) #this funtion is case_sensitive
# """
# #output:
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# Name: mail, dtype: bool
# """
#
#
#
# #endswith
# print(df["mail"].str.endswith("l")) #this funtion is case_sensitive
# """
# #output:
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# Name: mail, dtype: bool
# """
#
#
# print(df["mail"].str.endswith("L"))
# """
# #output:
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# Name: mail, dtype: bool
# """
#
#
#
# #upper
# print(df["mail"].str.upper())
# """
# #output:
# 0    SANTHOSH@GMAIL
# 1         RAJ@GMAIL
# 2       MUTHU@GMAIL
# 3       KUMAR@GMAIL
# 4        MANI@GMAIL
# Name: mail, dtype: str
# """
#
#
#
#
# #lower
# print(df["mail"].str.lower())
# """
# #output:
# 0    santhosh@gmail
# 1         raj@gmail
# 2       muthu@gmail
# 3       kumar@gmail
# 4        mani@gmail
# Name: mail, dtype: str
# """
#
#
# #capitalize()
# print(df["mail"].str.capitalize())
# """
# #output:
# 0    Santhosh@gmail
# 1         Raj@gmail
# 2       Muthu@gmail
# 3       Kumar@gmail
# 4        Mani@gmail
# Name: mail, dtype: str
# """
#
#
#
#
# #title
# print(df["name"].str.title())
# """
# #output:
# 0    Santhosh Kumar
# 1         Raj Pandi
# 2             Muthu
# 3             Kumar
# 4              Mani
# Name: name, dtype: str
# """
#
#
#
# #contains()
# print(df["name"].str.contains("s"))
# """
# #output:
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# Name: name, dtype: bool
# """
#
#
# dt = {"name":["santhosh     ","     raj","muthu","kumar","mani"],"mail":["santhosh@gmail","raj@gmail","muthu@gmail","kumar@gmail","mani@gmail"]}
# df = pd.DataFrame(data = dt)
# print(df["name"].str.len())
# """
# #output:
# 0    13
# 1     8
# 2     5
# 3     5
# 4     4
# Name: name, dtype: int64
# """
#
# #strip()
# print(df["name"].str.strip().str.len())
# """
# #output:
# 0    8
# 1    3
# 2    5
# 3    5
# 4    4
# Name: name, dtype: int64
# """
#
#
#
#
# print(df["name"].str.strip())
# """
# #output:
# Name: name, dtype: int64
# 0    santhosh
# 1         raj
# 2       muthu
# 3       kumar
# 4        mani
# Name: name, dtype: str
# """
#
#
#
#
# #concate --> use as cat
# print(df["name"].str.strip().str.cat(df["name"].str.strip(),sep="_"))
# """
# #output:
# 0    santhosh_santhosh
# 1              raj_raj
# 2          muthu_muthu
# 3          kumar_kumar
# 4            mani_mani
# Name: name, dtype: str
# """
#
#
#
#
# #indexing --> loc(lebel) , iloc(index)
# dt = {
#     "name": ["  santhosh  ", "raj   ", "muthu", "  kumar", "mani", "selvam  ", "  vijay", "anand"],
#     "city": ["chennai  ", "  madurai", "kovai", "  trichy", "salem", "chennai", "  kovai", "madurai"],
#     "dept": ["IT", "HR", "  Sales", "Marketing", "  IT", "HR", "Sales", "Marketing"],
#     "salary": [50000, 45000, 60000, 55000, 52000, 48000, 65000, 58000],
#     "mail": ["santhosh@gmail", "raj@gmail", "muthu@gmail", "kumar@gmail", "mani@gmail", "selvam@gmail", "vijay@gmail", "anand@gmail"]
# }
# df = pd.DataFrame(dt)
# df.index = list("abcdefgh")
#
# print(df.loc["a":"e","name"])
# """
# #output:
# a      santhosh
# b          raj
# c           muthu
# d           kumar
# e            mani
# Name: name, dtype: str
# """
#
#
# print(df.loc[:,"name":"mail"])
# """
# #output:
#            name       city       dept  salary            mail
# a    santhosh    chennai           IT   50000  santhosh@gmail
# b        raj       madurai         HR   45000       raj@gmail
# c         muthu      kovai      Sales   60000     muthu@gmail
# d         kumar     trichy  Marketing   55000     kumar@gmail
# e          mani      salem         IT   52000      mani@gmail
# f      selvam      chennai         HR   48000    selvam@gmail
# g         vijay      kovai      Sales   65000     vijay@gmail
# h         anand    madurai  Marketing   58000     anand@gmail
# """
#
#
#
# print(df.loc[["a","c","d"],["name","dept","mail"]])
# """
# #output:
#            name       dept            mail
# a    santhosh           IT  santhosh@gmail
# c         muthu      Sales     muthu@gmail
# d         kumar  Marketing     kumar@gmail
# """
#
#
#
#
# print(df.loc[["a","b","d","e"],"name":"dept"])
# """
# #output:
#            name       city       dept
# a    santhosh    chennai           IT
# b        raj       madurai         HR
# d         kumar     trichy  Marketing
# e          mani      salem         IT
# """
#
#
#
#
#
#
# #iloc
# print(df.iloc[1:5,1])
# """
# #output:
# b      madurai
# c        kovai
# d       trichy
# e        salem
# Name: city, dtype: str
# """
#
#
#
# print(df.iloc[:,0:4])
# """
# #output:
#            name       city       dept  salary
# a    santhosh    chennai           IT   50000
# b        raj       madurai         HR   45000
# c         muthu      kovai      Sales   60000
# d         kumar     trichy  Marketing   55000
# e          mani      salem         IT   52000
# f      selvam      chennai         HR   48000
# g         vijay      kovai      Sales   65000
# h         anand    madurai  Marketing   58000
# """
#
#
#
# print(df.iloc[0:5,[0,2,3,4]])
# """
# #output:
#            name       dept  salary            mail
# a    santhosh           IT   50000  santhosh@gmail
# b        raj            HR   45000       raj@gmail
# c         muthu      Sales   60000     muthu@gmail
# d         kumar  Marketing   55000     kumar@gmail
# e          mani         IT   52000      mani@gmail
# """
#
#
#
#
# print(df.iloc[0:5,range(1,5,2)])
# """
# #output:
#         city  salary
# a  chennai     50000
# b    madurai   45000
# c      kovai   60000
# d     trichy   55000
# e      salem   52000
# """
#
#
#
# print(df.iloc[0:5,list(range(1,5,2))])
# """
# #output:
#         city  salary
# a  chennai     50000
# b    madurai   45000
# c      kovai   60000
# d     trichy   55000
# e      salem   52000
# """
#
#
# dt = {
#     "team":["rcb","csk","rr","mi","srh","rcb","rcb","csk","rr","mi"],
#     "score":[2000,1900,3000,4000,2500,3000,4500,5000,3500,2000],
#     "year":[2025,2002,2004,2006,2010,2008,2010,2026,2003,2024],
#     "rank":[2,4,5,6,3,3,2,1,1,2]
# }
#
# df = pd.DataFrame(data=dt)
# a = df.groupby("team")
# print(a)
# #<pandas.api.typing.DataFrameGroupBy object at 0x00000250391ACA70>
#
# for i,j in a:
#     print(i,"\n",j)
# """
# #output:
# csk
#    team  score  year  rank
# 1  csk   1900  2002     4
# 7  csk   5000  2026     1
# mi
#    team  score  year  rank
# 3   mi   4000  2006     6
# 9   mi   2000  2024     2
# rcb
#    team  score  year  rank
# 0  rcb   2000  2025     2
# 5  rcb   3000  2008     3
# 6  rcb   4500  2010     2
# rr
#    team  score  year  rank
# 2   rr   3000  2004     5
# 8   rr   3500  2003     1
# srh
#    team  score  year  rank
# 4  srh   2500  2010     3
# """
#
#
#
#
# a = df.groupby(["rank"])
# for i,j in a:
#     print(i,"\n",j)
# """
# #output:
# (1,)
#    team  score  year  rank
# 7  csk   5000  2026     1
# 8   rr   3500  2003     1
# (2,)
#    team  score  year  rank
# 0  rcb   2000  2025     2
# 6  rcb   4500  2010     2
# 9   mi   2000  2024     2
# (3,)
#    team  score  year  rank
# 4  srh   2500  2010     3
# 5  rcb   3000  2008     3
# (4,)
#    team  score  year  rank
# 1  csk   1900  2002     4
# (5,)
#    team  score  year  rank
# 2   rr   3000  2004     5
# (6,)
#    team  score  year  rank
# 3   mi   4000  2006     6
# """
#
#
#
#
# a = df.groupby("team").groups
# print(a)
# """
# #output:
# {'csk': [1, 7], 'mi': [3, 9], 'rcb': [0, 5, 6], 'rr': [2, 8], 'srh': [4]}
# """
#
#
#
#
# a = df.groupby(["team","rank"])
# for i,j in a:
#     print(i,"\n",j)
# """
# #output:
# ('csk', 1)
#    team  score  year  rank
# 7  csk   5000  2026     1
# ('csk', 4)
#    team  score  year  rank
# 1  csk   1900  2002     4
# ('mi', 2)
#    team  score  year  rank
# 9   mi   2000  2024     2
# ('mi', 6)
#    team  score  year  rank
# 3   mi   4000  2006     6
# ('rcb', 2)
#    team  score  year  rank
# 0  rcb   2000  2025     2
# 6  rcb   4500  2010     2
# ('rcb', 3)
#    team  score  year  rank
# 5  rcb   3000  2008     3
# ('rr', 1)
#    team  score  year  rank
# 8   rr   3500  2003     1
# ('rr', 5)
#    team  score  year  rank
# 2   rr   3000  2004     5
# ('srh', 3)
#    team  score  year  rank
# 4  srh   2500  2010     3
# """
#
#
# a = df.groupby(["team","rank"]).groups
# print(a)
# """
# #output:
# {('csk', 1): RangeIndex(start=7, stop=8, step=1), ('csk', 4): RangeIndex(start=1, stop=2, step=1),
# ('mi', 2): RangeIndex(start=9, stop=10, step=1), ('mi', 6): RangeIndex(start=3, stop=4, step=1),
# ('rcb', 2): RangeIndex(start=0, stop=12, step=6), ('rcb', 3): RangeIndex(start=5, stop=6, step=1),
# ('rr', 1): RangeIndex(start=8, stop=9, step=1), ('rr', 5): RangeIndex(start=2, stop=3, step=1),
# ('srh', 3): RangeIndex(start=4, stop=5, step=1)}
# """
#
#
#
# a = df.groupby(["team"])
# for i,j in a:
#     print(i,"\n",j)
#
#
# print(a["score"].agg(func=sum))
# """
# #output:
# team
# csk    6900
# mi     6000
# rcb    9500
# rr     6500
# srh    2500
# Name: score, dtype: int64
# """
#
#
#
# a = df.groupby(["year"])
#
# print("average by years as each team",a["score"].agg(func=np.mean))
# """
# #output:
# average by years as each team year
# 2002    1900.0
# 2003    3500.0
# 2004    3000.0
# 2006    4000.0
# 2008    3000.0
# 2010    3500.0
# 2024    2000.0
# 2025    2000.0
# 2026    5000.0
# Name: score, dtype: float64
# """
#
#
# #aggregation used by multiple functions in single one
# a = df.groupby(["team"])
# print("average by years as each team\n",a["score"].agg(func=[np.mean,np.sum,np.std]))
# """
# #output:
# average by years as each team
#               mean   sum          std
# team
# csk   3450.000000  6900  1550.000000
# mi    3000.000000  6000  1000.000000
# rcb   3166.666667  9500  1027.402334
# rr    3250.000000  6500   250.000000
# srh   2500.000000  2500     0.000000
# """
#
# print("--"*30)
#
# a = df.groupby(["team"])
# for i,j in a:
#      print(i,"\n",j)
#
# a1 = lambda x: x+10
#
# print(a["score"].transform(func=a1))
# """
# #output:
# 0    2010
# 1    1910
# 2    3010
# 3    4010
# 4    2510
# 5    3010
# 6    4510
# 7    5010
# 8    3510
# 9    2010
# Name: score, dtype: int64
# """
#
#
#
# a1 = lambda x: x+1
#
# print(a["year"].transform(func=a1))
# """
# #output:
# 0    2026
# 1    2003
# 2    2005
# 3    2007
# 4    2011
# 5    2009
# 6    2011
# 7    2027
# 8    2004
# 9    2025
# Name: year, dtype: int64
# """
#
#
#
# #groupby --> using filter
#
# import pandas as pd
#
# dt = {
#     "team":["rcb","csk","rr","mi","srh","rcb","rcb","csk","rr","mi"],
#     "score":[2000,1900,3000,4000,2500,3000,4500,5000,3500,2000],
# }
#
# df = pd.DataFrame(data=dt)
#
# # Filter: Group total score 5000-ku mela irukanum
# # x["score"].sum() inga sum-a calculate pannudhu
# a = df.groupby(["team"])
# for i,j in a:
#     print(i,"\n",j)
#
#
# print(a.filter(lambda x: x["score"].sum() > 5000))
# """
# #ouput:
# ('csk',)
#    team  score
# 1  csk   1900
# 7  csk   5000
# ('mi',)
#    team  score
# 3   mi   4000
# 9   mi   2000
# ('rcb',)
#    team  score
# 0  rcb   2000
# 5  rcb   3000
# 6  rcb   4500
# ('rr',)
#    team  score
# 2   rr   3000
# 8   rr   3500
# ('srh',)
#    team  score
# 4  srh   2500
#   team  score
# 0  rcb   2000
# 1  csk   1900
# 2   rr   3000
# 3   mi   4000
# 5  rcb   3000
# 6  rcb   4500
# 7  csk   5000
# 8   rr   3500
# 9   mi   2000
# """
#
#
#
#
#
# #joins
# df_team = pd.DataFrame({
#     'team_id': [1, 2, 3],
#     'team_name': ['RCB', 'CSK', 'RR']
# })
#
# df_score = pd.DataFrame({
#     'team_id': [1, 2, 4],
#     'total_score': [9500, 6900, 4000]
# })
#
# print("Inner Join:")
# print(pd.merge(left=df_team, right=df_score, on='team_id', how='inner'))
# """
# #output:
#    team_id team_name  total_score
# 0        1       RCB         9500
# 1        2       CSK         6900
# """
#
# print("\nLeft Join:")
# print(pd.merge(left=df_team, right=df_score, on='team_id', how='left'))
# """
# #output:
# Left Join:
#    team_id team_name  total_score
# 0        1       RCB       9500.0
# 1        2       CSK       6900.0
# 2        3        RR          NaN
# """
#
# print("\nRight Join:")
# print(pd.merge(left = df_team, right = df_score, on='team_id', how='right'))
# """
# #output:
# Right Join:
#    team_id team_name  total_score
# 0        1       RCB         9500
# 1        2       CSK         6900
# 2        4       NaN         4000
# """
#
#
# print("\nOuter Join:")
# print(pd.merge(left=df_team,right = df_score, on='team_id', how='outer'))
# """
# #output:
# Outer Join:
#    team_id team_name  total_score
# 0        1       RCB       9500.0
# 1        2       CSK       6900.0
# 2        3        RR          NaN
# 3        4       NaN       4000.0
# """
#
#
#
#
# #concat()
# import pandas as pd
#
# # Table 1
# df1 = pd.DataFrame({
#     'team': ['RCB', 'CSK'],
#     'score': [9500, 6900]
# })
#
# # Table 2
# df2 = pd.DataFrame({
#     'team': ['RR', 'MI'],
#     'score': [6500, 6000]
# })
#
# # Axis=0 (Rows-ah add pannum - Vertically)
# df_axis0 = pd.concat([df1, df2], axis=0)
# print("--- Axis=0 (Vertical Add) ---")
# print(df_axis0)
# """
# #output:
# --- Axis=0 (Vertical Add) ---
#   team  score
# 0  RCB   9500
# 1  CSK   6900
# 0   RR   6500
# 1   MI   6000
# """
#
#
#
# # Axis=1 (Columns-ah add pannum - Horizontally)
# df_axis1 = pd.concat([df1, df2], axis=1)
# print("\n--- Axis=1 (Horizontal Add) ---")
# print(df_axis1)
# """
# #output:
# --- Axis=1 (Horizontal Add) ---
#   team  score team  score
# 0  RCB   9500   RR   6500
# 1  CSK   6900   MI   6000
# """
#
#
# #ignore_index
# # Axis=1 (Columns-ah add pannum - Horizontally)
# df_axis1 = pd.concat([df1, df2],ignore_index=True)#default as False
# print(df_axis1)
# """
# #output:
#   team  score
# 0  RCB   9500
# 1  CSK   6900
# 2   RR   6500
# 3   MI   6000
# """
#
#
#
#
# #time
# 
# #timestamp
# print(pd.Timestamp.now())
# """
# #output:
# 2026-07-14 12:42:08.807289
# """
#
# print(pd.Timestamp(2000))
# """
# #output:
# 1970-01-01 00:00:00.000002
# """
#
#
# print(pd.Timestamp("2027-03-12 09:44:2"))
# """
# #output:
# 2027-03-12 09:44:02
# """
#
#
#
#
# print(pd.Timestamp(year=1999, month=1, day=1,hour=1,minute=1,second=1,microsecond=1))
# """
# #output:
# 1999-01-01 01:01:01.000001
# """
#
#
# #unit convertion
# print(pd.Timestamp(199999,unit = "ns"))
# #1970-01-01 00:00:00.000199999
#
#
# print(pd.Timestamp(19,unit = "s"))
# #1970-01-01 00:00:19
#
#
#
#
#
#
# #date_range()
# print(pd.date_range("11:00", "13:30", freq='20min'))
# print(type(pd.date_range("11:00", "13:30", freq='20min')))
# """
# #output:
# DatetimeIndex(['2026-07-14 11:00:00', '2026-07-14 11:20:00',
#                '2026-07-14 11:40:00', '2026-07-14 12:00:00',
#                '2026-07-14 12:20:00', '2026-07-14 12:40:00',
#                '2026-07-14 13:00:00', '2026-07-14 13:20:00'],
#               dtype='datetime64[us]', freq='20min')
# <class 'pandas.DatetimeIndex'>
#
# """
# print("==================")
# print(pd.date_range("11:00", "13:30", freq='20min').time)
# print(type(pd.date_range("11:00", "13:30", freq='20min').time))
# """
# #output:
# DatetimeIndex(['2026-07-14 11:00:00', '2026-07-14 11:20:00',
#                '2026-07-14 11:40:00', '2026-07-14 12:00:00',
#                '2026-07-14 12:20:00', '2026-07-14 12:40:00',
#                '2026-07-14 13:00:00', '2026-07-14 13:20:00'],
#               dtype='datetime64[us]', freq='20min')
# <class 'pandas.DatetimeIndex'>
# ==================
# [datetime.time(11, 0) datetime.time(11, 20) datetime.time(11, 40)
#  datetime.time(12, 0) datetime.time(12, 20) datetime.time(12, 40)
#  datetime.time(13, 0) datetime.time(13, 20)]
# <class 'numpy.ndarray'>
# """
#
#
#
#
#
#
#
# #to_datetime
# a = pd.to_datetime(pd.Series(data=['Feb 28 2023', '2023-01-03', '2023-11-03', "", None, '2023-5', ""]),format='mixed')
# print(a)
# """
# #output:
# 0   2023-02-28
# 1   2023-01-03
# 2   2023-11-03
# 3          NaT
# 4          NaT
# 5   2023-05-01
# 6          NaT
# dtype: datetime64[us]
# """
#
#
# b = pd.to_datetime("1234")
# print(b)
# #1234-01-01 00:00:00
#
#
#
# b = pd.to_datetime(1234)
# print(b)
# #1970-01-01 00:00:00.000001234
#
#
# #bdate_range()
# a = pd.bdate_range(start='2023 01 01', end='2023 12 31')
# print(a)
# print(type(a))
# print(len(a))
# """
# #output:
# DatetimeIndex(['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
#                '2023-01-06', '2023-01-09', '2023-01-10', '2023-01-11',
#                '2023-01-12', '2023-01-13',
#                ...
#                '2023-12-18', '2023-12-19', '2023-12-20', '2023-12-21',
#                '2023-12-22', '2023-12-25', '2023-12-26', '2023-12-27',
#                '2023-12-28', '2023-12-29'],
#               dtype='datetime64[us]', length=260, freq='B')
# <class 'pandas.DatetimeIndex'>
# 260
# """
#
#
#
#
# #to_timedelta
# a = pd.to_timedelta('2 days 2 hours 15 minutes 30 second')
# print(a)
# #2 days 02:15:30
#
# a = pd.to_timedelta('2 days 2 hours 15 minutes 30 s')
# print(a)
# #2 days 02:15:30
#
# a = pd.to_timedelta('2 days 2 hours 15 minutes 30 sec')
# print(a)
# #2 days 02:15:30
#
# a = pd.to_timedelta('2 days 2 hours 15 min 30 sec')
# print(a)
# #2 days 02:15:30
#
# a = pd.to_timedelta('2 days 2 hr 15 min 30 sec')
# print(a)
# #2 days 02:15:30
#
#
#
#
# a = pd.to_timedelta(' 61 min 60 sec')
# print(a)
# #0 days 01:02:00
#
#
#
# a = pd.to_timedelta(' 61 hr 30 min 60 sec')
# print(a)
# #2 days 13:31:00
#
#
#
#
#
# a = pd.Timedelta(6, unit='h')
# print(a)
# # 0 days 06:00:00
#
# print(type(a))
# # <class 'pandas._libs.tslibs.timedeltas.Timedelta'>
#
# a = pd.to_timedelta('60.5 minutes')
# print(a)
# # 0 days 01:00:30
#
# a = pd.to_timedelta('61.5 minutes')
# print(a)
# # 0 days 01:01:30
#
# a = pd.to_timedelta('61.55 minutes')
# print(a)
# # 0 days 01:01:33
#
# print(type(a))
# # <class 'pandas._libs.tslibs.timedeltas.Timedelta'>
#
#
#
# # by using an examples
# s = pd.Series(pd.date_range(start='2023-1-1', periods=3, freq='D'), name="Vaani")
# print(s)
# # 0   2023-01-01
# # 1   2023-01-02
# # 2   2023-01-03
# # Name: Vaani, dtype: datetime64[ns]
#
# print("================")
#
# td = pd.Series([pd.Timedelta(days=i) for i in range(3)], name="Tamil")
# print(td)
# # 0   0 days
# # 1   1 days
# # 2   2 days
# # Name: Tamil, dtype: timedelta64[ns]
#
# print("================")
#
# df = pd.DataFrame(dict(A=s, B=td))
# print(df)
# #            A      B
# # 0 2023-01-01 0 days
# # 1 2023-01-02 1 days
# # 2 2023-01-03 2 days
#
#
# a = pd.Series([pd.to_timedelta(i) for i in range(3)], name="Ram")
#
# df["C"] = df["A"] + df["B"]
# print(df)
# """
# #output:
#            A      B          C
# 0 2023-01-01 0 days 2023-01-01
# 1 2023-01-02 1 days 2023-01-03
# 2 2023-01-03 2 days 2023-01-05
# """
#
#
#
# df["D"] = a + df["B"]
# print(df)
# """
# #output:
#            A      B          C                         D
# 0 2023-01-01 0 days 2023-01-01           0 days 00:00:00
# 1 2023-01-02 1 days 2023-01-03 1 days 00:00:00.000000001
# 2 2023-01-03 2 days 2023-01-05 2 days 00:00:00.000000002
# """
#
#
#
# a = pd.Series([pd.to_timedelta(i) for i in range(3)], name="Ram")
# td = pd.Series([pd.Timedelta(days=i) for i in range(3)], name="Tamil")
# for i,j in zip(a,td):
#     print(i,"===",j)
# """
# #output:
# 0 days 00:00:00 === 0 days 00:00:00
# 0 days 00:00:00.000000001 === 1 days 00:00:00
# 0 days 00:00:00.000000002 === 2 days 00:00:00
# """
#
#
#
# df["F"] = a - df["B"]
# print(df)
# """
# #output:
#            A      B  ...                         D                           F
# 0 2023-01-01 0 days  ...           0 days 00:00:00             0 days 00:00:00
# 1 2023-01-02 1 days  ... 1 days 00:00:00.000000001 -1 days +00:00:00.000000001
# 2 2023-01-03 2 days  ... 2 days 00:00:00.000000002 -2 days +00:00:00.000000002
# """
#
#
#
# print(pd.concat([s,td],axis=0))
# """
# #output:
# 0    2023-01-01 00:00:00
# 1    2023-01-02 00:00:00
# 2    2023-01-03 00:00:00
# 0        0 days 00:00:00
# 1        1 days 00:00:00
# 2        2 days 00:00:00
# dtype: object
# """
#
#
#
# print(pd.concat([s,td],axis=0,ignore_index=True))
# """
# #output:
# dtype: object
# 0    2023-01-01 00:00:00
# 1    2023-01-02 00:00:00
# 2    2023-01-03 00:00:00
# 3        0 days 00:00:00
# 4        1 days 00:00:00
# 5        2 days 00:00:00
# dtype: object
# """
#
#
#
# print(pd.concat([s,td,df["C"]],axis=1))
# """
# #output:
#        Vaani  Tamil          C
# 0 2023-01-01 0 days 2023-01-01
# 1 2023-01-02 1 days 2023-01-03
# 2 2023-01-03 2 days 2023-01-05
# """