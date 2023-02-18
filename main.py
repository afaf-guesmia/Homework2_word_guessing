##Afaf Guesmia
## student Id: axg190061
##CS4395.001-HW2
##Use Python and NLTK features to explore a text file and create a word guessing game


import random
import sys
import nltk
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import collections
import string
import re
from random import seed
from random import randint

## main function
if __name__ == '__main__':
    ## Check if the user enter an argument
    if len(sys.argv) < 2:
        print("Error: Please enter the name of the file as system arg")
        quit()
        ##open file anat19.txt
    with open(r'anat19.txt', 'r') as file:
        ## read the file line by line as a raw text
        file_info = file.read()
        raw_text = repr(file_info)
        ## tokenize the whole raw text
        token_raw = nltk.word_tokenize(raw_text)
        ## count the number of tokens as well as the number of unique tokens
        token_num = len(token_raw)
        token_unique = len(set(token_raw))
        ## calculate the lexical diversity and printing in a 2 decimal places format
        lexical_d = token_unique / token_num
        lexi_d = "%.2f" % lexical_d
        print('Number of token in the text:', token_num)
        print('Number of unique tokens in the text:', token_unique)
        print("The lexical diversity:", lexi_d)
        ##ignore all the characters in the text
        text = re.sub(r'[.?!,:;()\-\n\d]', '' '', raw_text.lower())
        token_raw = nltk.word_tokenize(text)
        ## create funtion to preprocess the text
        def token_noun():
            ## create tokens that are only alpha, and length>5
            token_w = [t for t in token_raw if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]
            print(token_w, "\n")
            wnl = WordNetLemmatizer()
            ## lemmatize the tokens and use set() to make a list of unique lemmas.
            lemmatized = [wnl.lemmatize(t) for t in token_w]
            lemmatized_output = list(set(lemmatized))
            pos_lemma = nltk.pos_tag(lemmatized_output)
            ##pos tagging unique lemmas
            for i in range(20):
                print(pos_lemma[i])

            noun_lemma = [w[0] for w in pos_lemma if w[1] == 'NN']
            ## print only the number of tokens from step a and the number of nouns
            print("number of tokens from step a", len(token_w))
            print("number of tokens from step d", len(noun_lemma))
            lemma_count = collections.Counter(noun_lemma)
            lemma_dict = dict(lemma_count.most_common(50))
            lemma_list = list(lemma_dict.keys())


            ## return tokens from step a and nouns
            return token_w, lemma_list

        ## word guessing game
        names=token_noun()
        lemma_list=names[0]
        token_w=names[1]


        ## create a set of the guessing letters
        guess_l = set()
        ## Getting a random name from the list
        random_word= random.choice(lemma_list)
        ##printing the correct word to check the code  is working
        print(random_word,"(printing the word to make sure the code is working)")
        print("Let's play a game")
        ## initial points
        initial_points=5
        ##using while loop for each letter and calculating the points of the guessed letters
        while True:
            word=[w if w in guess_l else "_" for w in random_word]
            print(" ".join(word))
            user_input = input("guess a letter: ")
            if user_input in random_word:
                print("Right!")
                guess_l.add(user_input)
                initial_points=initial_points+1
                print("Score",initial_points)
            else:
                initial_points = initial_points - 1
                print("Wrong answer try again!",initial_points)
                ## using quit if the user has 0 or the user enters !
                if initial_points==0 or user_input=='!':
                    print("Sorry no more points")
                    initial_points=5
                    random_word = random.choice(lemma_list)
                    ##printing the right word to check if the code is working
                    print(random_word,"(printing the word to make sure the code is working)")
                    print("Guess a new word")



                    guess_l=set()





































