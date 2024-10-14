import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

def build_lstm_model():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def predict(data):
    model = build_lstm_model()
    prediction = model.predict(data)
    return prediction
