
import datetime
import random
import time

def read_words(file):
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]

def add_log(file, word, guess):
    with open(file, "a") as f:
        f.write(f"{word == guess},{word},{guess},{datetime.datetime.now()}\n")

def main():
    words = read_words("words.txt")
    while True:
        word = words[random.randrange(0, len(words))]
        while True:
            for i in range(5, 1, -1):
                print(f"Word is: {word} (waiting {i} secs)", end = "\r")
                time.sleep(1)
            print("Word is now hidden                                        ")
            guess = input("Retype the word: ")
            add_log("log.txt", word, guess)
            if guess == word:
                print("Well done :)")
                break
            print("WRONG! Try again")

main()
