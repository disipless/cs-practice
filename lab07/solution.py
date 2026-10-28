import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.array(values,dtype=float)
    if width <= 0 or arr.size == 0 or arr.size % width != 0:
        return []
    return np.round(arr.reshape(width,-1)).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0:
        return []
    return np.round(arr[np.ix_(rows,columns)],6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:



def column_range(matrix: list[list[float]], column: int) -> float: