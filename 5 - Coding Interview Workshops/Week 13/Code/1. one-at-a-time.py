def say_something(sentence: str):
    if (len(sentence.split(" ")) == 1):
        return sentence

	words = sentence.split(" ")
	sentence = words[:-1]
	return sentence + say_something(sentence)