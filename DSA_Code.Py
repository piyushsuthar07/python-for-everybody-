arr = [2,5,3,7,5,8,5,9]
def find_max(arr):
    MAximum = arr[0]

    for num in arr:
        if num > MAximum:
            MAximum = num
    
    return MAximum
    
def Find_min(arr):
    Mimimum =arr[0]

    for num in arr:
        if num < Minimum:
            Mimimum = num
    
    return Minimum