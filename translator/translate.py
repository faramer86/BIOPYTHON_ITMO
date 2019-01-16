#!/usr/bin/env python
import sys
import random as rd


def dict_variables(line):
    try:
        popularity = int(line[0])
    except ValueError:
        print('There ae some problems with file.tr!')
        sys.exit()
    words = line[1:]
    ID = int(str(rd.randrange(0, 10**8)) + str(rd.randrange(0, 10**8)))
    return [popularity, words, ID]


def new_dictionary_generation(file):
    dictionary = dict()
    for line in file:
        line = line.replace(': ', ':').strip().split()
        variables = dict_variables(line)
        for word in variables[1]:
            word = word.split(':')
            language = word[0].upper()
            if language in dictionary:
                dictionary[language][variables[2]] = (word[1], variables[0])
            else:
                dictionary[language] = {variables[2]: (word[1], variables[0])}
    return dictionary


def translate_phrase(dictionary, from_language, to_language, phrase):
    if from_language == [] or to_language == [] or phrase == []:
        print('Input Error! Still not enough arguments!')
        sys.exit()
    whole_phrase = ''
    for word in phrase:
        if word.casefold() in list(map(lambda x: x[0].casefold(), dictionary[from_language].values())):
            extracted_ID = list(filter(lambda x: word.casefold() in x, map(lambda x: (
                x[0], x[1][0].casefold()), dictionary[from_language].items())))[0][0]
            try:
                translation_of_word = dictionary[to_language][extracted_ID][0]
            except KeyError:
                print('There is not any %s language translations of word "%s" in dictionary! Check input or dictionary!' % (
                    to_language, word))
                sys.exit()
            modified_new_word = ''.join(list(map(lambda a, b: b.lower() if a.islower() else b.upper(
            ), word, translation_of_word))) + str(translation_of_word[len(word):].lower())
            whole_phrase += modified_new_word + ' '
        else:
            print(
                'Source language in dictionary do NOT contain all the words from the phrase!')
            sys.exit()
    return whole_phrase


def translate_unknown_language(dictionary, to_language, phrase):
    if to_language == [] or phrase == []:
        print('Input Error! Not enough arguments or they are wrong!')
        sys.exit()
    whole_phrase = ''
    popularity_score = dict()
    for word in phrase:
        for language, IDs in dictionary.items():
            for value in IDs.values():
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
    if popularity > 100:
        print('Too high popularity!')
        sys.exit()
    if len(list_with_words) <= 1:
        print('Wrong input! Do not have enough arguments!')
        sys.exit()
    languages = [list_with_words[i].upper()
                 for i in range(0, len(list_with_words), 2)]
    words = [list_with_words[i] for i in range(1, len(list_with_words), 2)]
    ID = int(str(rd.randrange(0, 10**8)) + str(rd.randrange(0, 10**8)))
    string_for_file = '%s ' % popularity
    return [popularity, list_with_words, languages, words, ID, string_for_file]


if __name__ == '__main__':

    # generate new dictionary from file
    # as keys - languages, as values - other dict
    # inside that dict ID:(word, popularity)
    try:
        with open('dict-Kolosov.tr', 'r') as file:
            dictionary = new_dictionary_generation(file)
    except IndexError:
        print('Some issues with file.tr!')
        sys.exit()
    try:
        if sys.argv[1] == '+':
            if sys.argv[2] == [] or sys.argv[3:] == []:
                print('Input Error! Not enough arguments!')
                sys.exit()
            try:
                var = generate_variables(int(sys.argv[2]), sys.argv[3:])
            except ValueError:
                print('Wrong input!')
                sys.exit()
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

            with open('dict-Kolosov.tr', "r") as file:
                for translation in var[5].split(' ')[1:-1]:
                    translation = translation + ' '
                    if translation in file.read():
                        print(
                            'Some of the translations or all of them have already been added!')
                        sys.exit()

            with open('dict-Kolosov.tr', "a") as file:
                file.writelines(var[5] + '\n')

        elif sys.argv[1] == '?':
            try:
                translated_phrase = translate_phrase(
                    dictionary, sys.argv[2].upper(), sys.argv[3].upper(), sys.argv[4:])
            except IndexError:
                print('Input Error! Not enough arguments or they are wrong!')
                sys.exit()
            if translated_phrase != None:
                print(translated_phrase)
            else:
                print('Error!')

        elif sys.argv[1] == '!':
            # figure out unknown language
            try:
                from_language = translate_unknown_language(
                    dictionary, sys.argv[2].upper(), sys.argv[3:])
            except KeyError:
                print('Input Error! Not enough arguments or they are wrong!')
                sys.exit()
            # translate phrase to other language
            final_phrase = translate_phrase(
                dictionary, from_language, sys.argv[2].upper(), sys.argv[3:])
            if final_phrase != None:
                # first line - unknown language
                # second line - translated phrase
                print(from_language, '\n', final_phrase, sep='')
            else:
                print('Error!')
        else:
            print('There is no such first argument. Please, choose: + or ! or ?')
    except IndexError:
        print('There is no first arguments. Please.. add them!')
