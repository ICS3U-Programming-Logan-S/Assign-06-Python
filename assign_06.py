#!/usr/bin/env python3

# Created by: Logan
# Created on: Feb. 1, 2022
# This program asks a user for whether or not they want to translate a
# sentence or a sequence of words to pig latin, or if they want to type
# a list of either ints, floats, or strings and locate the character they
# inputted in the list.

# Importing modules
import datetime
import time
from sys import stdout


# This function is called at the end of the program to
# ask the user if they want to run it again
def ask_again():

    # User input
    print()
    user_answer = input("Would you like to run the program again?\n> ")

    # Answer statement to respond to yes or no
    if user_answer == "yes" or user_answer == "y" or user_answer == "Yes":
        type_of_list()
    elif user_answer == "no" or user_answer == "n" or user_answer == "No":
        print()

        thank_you_message = "Thank you for playing!"

        for letter in thank_you_message:
            time.sleep(0.06)  # In seconds
            stdout.write(letter)
            stdout.flush()
    else:
        print()
        print("Error. Try again?")
        print()
        ask_again()


def pig_latin_variable():

    # This function is ran instead of the normal translation function
    # so the function can be printed one letter at a time
    pig_latin2 = (f"Your entered string translated"
                  f" is: {pig_latin_translation().capitalize()}")
    for letter in pig_latin2:
        time.sleep(0.06)  # In seconds
        stdout.write(letter)
        stdout.flush()


