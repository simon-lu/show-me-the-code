# -*- coding: utf-8
# !/usr/bin/env python


def replace_bad_words():

    user_input = raw_input("please enter:")

    with open('filtered_word.txt', 'r') as filtered_file:
        filtered_word = filtered_file.read()
        filtered_word_list = filtered_word.split('\n')
        filtered_file.close()

    for word in filtered_word_list:
        if word in user_input:
            word_len = len(word)
            index = user_input.find(word)
            user_input = user_input[0: index] + "**" + user_input[index+word_len: len(user_input)]
    print user_input


if __name__ == '__main__':
    while True:
        replace_bad_words()