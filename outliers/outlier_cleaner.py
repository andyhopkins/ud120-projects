#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    l = len(predictions)

    for i in range(l):
        # Calculate the residuals.
        diff = abs(net_worths[i] - predictions[i])
        cleaned_data.append((ages[i], net_worths[i], diff))

    # Sort the array by the 3rd tuple value
    cleaned_data.sort(key=lambda tup: tup[2])

    # Remove the 10% biggest values based on their residuals.
    cleaned_data = cleaned_data[:int(l*0.9)]

    
    return cleaned_data

