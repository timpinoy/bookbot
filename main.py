def main():
    file_path = "books/frankenstein.txt"
    book = open_book(file_path)
    num_words = word_count(book)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")
    print_character_report(book)
    print("--- End report ---")


def open_book(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(book):
    return len(book.split())


def count_per_letter(book):
    letter_dict = {}
    for c in book.lower():
        if c in letter_dict:
            letter_dict[c] += 1
        elif c.isalpha():
            letter_dict[c] = 1

    return letter_dict


def sort_by_key(dict):
    return dict["num"]


def print_character_report(book):
    chars = count_per_letter(book)
    char_list = []
    for c in chars:
        char_list.append({"char": c, "num": chars[c]})
    char_list.sort(key=sort_by_key, reverse=True)
    for c in char_list:
        print(f"The '{c["char"]}' character was found {c["num"]} times")


main()