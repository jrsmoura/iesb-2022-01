import tensorflow as tf
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    print(tf.__version__)
    fashion = tf.keras.datasets.fashion_mnist
    (x_train_full, y_train_full), (x_test, y_test) = fashion.load_data()
    x_valid, x_train = x_train_full[:5000] / 255., x_train_full[5000:] / 255.
    y_valid, y_train = y_train_full[:5000], y_train_full[5000:]
    x_test = x_test / 255.

    model = Sequential([
        tf.keras.layers.Flatten(input_shape=[28, 28]),
        tf.keras.layers.Dense(300, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    print(model.summary())
    print("Compiling")
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])
    print("training")
    history = model.fit(x_train, y_train, epochs=10,
                        validation_data=(x_valid, y_valid))
