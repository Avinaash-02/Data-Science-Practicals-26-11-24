#Read csv,Excel,Html
import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\mtcars.csv")
print(df.head)
# df1=pd.read_excel(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\mtcars.csv")
url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
df1=pd.read_html(url)
print(df1.head())
