#Mean-Variance-Standard Deviation Calculator
#Code Author: Nelson Orellana

#imort required libraries
import numpy as np

#Calculate(lon): produces the mean, variance, standard deviation, max, min,
#   and sum of the rows, columns, and elements in a 3 x 3 matrix
#Calculate(): List of Num -> Dictionary of 6 string:(List of Num) pairs
#Requires: Length of lon must be exactly 9
def calculate(lon):

    #Variables for matrix dimensions
    matrix_rows = 3
    matrix_cols = 3
    
    #First check to see if the input requirement is met
    error = ValueError('List must contain nine numbers.')
    if len(lon) != (matrix_rows*matrix_cols):
        raise error
    
    
    #numpy array used to create and empty 3x3 matrix
    matrix = np.empty((matrix_rows,matrix_cols))
    #Create the matrix from the list
    #divide the list up into row numbers
    for current_row in range(matrix_rows):
        #likewise for columns
        for current_col in range(matrix_cols):
            #we obtain the position from the list of numbers (lon) by
            #multiplying the current row by the matrix row dimension, to get a starting point in the
            #list, and then adding the column to get the second entry, much like
            #memory address
            matrix[current_row,current_col] = lon[(current_row*matrix_rows) + current_col]

    #create the output dictionary
    stats = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    #function dictionary, to reduce the amoount of variables created while perfroming each function
    function_dict = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    #since the keys in both dictionaries are the same, we can iterate through a
    #list of the keys, pulling the function from the function dicitonary while
    #we then assign the answer to the answer dictionary with the same key.
    keylist = dict.keys(function_dict)
    for current_stat in keylist:
        #col
        #call the function from function_dict and save the answer to a variable
        col_stats = function_dict[current_stat](matrix, 0)
        #rows
        row_stats = function_dict[current_stat](matrix,1)
        #flat
        flat_stats = function_dict[current_stat](matrix)
        #assign stats variables to the answer dictionary
        stats[current_stat] = [col_stats.tolist(),row_stats.tolist(),flat_stats]
    
    return(stats)      

