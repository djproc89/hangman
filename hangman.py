
import time
import random

hangman_picture = ["\n\n\n\n", "\n\n\n\n|", "\n\n\n|\n|", "\n\n|\n|\n|", "\n|/\n|\n|\n|", "_____\n|/\n|\n|\n|", "_____\n|/  |\n|\n|\n|",\
    "_____\n|/  |\n|   o\n|\n|", "_____\n|/  |\n|   o\n|   |\n|", "_____\n|/  |\n|   o\n|  /|\n|", "_____\n|/  |\n|   o\n|  /|\\\n|",\
    "_____\n|/  |\n|   o\n|  /|\\\n|  /", "_____\n|/  |\n|   o\n|  /|\\\n|  / \\", "_____\n|/  |\n|   o\n|  /|\\\n|  /`\\"]

keywords = [
    ("Chess Grandmaster", "Anatoly Karpov"),\
    ("Chess Grandmaster", "Mikhail Tal"),\
    ("President", "Aleksander Kwaśniewski")
    ("Tennis player", "Iga Świątek"),\
    ("Proverb", "Garbage in, garbage out"),\
    ("Proverb", "haste makes waste"),\
    ("Proverb", "The enemy of my enemy is my friend"),\
    ("Proverb", "Ignorance is bliss"),\
    ("Proverb", "It ain't over till the fat lady sings"),\
    ("Proverb", "With great power comes great responsibility"),\
    ("Proverb", "On the Internet, nobody knows you're a dog"),\
    ("Proverb", "Those who live in glass houses should not throw stones"),\
    ("Proverb", "Your mileage may vary"),\
    ]

class Game:
    
    tries = len(hangman_picture)
    tried = []
    failed = 0
    subject = ""
    keyword = ""
    masked = ""
    score = 0
    
    def __init__(self, keyword) -> None:
        self.subject, self.keyword = keyword
        
    def draw(self):
        print("\033c")
        print(hangman_picture[self.failed])
        print("Keyword: {}".format(self.masked))
        print("Subject: {}".format(self.subject))
        print("You've tried: {}".format(self.tried))
        print("Your score: {}".format(self.score))

    def guess(self, letter):
        if not letter in self.tried:
            self.tried.append(letter)
            self.tried.sort()
            if letter in self.keyword.lower():
                self.score += 1
            else:
                self.failed += 1
        self.gen_masked()
    
    def gen_masked(self):
        masked = str()
        for i in self.keyword:
            if i.lower() in self.tried:
                masked += str(i)
            elif i == " ":
                masked += " "
            else:
                masked += "_"
        self.masked = masked
    
    def checkwin(self):
        if(self.masked == self.keyword):
            print("\033c")
            print("Keyword was: {}".format(self.keyword))
            print("You won, your score is: {}".format(self.score))
            return False
        if self.failed >= self.tries:
            print("\033c")
            print("Keyword was: {}".format(self.keyword))
            print("You've lost!")
            return False
        return True
    
    def loop(self):
        self.gen_masked()
        while self.checkwin():
            self.draw()
            self.guess(str(input("Guess a letter: "))[0].lower())   
        

game = Game(keywords[random.randint(0,len(keywords)-1)])
game.loop()