class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return "".join([
            f"{len(string)}#{string}" for string in strs
        ])

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        result = []
        l,r = 0, 0
        while l < len(str):
            while str[r] != '#':
                r += 1
            numOfChars = int(str[l:r])
            start = r+1
            end = start + numOfChars
            result.append(str[start:end])
            l, r = end, end

        return result
