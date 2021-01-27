import os
import json


data = json.load(open("data.json"))
user_word = input("What word would you like to look up?  ")

def dictionary(word):
	if word in data:
		print(word, data[word])
	else:
		print("The word is not found, please check the spelling")

dictionary(user_word.lower())
