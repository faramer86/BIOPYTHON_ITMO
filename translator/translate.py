#!/usr/bin/env python
import sys
import random as rd

def new_dictionary_generation(file):
	dictionary = dict()
	for line in file:
		line = line.replace(': ', ':').strip().split()
		popularity = int(line[0])
		words = line[1:]
		ID = int(str(rd.randrange(0, 10**8)) + str(rd.randrange(0, 10**8)))
		for word in words:
			word = word.split(':')
			language = word[0].upper()
			if language in dictionary:
				dictionary[language][ID] = (word[1], popularity)
			else:
				dictionary[language] = {ID:(word[1], popularity)}
	return dictionary

def translated_phrase(from_language, to_language, phrase):
	whole_phrase = ''
	for word in phrase:
		if word.casefold() in list(map(lambda x : x[0].casefold(), dictionary[from_language].values())):
			ID = list(filter(lambda x: word.casefold() in x, map(lambda x : (x[0], x[1][0].casefold()), dictionary[from_language].items())))[0][0]
			try:
				translation_of_word = dictionary[to_language][ID][0]
			except KeyError:
				print('There is not any %s translations of word "%s" in dictionary' % (to_language, word))
				return
			modified_new_word = ''.join(list(map(lambda a, b: b.lower() if a.islower() else b.upper(), word, translation_of_word))) + str(translation_of_word[len(word):].lower())
			whole_phrase += modified_new_word + ' '
		else:
			print('Source language in dictionary do NOT contain all the words from the phrase.')
			return
	return whole_phrase


def translate_unknown_language(to_language, phrase):
	whole_phrase = ''
	popularity_score = dict()
	for word in phrase:
		for language, values in dictionary.items():
			for value in values.values():
				if word.casefold() == value[0].casefold():
					if language not in popularity_score:
						popularity_score[language] = 0
						popularity_score[language] += value[1]
					else:
						popularity_score[language] += value[1]
	if not popularity_score:
		print('unknown language')
	sorted_popularity_score = sorted(popularity_score.items(), key=lambda x: x[1])
	return sorted_popularity_score[-1][0]  

if __name__ == '__main__':

	with open('dict-Kolosov.tr', 'r') as file:
		dictionary = new_dictionary_generation(file)
	
	if sys.argv[1] == '+':
		popularity = int(sys.argv[2])
		list_with_words = sys.argv[3:]
		languages = [list_with_words[i].upper() for i in range(0,len(list_with_words),2)]
		words = [list_with_words[i] for i in range(1,len(list_with_words),2)]
		ID = int(str(rd.randrange(0, 10**8)) + str(rd.randrange(0, 10**8)))
		for language, word in zip(languages, words):
			if language not in dictionary:
				dictionary[language] = dict()
				dictionary[language][ID] = (word, popularity)
			else:
				dictionary[language][ID] = (word, popularity)

	
	elif sys.argv[1] == '?':
		translated_phrase = translated_phrase(sys.argv[2].upper(), sys.argv[3].upper(), sys.argv[4:])
		if translated_phrase != None:
			print(translated_phrase)

	elif sys.argv[1] == '!':
		from_language = translate_unknown_language(sys.argv[2].upper(), sys.argv[3:])
		final_phrase = translated_phrase(from_language, sys.argv[2].upper(), sys.argv[3:])
		if final_phrase != None:
			print(translated_phrase)
	else:
		print('There is no such <arg_1>. Please, choose: + or ! or ?')
