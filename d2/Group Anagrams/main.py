class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a map of [frequency : list]
        res = {}
        #iterate over every word
        for s in strs:
            #get frequency of each letter for each word
            count = [0] * 26 # 26 letters in english alphabet
            for char in s:
                #loot at each character and add 1 to frequency at it's index
                #in this case it's ord converting character to its unicode 
                #value and subtracting unicode value of a (which is 0)
                count[ord(char) - ord('a')] += 1 #adding 1 at index of current letter
            #tuple is an immutable list, which can be used as a key in a map
            key = tuple(count)
            #check if it's already in the map and append a word to it
            if key not in res:
                res[key] = []
            res[key].append(s)
        #return only values, not the keys
        return list(res.values())
