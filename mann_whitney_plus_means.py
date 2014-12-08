import numpy as np
import scipy
import scipy.stats


def mann_whitney_plus_means(turnstile_weather):
    '''
    This function get as input the turnstile_weather dataframe. 
    
    Here I take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function returns:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    Here I use the Mann-Whitney implementation from scipy's.
    
    '''
    without_rain_mean=np.mean(turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==0])
    with_rain_mean=np.mean(turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==1])

    (U,p)=scipy.stats.mannwhitneyu((turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==0]), (turnstile_weather['ENTRIESn_hourly'] [turnstile_weather.rain==1]), use_continuity=True)
      ### YOUR CODE HERE ###
    
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader
