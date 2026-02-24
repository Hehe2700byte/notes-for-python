import math
from typing import List, Tuple, Union

# Define type alias for readability as suggested in starter code
Vector = List[Union[int, float]]

def sigmoid(z: float) -> float:
    """Computes the sigmoid of an input value z[cite: 236, 287]."""
    return 1 / (1 + math.exp(-z))

def binary_cross_entropy(Y: Vector, Y_pred: Vector) -> float:
    """
    Calculates the binary cross-entropy loss[cite: 257, 288, 292].
    Formula: -1/m * sum(Y*ln(Y_pred) + (1-Y)*ln(1-Y_pred))
    """
    m = len(Y)
    total_loss = 0.0
    for i in range(m):
        # Using math.log for natural logarithm [cite: 293]
        total_loss += Y[i] * math.log(Y_pred[i]) + (1 - Y[i]) * math.log(1 - Y_pred[i])
    return -total_loss / m

def fit(X: List[Vector], Y: Vector, epochs: int, learning_rate: float, tolerance: float) -> Tuple[Vector, float]:
    """
    Trains the logistic regression model using gradient descent[cite: 294, 302].
    """
    m = len(X)
    n = len(X[0])
    
    # Initialize weights to zeros and bias to zero [cite: 303]
    w = [0.0] * n
    b = 0.0
    
    final_epoch = 0
    final_cost = 0.0

    for epoch in range(epochs):
        # 1. Compute predicted probabilities (Y_pred) [cite: 304]
        Y_pred = []
        for i in range(m):
            z = sum(w[j] * X[i][j] for j in range(n)) + b
            Y_pred.append(sigmoid(z))
            
        # 2. Calculate current cost [cite: 306]
        cost = binary_cross_entropy(Y, Y_pred)
        
        # 3. Check for convergence based on tolerance 
        if cost < tolerance:
            final_epoch = epoch
            final_cost = cost
            break
            
        # 4. Update weights and bias via gradient descent [cite: 263, 268, 305]
        # Calculate gradients
        dw = [0.0] * n
        db = 0.0
        for i in range(m):
            error = Y_pred[i] - Y[i]
            for j in range(n):
                dw[j] += error * X[i][j]
            db += error
            
        # Apply updates
        for j in range(n):
            w[j] -= learning_rate * (dw[j] / m)
        b -= learning_rate * (db / m)
        
        final_epoch = epoch
        final_cost = cost

    # Print training status [cite: 308]
    print(f"Training stopped at epoch {final_epoch}, Cost: {final_cost:.5f}")
    return w, b

def predict(X: List[Vector], w: Vector, b: float) -> Vector:
    """
    Predicts class labels (0 or 1) for the given feature vectors[cite: 312, 324].
    """
    predictions = []
    n = len(w)
    for i in range(len(X)):
        # Calculate linear combination z [cite: 323]
        z = sum(w[j] * X[i][j] for j in range(n)) + b
        prob = sigmoid(z)
        # Apply 0.5 threshold [cite: 324]
        predictions.append(1 if prob >= 0.5 else 0)
    return predictions

if __name__ == '__main__':
    # Sample Client Code as provided in the assignment [cite: 326]
    
    # Example dataset 1 [cite: 330]
    X1 = [[1, 2], [2, 3], [3, 3], [5, 6], [8, 9], [1, 1]]
    Y1 = [0, 0, 0, 1, 1, 0]
    
    W1, b1 = fit(X1, Y1, learning_rate=0.01, epochs=5000, tolerance=0.05)
    preds1 = predict(X1, W1, b1)
    print("Weights: [" + ", ".join(f"{w:.5f}" for w in W1) + "]")
    print(f"Bias: {b1:.5f}")
    print("Predictions:", preds1)
    
    # Example dataset 2 [cite: 343]
    X2 = [[1, 2, 1], [8, 7, 9], [5, 1, 2], [2, 4, 3], [9, 9, 7], [1, 1, 0]]
    Y2 = [0, 1, 0, 0, 1, 0]
    
    W2, b2 = fit(X2, Y2, learning_rate=0.01, epochs=3000, tolerance=0.03)
    preds2 = predict(X2, W2, b2)
    print("Weights: [" + ", ".join(f"{w:.5f}" for w in W2) + "]")
    print(f"Bias: {b2:.5f}")
    print("Predictions:", preds2)