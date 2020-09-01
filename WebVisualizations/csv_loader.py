# from prettytable import PrettyTable
import os
import csv
import pandas as pd
csvpath='C://Users/brook/Documents/BootCamp/GITHUB/Web_Design_Challenge/WebVisualizations/Resources/cities.csv'
df=pd.read_csv(csvpath)
table = df.to_html()
print(table)
