from stats import count_words, count_chars, count_chars_sorted

file_name = "books/frankenstein.txt"

def main():
    frank_text = get_book_text(file_name)
    num_words = count_words(frank_text)
    char_count = count_chars(frank_text) 
    char_count_sorted = count_chars_sorted(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in char_count_sorted:
        if el["letter"].isalpha():
            print(f"{el["letter"]}: {el["num"]}")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

    
main()