def is_alldistinct(data):
    distincts = set()
    for x in data:
        if x in distincts:
            return False
        distincts.add(x)
    return True # all the numbers are different from each other