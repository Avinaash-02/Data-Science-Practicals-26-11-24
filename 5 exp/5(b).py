#python Scripts tomake Read of Excel sheets
import xlwings as xw
read= xw.Book(Sample_weather_csv)
v1=read.range("A1,A2").value
v2=read.range("F5")
print("result",v1,v2)
