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
                dictionary[language] = {ID: (word[1], popularity)}
    return dictionary


def translate_phrase(dictionary, from_language, to_language, phrase):
    whole_phrase = ''
    for word in phrase:
        if word.casefold() in list(map(lambda x: x[0].casefold(), dictionary[from_language].values())):
            extracted_ID = list(filter(lambda x: word.casefold() in x, map(lambda x: (
                x[0], x[1][0].casefold()), dictionary[from_language].items())))[0][0]
            try:
                translation_of_word = dictionary[to_language][extracted_ID][0]
            except KeyError:
                print('There is not any %s translations of word "%s" in dictionary' % (
                    to_language, word))
                return
            modified_new_word = ''.join(list(map(lambda a, b: b.lower() if a.islower() else b.upper(
            ), word, translation_of_word))) + str(translation_of_word[len(word):].lower())
            whole_phrase += modified_new_word + ' '
        else:
            print(
                'Source language in dictionary do NOT contain all the words from the phrase.')
            return
    return whole_phrase


def translate_unknown_language(dictionary, to_language, phrase):
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
    sorted_popularity_score = sorted(
        popularity_score.items(), key=lambda x: x[1])
    return sorted_popularity_score[-1][0]


def generate_variables(popularity, list_with_words):
    languages = [list_with_words[i].upper()
                 for i in range(0, len(list_with_words), 2)]
    words = [list_with_words[i] for i in range(1, len(list_with_words), 2)]
    ID = int(str(rd.randrange(0, 10**8)) + str(rd.randrange(0, 10**8)))
    string_for_file = '%s ' % popularity
    return popularity, list_with_words, languages, words, ID, string_for_file


if __name__ == '__main__':

	# generate new dictionary from file
	# as keys - languages, as values - other dict
	# inside that dict ID:(word, popularity)
    with open('dict-Kolosov.tr', 'r') as file:
        dictionary = new_dictionary_generation(file)

    if sys.argv[1] == '+':
        var = generate_variables(int(sys.argv[2]), sys.argv[3:])
        # Add new words to dict using languages as keys
        # With each meaning of word store popularity
        for language, word in zip(var[2], var[3]):
            var[5] += language.title() + ':' + word + ' '
            if language not in dictionary:
                dictionary[language] = dict()
                dictionary[language][var[4]] = (word, var[0])
            else:
                dictionary[language][var[4]] = (word, var[0])
        # Add new line to file
        with open('dict-Kolosov.tr', 'a') as file:
            file.writelines(var[5] + '\n')

    elif sys.argv[1] == '?':
        translated_phrase = translate_phrase(
            dictionary, sys.argv[2].upper(), sys.argv[3].upper(), sys.argv[4:])
        if translated_phrase != None:
            print(translated_phrase)

    elif sys.argv[1] == '!':
    	# figure out unknown language
        from_language = translate_unknown_language(
            dictionary, sys.argv[2].upper(), sys.argv[3:])
        # translate phrase to other language
        final_phrase = translate_phrase(
            dictionary, from_language, sys.argv[2].upper(), sys.argv[3:])
        if final_phrase != None:
        	# first line - unknown language
        	# second line - translated phrase
            print(from_language, '\n', final_phrase, sep ='')
    else:
        print('There is no such <arg_1>. Please, choose: + or ! or ?')
