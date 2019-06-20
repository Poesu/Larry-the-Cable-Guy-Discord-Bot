import random

#created a function to return the contents of a random line in a text file
def get_random_line(filename):
    file = open(filename)
    text = file.read()
    lines = text.splitlines()
    count = len(lines)
    count = count - 1
    random_int = random.randint(0, count)
    random_line = lines[random_int]
    return random_line

#returns a random movie
def getmovie():
    movie = get_random_line("movielist.txt")
    return movie

#returns a random quote
def getquote():
    quote = get_random_line("quotelist.txt")
    return quote
