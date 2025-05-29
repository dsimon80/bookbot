def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents 

from stats import word_count
from stats import character_count
from stats import sort_on
from stats import sortdict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath=sys.argv[1]
    file_contents=get_book_text(filepath)
    num_words=word_count(file_contents)
    dictionary=character_count(file_contents)
    dictfinal=sortdict(dictionary)

    # design output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for dict in dictfinal:
        if dict[0].isalpha():
            print(f"{dict[0]}: {dict[1]}")
        else:
            pass
    
main()
