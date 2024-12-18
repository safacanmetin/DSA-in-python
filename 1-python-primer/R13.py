def minmax(data):
    smallest = largest = data[0]
    
    for value in data: 
        if value>largest:
            largest = value
        if value<smallest:
            smallest = value
        
    return (smallest, largest)
