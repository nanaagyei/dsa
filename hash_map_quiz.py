
# Question 1
def array_intersection(arr1, arr2):
    """
    Returns the intersection of two arrays.
    """
    intersection = []
    hash_map = {}
    for item in arr1:
        hash_map[item] = True
    
    for item in arr2:    
        if item in hash_map:
            intersection.append(item)
    
    return intersection

def array_difference(arr1, arr2):
    """
    Returns the difference of two arrays.
    """
    difference = []
    hash_map = {}
    for item in arr1:
        hash_map[item] = True
    
    for item in arr2:    
        if item not in hash_map:
            difference.append(item)
    
    return difference

def array_union(arr1, arr2):
    """
    Returns the union of two arrays.
    """
    union = []
    hash_map = {}
    for item in arr1:
        hash_map[item] = True
        union.append(item)
    
    for item in arr2:    
        if item not in hash_map:
            union.append(item)
    
    return union

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [0, 2, 4, 6, 8]

# print(array_intersection(arr1, arr2))
# print(array_difference(arr1, arr2))
# print(array_union(arr1, arr2))

# Question 2
def duplicate_string(array):
    """
    Returns the duplicate string in an array.
    """
    hash_map = {}
    for item in array:
        if item in hash_map:
            return item
        else:
            hash_map[item] = True
    return None

array = ["a", "b", "c", "d", "c", "e", "f"]
# print(duplicate_string(array))

# Question 3
def get_missing_letter(string):
    """
    Return a missing letter from a string of words.
    """
    hash_map = {}
    for i in range(len(string)):
        hash_map[string[i]] = True
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        if alphabet[i] not in list(hash_map.keys()):
            return alphabet[i]

# word = "the quick brown box jumps over the lazy dog"
# print(get_missing_letter(word))

# Question 4
def non_duplicate(string):
    """
    Return the first non-duplicated character in a string.
    """

    hash_map = {}

    for letter in string:
        if letter in hash_map:
            hash_map[letter] += 1
        else:
            hash_map[letter] = 1
    
    for letter in string:
        if hash_map[letter] == 1:
            return letter
    # for i in range(len(string)):
    #     if hash_map[string[i]] == 1:
    #         return string[i]

word = "minimum"
print(non_duplicate(word))