import pandas as pd
iris=pd.read_csv(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\iris.csv")
subset=iris[iris['variety']=='Setosa']
print("Subset of the Iris Dataset is :[variety='Setosa']")
print(subset)
aggregate_result=subset.aggregate({'sepal_length':['min','max','mean'],'sepal_width':'mean'})
print("\nAggregate result for the subset")
print(aggregate_result)
