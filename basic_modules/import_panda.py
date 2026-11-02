
# -----------------------------------------------------------------
# Checking what a "library" looks like (just observing, not using yet)
# -----------------------------------------------------------------
# NOTE: You do NOT need to understand this code yet.
# This is only shown so you can SEE what using a library looks like.
# Pandas (a library for data analysis) will be properly taught in upcoming module.

import pandas as pd  # "import" brings in a library so Python can use it

print("Pandas library imported successfully. Version:", pd.__version__)

# Expected Output (version number may differ on your system):
# Pandas library imported successfully. Version: 2.x.x


# -----------------------------------------------------------------
# A first (very early) look at the course dataset
# -----------------------------------------------------------------
# Again - do not worry about understanding this code fully yet.
# This just proves your dataset files are in place and readable.
# We will learn every part of this in upcomin module.

df = pd.read_csv("customers.csv")
print("Number of customers in the dataset:", len(df))
print(df.head(3))

# Expected Output:
# Number of customers in the dataset: 80
# (a table showing the first 3 rows of customer data)


# -----------------------------------------------------------------
# BUSINESS INSIGHT
# -----------------------------------------------------------------
# Even this tiny script demonstrates the core idea of Python for
# Data Analysts: write instructions once, and Python executes them
# exactly the same way every time you run the file. This is the
# foundation of automation, which you will build toward across
# this entire course.
