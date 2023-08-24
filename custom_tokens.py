class Tokenizer:
    def __init__(self, word):
        self.word = word
        self.tokens = []

    def tokenize(self):
        token = []
        print(self.word)
        for i in range(len(self.word)+1):
            if i==len(self.word):
                letter=self.word[len(self.word)-1]
            else:
                letter = self.word[i]

            if letter==' ' or i==len(self.word):
                self.tokens.append(''.join(token));
                token = []
                continue

            token.append(letter)

    def getTokens(self):
        return self.tokens

tokenizer = Tokenizer('This is a tokenizer\'s capability test')
tokenizer.tokenize()

tok = tokenizer.getTokens()

print(tok)