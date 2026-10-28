import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.array(values,dtype=float)
    if width <= 0 or arr.size == 0 or arr.size % width != 0:
        return []
    return np.round(arr.reshape(-1, width), 6).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0:
        return []
    return np.round(arr[np.ix_(rows,columns)],6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0:
        return []
    return np.round(arr.mean(axis=0),6).tolist()



def column_range(matrix: list[list[float]], column: int) -> float:
    arr = np.asarray(matrix,dtype=float)
    if arr.size == 0:
        return 0.0
    col = arr[:, column]
    return float(np.round(col.max()-col.min(),6))

