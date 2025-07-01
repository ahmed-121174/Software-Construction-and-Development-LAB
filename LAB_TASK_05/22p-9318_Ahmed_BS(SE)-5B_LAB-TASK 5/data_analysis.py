import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Basic Data Analysis
print(df.describe())

# Visualization
sns.barplot(x='Category', y='Values', data=df)
plt.title('Category vs Values')
plt.show()
