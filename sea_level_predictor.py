# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create first line of best fit
slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years1 = range(1880, 2051)
plt.plot(years1, [slope1 * year + intercept1 for year in years1], label='Fit: All Data')

# Create second line of best fit (from year 2000)
df_recent = df[df['Year'] >= 2000]
slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years2 = range(2000, 2051)
plt.plot(years2, [slope2 * year + intercept2 for year in years2], label='Fit: 2000 Onwards')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Show plot
plt.show()
