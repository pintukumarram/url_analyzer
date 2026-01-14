import numpy as np

def analyze_matrix():
    matrix = np.random.randint(1, 50, (4, 4))
    array = matrix.reshape(-1)
    sorted_array = np.sort(array)

    return {
        "matrix": matrix.tolist(),
        "sorted_array": sorted_array.tolist()
    }
