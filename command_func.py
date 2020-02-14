import random

#created a function to return the contents of a random line in a text file
def get_random_line(filename):
    file = open(filename)
    text = file.read()
    lines = text.splitlines()
    count = len(lines) - 1
    random_int = random.randint(0, count)
    random_line = lines[random_int]
    return random_line

#created a separate function to return the amount of lines in the text file.
#Eventually, I'd like to have one funtion that can return both of these but
#I'm not entirely sure how to go about that so right now it stays like this
def get_file_line_count(filename):
    file = open(filename)
    text = file.read()
    lines = text.splitlines()
    count = len(lines) - 1
    return count

#returns a random movie
def getmovie():
    movie = get_random_line("movielist.txt")
    return movie

#returns a random quote
def getquote():
    quote = get_random_line("quotelist.txt")
    return ('```\n❝' + quote + '❞\n```')

#trying to find out how to just use a variable as the description of a command
def quote_help():
    quote_count = get_file_line_count("quotes.txt")
    quote_description = ("Gets a random quote from a list of" + quote_count + "quotes.")
    return quote_description

#future command
def getnba():
    return