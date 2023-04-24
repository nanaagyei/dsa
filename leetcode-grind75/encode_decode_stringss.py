class Solution:

    def encode(self, strs):
        concat_str = ""
        for s in strs:
            concat_str += str(len(s)) + "#" + s
        return concat_str

    def decode(self, string):
        str_list, i = [], 0

        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            length = int(string[i:j])
            str_list.append(string[j+1: j + 1 + length])
            i = j + 1 + length