import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import survshap
from survshap import SurvivalModelExplainer, PredictSurvSHAP, ModelSurvSHAP
import random
    
def time_processing(df):
    time_columns = []
    for col in df.columns:
        new_col = col.replace('t = ', '').replace('.0', '')
        time_columns.append(new_col)
    
    df.columns = time_columns
    return df


def shap_lines_plot(df, var):
    #Preprocess
    df = time_processing(df)
    df = df[df.variable_str.str.contains(var)]
    df = df.drop(['variable_str', 'variable_name', 'B', 'aggregated_change', 'index'], axis = 1)
    df = df.groupby(["variable_value"]).mean().reset_index()
    
    #Plot
    fig, ax = plt.subplots(figsize=(15, 8))
    for name, group in df.groupby('variable_value'):
        
        #Define colors for color bar
        color_norm = mcolors.Normalize(vmin=df['variable_value'].min(), vmax=df['variable_value'].max())
        blue = (0.15, 0.32, 0.5)
        yellow = (0.98, 0.82, 0.21)
        red = (0.7, 0.14, 0.14)
        color_map = plt.cm.ScalarMappable(norm=color_norm, cmap=mcolors.LinearSegmentedColormap.from_list("", [blue, yellow, red]))
    
        x = df.columns[1:] #Retreive all time based columns 
        y = group[x].values.tolist()[0]
        c = group['variable_value'].iloc[0]
        ax.plot(x, y, color=color_map.to_rgba(c), label=c)
        
    #Configure plot    
    ax.set_title('SHAP Lines - ' + var)
    ax.set_xlabel('Days')
    ax.set_xticks(x[::10])
    ax.set_ylabel('SHAP Value')
    cbar = fig.colorbar(color_map, ax=ax, shrink = 0.5)
    cbar.set_label(var)

