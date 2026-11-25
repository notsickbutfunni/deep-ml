import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows, cols = new_shape
    new_a = []
    res = []

    for row in a:
        for item in row:
            new_a.append(item)
    
    if len(new_a) != rows * cols:
        return []

    for i in range(0, len(new_a), cols):
        res.append(new_a[i : i + cols])
    
    return res