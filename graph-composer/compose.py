import string
import random
import re
import os

from graph import Graph, Vertex

# Generate a passage from drake lyrics, or text files

def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # remove [text in brackets]
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split()) # Remove lines and indents
        text = text.lower()

        # Don't worry about punction today
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() # split on spaces
    return words

def make_graph(_words):
    g = Graph()

    previous_word = None

    for word in _words:
        # Check if word is in graph, maybe add it
        word_vertex = g.get_vertex(word)

        # If there was a previous word, then add an edge if it does not have one already, 
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # otherwise, increment the weight of the existing edge by 1
        # set our word to the previous word and iterate
        previous_word = word_vertex

    # We need to generate the probability map before composing
    # This is a great place to do it before we return the graph object
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to start

    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main(artist):
    # Step 1: get words from the text
    #text_file_path = 'texts/hp_sorcerer_stone.txt'
    #words = get_words_from_text(text_file_path)

    # For song lyrics
    for song_file in os.listdir(f"songs/{artist}"):
        words = get_words_from_text(f"songs/{artist}/{song_file}")

    # Step 2: make a graph using those words
    g = make_graph(words)

    # Step 3: get the next word for x number of words (defined by user)
    composition = compose(g, words, 111)
    # Step 4: show the user!
    return ' '.join(composition) # don't return list
    
if __name__ == '__main__':
    print(main('drake'))
