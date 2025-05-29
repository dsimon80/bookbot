def word_count(text):
    number_of_words = len(text.split())
    return number_of_words

def character_count(text):
    # start with an empty dict
    dictionary = {}
    #split text into a list of characters
    characters = list(text.lower())
    # iterate across the list of characters
    for char in characters:
        if char in dictionary.keys():
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def sort_on(dictionary):
    return dictionary[1]

def sortdict(dictionary):
    listdict=list(dictionary.items())
    listdict.sort(reverse=True, key=sort_on)
    return listdict
