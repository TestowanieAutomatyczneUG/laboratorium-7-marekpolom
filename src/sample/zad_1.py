class IsPangram:
    def pangram(self, word):
        abc = list("abcdefghijklmnopqrstuvwxyz")

        w = list(word.lower())
        temp = list()

        for x in w:
            if x in abc:
                temp += x

        temp = list(set(temp))
        temp.sort()

        if temp == abc:
            return 'To pangram'
        else:
            return 'To nie pangram'