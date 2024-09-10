import spacy 

def determine_general_similarity(new_message, old_messages):
    sum_sim = list(map(get_similarity, new_message, old_messages))
    average_sim = sum(sum_sim) / len(sum_sim)
    return average_sim        

def get_similarity(new_message, old_message):
    nlp = spacy.load('en_core_web_md')
    
    doc1 = nlp(new_message)
    doc2 = nlp(old_message)
    
    similarity = doc1.similarity(doc2)
    return similarity


new_message = "I am a new message"
# 10 old messages 
old_messages = ["I am a old message", "I am also a old message", "I am the oldest message", "I am the second oldest message", "I am the third oldest message", "I am the fourth oldest message", "I am the fifth oldest message", "I am the sixth oldest message", "I am the seventh oldest message", "I am the eight oldest message"]

output = determine_general_similarity(new_message, old_messages)
print(output)