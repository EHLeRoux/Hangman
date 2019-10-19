import random
lives = 8
game = True


def split_string_into_list(string):  # Takes a single string as a argument
    list = []  # Generates empty list
    for i in range(len(string)):
        list.append(string[i])  # Appends the list with the string characters to create a list of the string
        
    return list


def empty_list_creator(list):
    emptyList = []  # Creates a empty list
    for i in range(len(list)):
        emptyList.append("_")  # Creates a list with the same size as the word and fills it with the character _ 
    print(emptyList)
    return emptyList
    

def listComparison(list1, list2, char):  # Compares the word selected (list) with the empty list and the character the user enters
    global characterList
    characterList = []
    if char in characterList: 
        print("Your char has already been selected")

        userNewInput = input ("Please insert a new character that you have not chosen before")
        char = userNewInput
        characterList.append(char)
        
    elif char not in characterList:
        try:
            list1.index(char)  # If the character is not in the word, user loses a life
            
        except: 
            print("-----------------------------------------------")
            print("You have lost a life")
            print("-----------------------------------------------")
            global lives
            lives -= 1
    
        for index, character in enumerate(list1):  # enumerate function to keep track of the index, if the character user selected is in the list will place that character in the same position but in the empty list
            if character == char: 
                # print(index)
                list2[index] = char
        
        if list1 == list2:  # determines whether the user has completed their word and completes the game
            print(list2)
            print("-----------------------------------------------")
            print("Congrats! you have won!")
            print("-----------------------------------------------")
            quit()
            restart()
            
        if lives == 0:  # If their lives have reached zero they have lost
            print("-----------------------------------------------")
            print("Sorry, you have lost")
            print("-----------------------------------------------")
            quit()  # First quits the game and then
            restart()  # asks the user if they want to play again
    
        print("-----------------------------------------------")    
        print("Lives: ", lives)
        print("-----------------------------------------------")
    return list2


def quit():  # terminates the game when called because the game variable is global
    global game 
    game = False
    

def restart():
    user_restart = input ("Do you want to restart? Yes / No") 
    
    if user_restart == "Yes":  # Determines whether the user wants to restart his game
        global game  # Declaring game variable as global and setting the lives and game as True
        game = True
        global lives
        lives = 8
        userChoice = input(" Random: 1 \n animals: 2 \n movies: 3 \n games: 4 \n")
        
        # User choice regarding the type of words they want to play with, depending on the integer that list will be called
        if userChoice == "1":
            main_game(random_list)
            
        elif userChoice == "2":
            main_game(animals_list)
            
        elif userChoice == "3":
            main_game(movies_list)
            
        else:
            main_game(games_list)
            
    elif user_restart == "No":  # If user does not want to restart his game the quit function will be called which terminates the game
        print("-----------------------------------------------")
        print("Thanks for playing!")
        print("-----------------------------------------------")
        quit()
    

def getWord(my_list):  # takes in a list of words as a parameter
    random.shuffle(my_list)  # Shuffles the list of words with the random module
    selection_of_word = my_list[0].lower()  # Selects the first word of the shuffled list and makes it lowercase
    # print(selection_of_word)
    return(selection_of_word)  # returns one word


def main_game(chosen_list):
    word_in_list = split_string_into_list(getWord(chosen_list))  # Two functions are being called here, the GetWord function to get a random word and the split_string_into_list function
    # print(word_in_list)
    empty_list_of_length_of_word = empty_list_creator(word_in_list)  # This function also prints out a list with the same size as the selected word but the list is completely empty 
    characterList = []
    
    while game: 
        
        print("-----------------------------------------------")
        userInput = input("Please select your letter: ")
        print("-----------------------------------------------")
        
        characterList.append(userInput)
        print("characterlist: ", characterList)  # keeps track of the character 
        print(listComparison(word_in_list, empty_list_of_length_of_word, userInput))

    
if __name__ == "__main__": 
    
    # Four lists generated for the game
    random_list = ["Nintendo", "Playstation", "Xbox", "Batman", "revenge of the fallen", "Sony", "Darth Vader", "Peanut", "Kreator", "Avenged Sevenfold", "HyperionDev", "MacDonalds", "this is hangman", "God of War", "dog", "cat", "bird", "elephant" ]
    animals_list = ["dog", "cat", "Elephant", "Hippo", "Lion", "Tiger", "Whale", "Kuala", "Parrot", "bird", "monkey", "ape"]
    movies_list = ["Batman", "Transformers", "The Lego Movie", "Spider man", "Terminator", "The Avengers"]
    games_list = ["Call of duty", "Counter strike", "Dota 2", "Gears of war", "Tekken", "Mortal Kombat"]
    
    # introduction
    print("-----------------------------------------------")
    print("Welcome to Hangman! ")
    print("You have 8 lives each round")
    print("You can select from 4 different word categories")
    print("Please note that all words will be lowercase")
    print("-----------------------------------------------")
    
    # let the games begin
    restart()
    
