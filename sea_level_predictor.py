import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit
    # Regresión lineal con todos los datos
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Creamos el rango de años hasta 2050 (2051 para incluirlo)
    years_all = np.arange(df['Year'].min(), 2051)
    # Calculamos los valores de Y para la línea: y = mx + b
    line_all = res_all.slope * years_all + res_all.intercept
    
    ax.plot(years_all, line_all, color='red')

    # Create second line of best fit
    # Filtramos el DataFrame para tomar solo datos del año 2000 en adelante
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    # Creamos el rango de años desde 2000 hasta 2050
    years_2000 = np.arange(2000, 2051)
    line_2000 = res_2000.slope * years_2000 + res_2000.intercept
    
    ax.plot(years_2000, line_2000, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()