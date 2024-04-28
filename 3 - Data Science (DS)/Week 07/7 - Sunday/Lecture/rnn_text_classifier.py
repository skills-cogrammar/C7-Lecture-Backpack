import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, SimpleRNN, Dense

# Sample dataset
comments = [
    "This product is amazing!",
    "I'm really disappointed with the service.",
    "The movie was great, I enjoyed it.",
    "The food was terrible, wouldn't recommend.",
    "I had a fantastic experience at the hotel."
]
labels = [1, 0, 1, 0, 1]  # 1: Positive, 0: Negative

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(comments)
sequences = tokenizer.texts_to_sequences(comments)

# Pad sequences to a fixed length
max_length = 10
padded_sequences = pad_sequences(sequences, maxlen=max_length)

# Define the RNN model
model = Sequential()
model.add(Embedding(1000, 32, input_length=max_length))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(padded_sequences, labels, epochs=10, batch_size=32)

# Example prediction
import numpy as np

new_comment = input("Enter a comment: ")
new_sequence = tokenizer.texts_to_sequences([new_comment])
if not all(len(seq) == 0 for seq in new_sequence):
    new_padded_sequence = pad_sequences(new_sequence, maxlen=max_length)
    new_padded_sequence = np.reshape(new_padded_sequence, (1, -1))  # ensure it's a 2D array
    prediction = model.predict(new_padded_sequence)
    if prediction >= 0.5:
        print("Positive comment")
    else:
        print("Negative comment")
else:
    print("Comment contains no known words")