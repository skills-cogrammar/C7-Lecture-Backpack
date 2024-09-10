stop_words = [

    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "if",
    "in",
    "into",
    "is",
    "it",
    "no",
    "not",
    "of",
    "on",
    "or",
    "such",
    "that",
    "the",
    "their",
    "then",
    "there",
    "these",
    "they",
    "this",
    "to",
    "was",
    "will",
    "with",
]

import sqlite3

# Create a function for cleaning input 
def remove_stop_words(sentence):
    sentence = sentence.split()
    new_sentence = []

    for word in sentence:
        if word not in stop_words:
            new_sentence.append(word)

    return " ".join(new_sentence)

def to_lowercase(sentence):
    return sentence.lower()

def write_to_databse(username, message, chat_id):
    with sqlite3.connect("user_data.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO user_data (username, message, chat_id) VALUES (?, ?, ?)", (username, message, chat_id))
        conn.commit()
    

if __name__ == "__main__":
    username = input("Enter username: ")
    chat_id = input("Enter chat id: ")
    new_message = input("Enter a message: ")

    new_message = remove_stop_words(new_message)
    new_message = to_lowercase(new_message)
    write_to_databse(username=username, message=new_message, chat_id=chat_id)