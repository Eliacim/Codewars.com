def get_strings(city):
    result = ""
    for i in city.lower():
        if i not in result and i.isalpha():
            result += i + ":" + "*" * city.lower().count(i) + ","
    return result[:-1]


print(get_strings("Las Vegas"))
