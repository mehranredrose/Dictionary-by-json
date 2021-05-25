#by mehranredrose
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    
    word = word.lower()
    
    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]
    
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("\t\tDid you mean (\"%s\") instead ?" %get_close_matches(word, data.keys())[0])

        decide = input("\nPress y for yes or n for no : ")
        
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        
        elif decide == "n":
            return("Sorry ,Couldn't find your input word !")
        
        else:
            return("You have entered wrong input!please enter y or n : ")
        
    else:
        print("Sorry ,your input word is not in the Dictionary!")


usercommand = "y"

while usercommand == "y":

    word = input("Search for word : ")

    output = translate(word)
    print('\n')

    if type(output) == list:
        for item in output:
            print('==>',item)
    else:
        print('==>',output)

    print('\n')
    usercommand=input('want to search another word ? enter (y/n) ')