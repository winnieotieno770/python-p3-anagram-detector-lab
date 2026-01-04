# your code goes here!

class Anagram():
    def __init__(self, word):
        self.word = word.lower()

    def match(self,list):
        matches = []
        targeted_lowered = sorted(self.word)

        for word in list:
            lowered_word = word.lower()
            if sorted(lowered_word) == targeted_lowered:
                matches.append(lowered_word)
        
            
        return matches
