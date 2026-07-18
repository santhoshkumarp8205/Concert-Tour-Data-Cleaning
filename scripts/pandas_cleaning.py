import pandas as pd

pd.set_option('display.max_rows', None)

pd.set_option('display.width', None)

pd.set_option('display.max_columns', None)

df = pd.read_csv("D:\\learning files\\my_file (1).csv")
print(df.columns)
df.columns = df.columns.str.strip().str.lower().str.replace(r'\s++', '_',regex=True)
print(df.columns)
# print(df)
# print(df.info())

null_percentage = df["peak"].isnull().mean()*100
# null_percentage = df["peak"].isnull().sum()/len(df["peak"])*100
print(null_percentage)


df.drop(columns=["peak","all_time_peak"], inplace=True)


#to clean and make the "actual_gross" as str to int
df["actual_gross"] = df["actual_gross"].replace(r'\[.*?\]|[$,]',"",regex=True).astype(int)


df["adjusted_gross_(in_2022_dollars)"] = df["adjusted_gross_(in_2022_dollars)"].replace(r'\[.*?\]|[$,]',"",regex=True).astype(int)




df["tour_title"] = df["tour_title"].str.encode('ascii', 'ignore').str.decode('ascii')
df["tour_title"] = df["tour_title"].str.replace(r'\[.*?\]|[*+]',"",regex=True).astype(str)


df["year(s)"] = df["year(s)"].astype(str).str.replace(r'[–—]', '-', regex=True).str.split('-').str[0].astype(int)
df.rename(columns={'year(s)':'year'}, inplace=True)


df["shows"].astype(int)

df["average_gross"] = df["average_gross"].replace(r'\[.*?\]|[$,]',"",regex=True).astype(int)

df.rename(columns={'ref.':'reference'}, inplace=True)
df['reference'] = df['reference'].str.replace(r'[\[\]]', '', regex=True)
df['reference'] = df['reference'].replace("d",0).astype(int)

print(df.info())

df.to_csv('cleaned_data.csv', index=False)




