def featureScaling(arr):
    xmin = float(arr[0])
    xmax = float(arr[2])
    xprime = []
    if xmin == xmax:
        xprime = [xmin,arr[1],xmax]
        return xprime    
        
    for x in arr:
        xprime.append((x-xmin)/(xmax-xmin))
        
    return xprime

# tests of your feature scaler--line below is input data


data = [0.0, 200000.0, 1111258.0]
print "Salary ",featureScaling(data)

data = [0.0,1000000.0, 34348384.0]
print "Stocks ",featureScaling(data)