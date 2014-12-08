import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it is useful to take a
    look at the data we're hoping to analyze. More specifically,  
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Here I plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. 
    '''
#    AL=turnstile_weather['ENTRIESn_hourly'][turnstile_weather.rain==1]
  #  print AL
    plt.figure()
    turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==0].hist(stacked=True, bins=200, label='No Rain')# your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==1].hist(stacked=True, bins=200,  label='Rain')# your code here to plot a historgram for hourly entries when it is raining

    plt.legend ()
    plt.title('Histogram of ENTRIESn_hourly')
    plt.ylim([0,45000])
    plt.xlim([0,6000])
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')

    return plt
