class Solution:
    def isNumber(self, s: str) -> bool:
        def is_valid(word):
            if not word:
                return False
            num=False
            i=0
            if word[i] in ['-','+']:
                i+=1
            while i<len(word):
                if not word[i].isdigit():
                    return False
                else:
                    num=True
                i+=1
            return num

        decimal=False
        number=False
        i=0
        if s[i] in ['-','+']:
            i+=1
        while i<len(s):
            cur_char=s[i]
             
            if cur_char.isalpha():
                if cur_char not in ['e','E']:
                    return False
                else:
                    return number and is_valid(s[i+1:])

            elif cur_char=='.':
                if decimal:
                    return False
                else:
                    decimal=True

            elif cur_char in['-','+']:
                return False

            else:
                number=True
            i+=1
        return number

