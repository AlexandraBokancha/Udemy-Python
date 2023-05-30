import difflib
import json

# create a dict from a json file
with open('data.json', 'r') as f:
    data = json.load(f)


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()].rs
    elif word.upper() in data:
        return data[word.upper()]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead" %difflib.get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[difflib.get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            print("You have entered wrong word")
        else:
            print("You have entered wrong input please enter just y or n: ")

    else:
        print("You have entered wrong word")


word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
