def get_word_count(filecontents):
    words = filecontents.split()
    num_words = len(words)
    return num_words


def get_character_counts(filecontents):
    chars = {}
    words = filecontents.lower()
    words = words.split()
    for word in words:   
        for char in word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def create_dictionary(chars):
    dicts = []
    for k, v in chars.items():
        dict = {"char": k, "nums": v}
        dicts.append(dict)
    dicts.sort(key=lambda x: x["nums"], reverse=True)
    return dicts
        
