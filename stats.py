def get_num_words(file_contents: str) -> int:
    count = len(file_contents.split())
    return count

def get_char_dict(file_contents: str) -> dict:
    char_dict = {}
    for char in file_contents:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    del char_dict[" "]
    return char_dict

def sort_char_dict(char_dict: dict) -> list[dict[str, any]]:
    def sort_func(d):
        return d["num"]
    
    sorted_list = [{ "char": k, "num":char_dict[k] } for k in char_dict]
    sorted_list.sort(key=sort_func, reverse=True)
    return sorted_list