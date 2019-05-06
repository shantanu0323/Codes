def reverse(data):
    return data[::-1]


def get_word(statement):
    words = statement[:-1].split(' ')
    for word in words:
        checklist = words[words.index(word):]
        for item in checklist:
            if reverse(item) == word:
                return word
    return "$"


if __name__ == '__main__':
    statement = "the jaguar who  asked wanted raugaj him my deksa on the floor$"
    print(get_word(statement))
