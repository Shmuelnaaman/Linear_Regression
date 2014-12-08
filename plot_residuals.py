import numpy as np
import scipy
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    histogram of the residuals, that is, the difference between the original 
    hourly entry data and the predicted values.
    '''
    
    plt.figure()
    (turnstile_weather['rain'] - predictions).hist()
    
    plt.title('difference between original hourly entry and predicted values')
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Residuals')

    return plt
