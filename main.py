from stats import get_num_words, get_char_dict, sort_char_dict
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Ussage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(sys.argv)
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    file_contents = get_book_text(file_path)
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_dict = get_char_dict(file_contents)
    sorted_chars = sort_char_dict(char_dict)
    for c in sorted_chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()