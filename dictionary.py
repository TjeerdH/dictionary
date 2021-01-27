import os
import json
import difflib as dl

data = json.load(open("data.json"))
user_word = input("What word would you like to look up?  ")

def dictionary(word):
	close_matches = dl.get_close_matches(word, data.keys(), cutoff=0.7)
	if word in data:
		print(word)
		print(data[word])
	elif close_matches:
		check = input(f"Did you mean {close_matches[0]}? Enter yes or no. ")
		if check.lower() == "y" or check.lower() == "yes":
			word = close_matches[0]
			print(word)
			print(data[word])
		elif check.lower() == "n" or check.lower() == "no":
			print("The word is not found, please check the spelling")
		else:
			print("The answer is not recognised, please try again!")

	else:
		print("The word is not found, please check the spelling")

dictionary(user_word.lower())
