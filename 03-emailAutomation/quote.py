import random

class Quote:
    """
    Randomly generate quote out of a file (called quotes.txt).
    """

    file = "quotes.txt"

    def __str__(self):
        return self.getQuote()
    
    def getQuote(self) -> str:
        with open(self.file) as file:
            quotes = list()
            data = file.readlines()
            for lines in data:
                quotes.append(lines.rstrip())
            quote = random.choice(quotes)
            return quote



def main():
    q = Quote()
    print(q)

if __name__ == "__main__":
    main()