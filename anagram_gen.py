
# Returns an array of all anagrams of a given string

def anagrams_of(string):
    # base case
    if len(string) == 1:
        return [string]

    # Recursive case
    collection = []
    substring_anagrams = anagrams_of(string[1:len(string)])

    for substring_anagram in substring_anagrams:
        for i in range(len(substring_anagram) + 1):
            copy = substring_anagram
            collection.append(copy[:i] + string[0] + copy[i:])

    return collection

# text = "abcd"
# print(anagrams_of(text))
