def string_letter_count(s):
    result = ""
    for i in sorted(s.lower()):
        if i.isalpha() and i not in result:
            result += str(s.lower().count(i)) + i
    return result


print(string_letter_count("The quick brown fox jumps over the lazy dog."))
