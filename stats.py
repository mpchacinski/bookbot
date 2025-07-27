def count_words(book_str):
    words_count = len(book_str.split())
    return words_count


def count_chars(book_str):
    book_str_lower = book_str.lower()
    char_cnt_dict = {}

    for char in book_str_lower:
        if char not in char_cnt_dict:
            char_cnt_dict[char] = 0
        char_cnt_dict[char] += 1
    
    return char_cnt_dict

def count_chars_sorted(chars_count):
    dict_list = []
    for key in chars_count:
        dict_list.append(
            {
                "letter": key,
                "num": chars_count[key]
            }
        )

    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
