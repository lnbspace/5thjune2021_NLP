
# welcome to Learn and Build
# www.learnandbuild.in

import numpy as np
import time
import collections
training_file = 'Story1.txt'
def read_data(fname):
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        content = [content[i].split() for i in range(len(content))]
        content = np.array(content)
        content = np.reshape(content, [-1, ])
        return content
training_data = read_data(training_file)
print(training_data)
print("Loaded training data...")
def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
        reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return dictionary, reverse_dictionary
dictionary, reverse_dictionary = build_dataset(training_data)
vocab_size = len(dictionary)
print(vocab_size)
print(dictionary, reverse_dictionary)
