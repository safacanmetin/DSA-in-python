def multodd(data):
    for i in range(len(data)):
        for j in range(i+1 , len(data)):
            if data[i] % 2 == 1 and data[j] % 2 == 1:
                return (data[i], data[j])
    return None
             