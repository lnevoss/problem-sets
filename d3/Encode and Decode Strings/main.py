class Solution:

    def encode(self, strs: List[str]) -> str:

        return_str = []

        for x in strs:
            if len(x) > 0:
                temp = []
                for y in x:
                    temp.append(str(ord(y) << 1))
    
                temp = '|'.join(temp)
                return_str.append(temp)
            else:
                return_str.append('-1')

        return '/'.join(return_str)

    def decode(self, s: str) -> List[str]:

        if len(s) < 1:
            return []

        return_arr = []

        words = s.split('/')
        for word in words:
            characters = word.split('|')
            decoded_string = ''

            for char in characters:
                if int(char) == -1:
                    break
                decoded_string += chr(int(char) >> 1)

            return_arr.append(decoded_string)

        return return_arr


# better, compact solution
# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         return ''.join(f"{len(s)}#{s}" for s in strs)

#     def decode(self, s: str) -> List[str]:
#         res, i = [], 0
#         while i < len(s):
#             j = s.index('#', i)          # end of the length prefix
#             length = int(s[i:j])
#             res.append(s[j + 1 : j + 1 + length])
#             i = j + 1 + length
#         return res
