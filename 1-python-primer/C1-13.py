'''
function reverseList(data):
    left = 0
    right = length(data) - 1
    while left < right:
        temp = data[left]
        data[left] = data[right]
        data[right] = temp
        left = left + 1
        right = right - 1
    return data
''' 