import pandas as pd

# Read the CSV file
mtcars = pd.read_csv(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\mtcars.csv")

# Generate and print a summary
mtcars_summary = mtcars.describe()
print("\nThe mtcars Summary is:\n", mtcars_summary)

# Print dataset information
print("\nThe mtcars Info are:")
mtcars.info()

numeric_mtcars = mtcars.select_dtypes(include=['number']) #select_dtypes(include=['number])
mtcars_quartiles = numeric_mtcars.quantile([0.75, 0.25, 0.5])
print("\nThe Quantiles values are:\n", mtcars_quartiles)
