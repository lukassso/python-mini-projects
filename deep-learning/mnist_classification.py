import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# Load Fashion MNIST dataset
(X_train_full, y_train_full), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Split training set into training and validation sets
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
X_test = X_test / 255.0

# Class names for better interpretability
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# Display a sample image
plt.imshow(X_train[0], cmap="binary")
plt.title(class_names[y_train[0]])
plt.axis('off')
plt.show()

# Build a simple MLP model using Keras Sequential API
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),       # Flatten 28x28 images to 1D vector
    keras.layers.Dense(300, activation="relu"),       # First hidden layer with 300 neurons
    keras.layers.Dense(100, activation="relu"),       # Second hidden layer with 100 neurons
    keras.layers.Dense(10, activation="softmax")      # Output layer for 10 classes
])

# Print model summary
model.summary()

# Compile the model
model.compile(
    loss="sparse_categorical_crossentropy",           # Suitable for integer labels
    optimizer=keras.optimizers.SGD(learning_rate=1e-3), # Stochastic Gradient Descent
    metrics=["accuracy"]                              # Track accuracy during training
)

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,
    validation_data=(X_valid, y_valid)
)

# Plot learning curves
plt.figure(figsize=(8,5))
pd.DataFrame(history.history).plot()
plt.grid(True)
plt.gca().set_ylim(0,1)
plt.show()

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.3f}")

# Predict classes for new samples
X_new = X_test[:10]
y_proba = model.predict(X_new)
y_pred = np.argmax(y_proba, axis=1)
print("Predicted classes:", y_pred)
print("True classes:     ", y_test[:10])

# Visualize predictions
plt.figure(figsize=(10, 2))
for index, image in enumerate(X_new):
    plt.subplot(1, 10, index + 1)
    plt.imshow(image, cmap="binary")
    plt.title(class_names[y_pred[index]], fontsize=8)
    plt.axis('off')
plt.show()
