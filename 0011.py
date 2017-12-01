# -*- coding: utf-8
# !/usr/bin/env python


def detected_words():

    user_input = raw_input("please enter:")

    with open('filtered_word.txt', 'r') as filtered_file:
        filtered_word = filtered_file.read()
        filtered_word_list = filtered_word.split('\n')
        filtered_file.close()

    # print filtered_word_list
    if user_input in filtered_word_list:
        print "freedom"
    else:
        print "Human Rights"


if __name__ == '__main__':
    while True:
        detected_words()