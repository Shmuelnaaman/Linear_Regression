import numpy as np
import pandas


"""
In this Function I 
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure to maximize R^2) and make predictions.

"""

def normalize_features(array):
   """
   Normalize the features in the data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, 
    and the values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m) 

    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """
    m = len(values)
    cost_history = []
    for n_i in range(num_iterations):
        sum_of_theta = np.dot(features, theta)-values
        theta=   theta-(alpha/(m))*(np.dot(sum_of_theta,features))
        cost=compute_cost(features, values, theta)
        cost_history.append (cost)

    return theta, pandas.Series(cost_history) # leave 
    
    
def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, I predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    for the prediction I was llooking for the parameters that maximize R^2 
    '''
    # Select Features (try different features!)
    features = dataframe[['precipi','Hour','meantempi','meandewpti','rain']] #, 'rain', 'precipi', 'Hour', 'meantempi'
       
    # Add day of the week
    
    dummy_units = pandas.get_dummies(dataframe['DATEn'].apply (lambda x:datetime.strftime(datetime.strptime(x,"%Y-%m-%d"),"%A")), prefix='Dow')
    features = features.join(dummy_units)
    
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    
    # Values
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()
    #print np.corrcoef(values_array,features_array)
    # Set values for alpha, number of iterations.
    alpha = 0.1 # please feel free to change this value
    num_iterations = 75 # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    # plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.
    
    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot



