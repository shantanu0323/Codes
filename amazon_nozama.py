def reverse(data):
    return data[::-1]


def get_word(statement):
    if statement[-1] != '$':
        return "$"
    words = statement[:-1].split(' ')
    for word in words:
        checklist = words[words.index(word) + 1:]
        for item in checklist:
            if reverse(item).lower() == word.lower():
                return word
    return "$"


if __name__ == '__main__':
    statement = str(input())
    print(get_word(statement), end='')