def pig_latin_translation():

    # This function takes the user input and splits it so the rest
    # of the function can rearrange the word to translate it into pig latin

    # Making the list for start combinations
    lst1 = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr',
            'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

    # Sentence input and Error checking to make sure the input is a string
    sentence1 = input("Type what you would like translated: ")
    try:
        sentence_int_error = int(sentence1)
        sentence_float_error = float(sentence1)
    except Exception:
        pass
    else:
        print()
        print("Input should be in words, not numbers!\n")
        pig_latin_variable()

    # Changes the user input to a list by "splitting" the characters
    sentence1 = sentence1.split()

    for k in range(len(sentence1)):
        i = sentence1[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            sentence1[k] = i + 'way'
        elif return_str_pig_latin(i) in lst1:
            sentence1[k] = i[2:] + i[:2] + 'ay'
        elif i.isalpha() is False:
            print("Invalid. There should be no numbers!")
            pig_latin_variable()
        else:
            sentence1[k] = i[1:] + i[0] + 'ay'

    return ' '.join(sentence1)


def return_str_pig_latin(str):

    # Returning the strings from the list back
    # to the original pig latin function
    return (str[0] + str[1])


def list_position_str():

    # Create an empty list and input for amount of indexes
    index_list3 = []
    amount_3 = input("Please enter the amount of strings: ")
    # Error checking
    try:
        amount_3_int = int(amount_3)
    except Exception:
        print("Invalid input. Try again!")
        list_position_str()

    # Looping input and appending to the list
    for i in range(1, amount_3_int + 1):
        value_3 = input("Please enter string %d: " % i)

        # Error checking
        try:
            value_3_error1 = int(value_3)
            value_3_error2 = float(value_3)
        except Exception:
            # This is a different version of try catch to make sure
            # that the input is in letters, and not ints or floats
            # (not sure if this counts as extra functionality.)
            pass
        else:
            print("Input should be strings. If you want to put numbers,"
                  " go for integers or floats!\n")
            list_position_str()
        index_list3.append(value_3)

    item_3 = input("Please enter the character(s) "
                   "you want to find(Case Sensitive!)\n> ")

    # Error checking
    try:
        item_3_error1 = int(item_3)
        iem_3_error2 = float(item_3)
    except Exception:
        pass
    else:
        print("Input should be strings. If you want to put numbers,"
              " go for integers or floats!\n")
        list_position_str()

    try:
        print("The position of your string = ", index_list3.index(item_3))
        ask_again()
    except ValueError:
        print("The position of your string = -1 (Doesn't exist in the list)")
        ask_again()


def list_position_float():

    # Create an empty list and input for amount of indexes
    index_list2 = []
    amount_2 = input("Please enter the amount of floats: ")

    # Error checking
    try:
        amount_2_int = int(amount_2)
    except Exception:
        print("Invalid input. That should be an integer!")
        list_position_float()

    # Looping input and appending to the list
    for i in range(1, amount_2_int + 1):
        value_2 = input("Please enter the Value of float %d: " % i)

        # Error checking
        try:
            value_2_int = int(value_2)
            value_2_str = str(value_2)
        except Exception:
            pass
        else:
            print("\nInvalid input. This should be a decimal!\n")
            list_position_float()
        index_list2.append(value_2)

    item_2 = input("Please enter the decimal number that you want to Find: ")

    # Error checking
    try:
        item_2_float = float(item_2)
    except Exception:
        print("Invalid input. Try again!")
        list_position_float()

    try:
        print("\nThe position of your number =", index_list2.index(item_2))
        ask_again()
    except ValueError:
        print("\nThe position of your number = -1 (Doesn't exist in the list)")
        ask_again()


def list_position_int():

    # Creating an empty list to append the inputs to it later
    # User input for how long they want their list to be
    index_list1 = []
    amount_1 = input("Please enter the amount of integers: ")

    # Error checking
    try:
        amount_1_int = int(amount_1)
    except Exception:
        print("Invalid input. Try again!")
        list_position_float()

    # Entering input for each index of the list with he size the user entered
    for i in range(1, amount_1_int + 1):
        value_1 = input("Please enter the Value of %d Element: " % i)

        # Error checking
        try:
            value_1_int = int(value_1)
        except Exception:
            print("Invalid input. Should be integers!")
            list_position_float()
        index_list1.append(value_1_int)

    item_1 = input("Please enter the integer you want to find: ")

    # Error checking
    try:
        item_1_int = int(item_1)
    except Exception:
        print("Invalid input. Try again!")
        list_position_float()

    try:
        print("The position of your number = ", index_list1.index(item_1_int))
        ask_again()
    except ValueError:
        print("The position of your number = -1 (Doesn't exist in the list)")


def list_position_choice():

    type_choice = input("Which type of numbers would you like to "
                        "enter(floats, integers, strings)?\n> ")

    if(type_choice == "int" or type_choice == "integer" or
       type_choice == "ints" or type_choice == "integers"):
        print()
        list_position_int()
    elif (type_choice == "floats" or type_choice == "float"):
        print()
        list_position_float()
    elif (type_choice == "strings" or type_choice == "string"
          or type_choice == "str"):
        print()
        list_position_str()
    else:
        print("Invalid choice, Please try again!")
        list_position_choice()


def type_of_list():

    # Choice of program
    begin_program1 = input("\nWhat would you like to do?\n"
                           "1. Translate a sentence to pig latin\n"
                           "2. Find your input in a list of numbers\n> ")

    # Check the input the user enters to determine which function they run
    if (begin_program1 == "1"):
        print()
        pig_latin_variable()
        time.sleep(0.5)
        print()
        ask_again()
    elif (begin_program1 == "2"):
        list_position_choice()
        print()
    else:
        print("Invalid Input. Try again!")
        type_of_list()


def main():

    # Give the user the point of the program and how it works
    # (Added the date and time for "extra functionality"
    # but I'm not sure if it counts)
    print("Today's date & time: {}" .format(datetime.datetime.now()))
    greeting = ("Welcome! Today you can choose which type of program "
                "you want to try! We can translate a message, "
                "or find input in a list!")

    # Loop to have typing text
    for letter in greeting:
        time.sleep(0.06)  # In seconds
        stdout.write(letter)
        stdout.flush()

    print()
    print()
    time.sleep(0.5)
    start_program = input("Start the lists program? y/n: ")

    # Input to start the program or not
    if start_program == "y":
        type_of_list()
    elif start_program == "n":
        print()
        goodbye = "Goodbye!"
        for letter in goodbye:
            time.sleep(0.06)  # In seconds
            stdout.write(letter)
            stdout.flush()
    else:
        print()
        print("I don't understand that. I'll just start you off!")
        time.sleep(0.5)
        type_of_list()


if __name__ == "__main__":
    main()
