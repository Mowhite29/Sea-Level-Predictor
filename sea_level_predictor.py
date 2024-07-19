import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', delimiter=',')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax = df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter')
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')

    # Create first line of best fit
    df_copy_1 = df.copy()
    line_1 = linregress(df_copy_1['Year'], y=df_copy_1['CSIRO Adjusted Sea Level'])
    for i in range(0, 37, 1):
        df_copy_1.loc[(134 + i),'Year'] = (2014 + i)
    ax = plt.plot(df_copy_1['Year'], (line_1.intercept + line_1.slope * df_copy_1['Year']))

    # Create second line of best fit
    df_copy_2 = df.copy()
    df_copy_2.drop(df_copy_2[df_copy_2.Year < 2000].index, inplace=True)
    line_2 = linregress(df_copy_2['Year'], y=df_copy_2['CSIRO Adjusted Sea Level'])
    for i in range(0, 37, 1):
        df_copy_2.loc[(134 + i),'Year'] = (2014 + i)
    ax = plt.plot(df_copy_2['Year'], (line_2.intercept + line_2.slope * df_copy_2['Year']))


    # Add labels and title
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()