import numpy as np


def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    Rk = np.random.rand(data.shape[0])
    Rk = Rk / np.linalg.norm(Rk)
    for i in range(num_steps):
        w = np.dot(data, Rk)
        Rk = w / np.linalg.norm(w)
        eigenvalue = np.dot(Rk, np.dot(data, Rk))
    return float(eigenvalue), Rk
