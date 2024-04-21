import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import cv2

# Define neural network architecture (CNN)
def create_model(input_shape, num_classes):
    model = tf.keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes)
    ])
    return model

# Define environment
class ImageEnvironment:
    def __init__(self, dataset):
        self.dataset = dataset
        self.num_samples = len(dataset)
        self.current_index = 0

    def reset(self):
        self.current_index = 0

    def step(self, action):
        image, true_label = self.dataset[self.current_index]
        reward = 1 if action == true_label else -1
        self.current_index = (self.current_index + 1) % self.num_samples
        return image, reward

def train_model(model, environment, optimizer, num_episodes):
    for episode in range(num_episodes):
        state, _ = environment.step(np.random.randint(0, num_classes))  # Initial state (random action)
        state = np.expand_dims(state, axis=0)  # Add batch dimension
        with tf.GradientTape() as tape:
            q_values = model(state, training=True)
            action = tf.argmax(q_values, axis=1)[0].numpy()
            _, reward = environment.step(action)
            target = reward + tf.reduce_max(q_values)
            loss = tf.square(target - q_values[0, action])
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
        print(f"Episode: {episode+1}, Loss: {loss.numpy()}, Reward: {reward}")
    model.save("save\model.keras")
    

# Example dataset (replace with your dataset)
def load_image(filepath):
    # Load image using OpenCV
    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    # Resize image to 28x28
    image = cv2.resize(image, (28, 28))
    # Normalize pixel values
    image = image / 255.0
    return image


file_path = "C:\Ruchira\Academic\.IMMEDIATE\FYP\FYP\Datasets\Personalized\Image\Original"
labels = ['Happy', 'Sad', 'Fear', 'Angry', 'Neutral']
dataset = []

for index, label in enumerate(labels):
    for filename in os.listdir(os.path.join(file_path,label)):
        image_path = os.path.join(file_path,label,filename)
        print(image_path)
        dataset.append((load_image(image_path),index))


# Define parameters
input_shape = (28, 28, 1)
num_classes = 5
num_episodes = len(dataset)
learning_rate = 0.001

# Create environment and model
environment = ImageEnvironment(dataset)
model = create_model(input_shape, num_classes)
optimizer = tf.keras.optimizers.Adam(learning_rate)

# Train model
train_model(model, environment, optimizer, num_episodes)
