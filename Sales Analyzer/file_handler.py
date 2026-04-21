import numpy as np

def load_file(file_path):
    data = np.genfromtxt(
        file_path,
        delimiter = ',',
        dtype = None,
        encoding = "utf-8",
        skip_header = 1
    )
    
    return data