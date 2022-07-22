import random
from time import sleep

def is_correct(given_ans, correct_ans):
    if given_ans == '':
        return False
    if given_ans in correct_ans:
        return True
    return False

def get_corr_ans(insults, compliments, catpic,  question, *corr_ans, hint=False):
    given_ans = ''
    while not is_correct(given_ans, corr_ans):
        given_ans = input(question).lower().strip()
        if given_ans == 'hint' and bool(hint):
            print(hint)
            continue
        if not is_correct(given_ans, corr_ans):
            if type(insults) == str:
                print(insults)
            else:
                print(random.choice(insults))
        else:
            if type(compliments) == str:
                print(compliments)
            else:
                print(random.choice(compliments))
            print(catpic)

def intro():
    print('WELCOME TO OUR ESCAPE ROOM\n')
    print('''Background:
    ''')

def room1():
    list_of_insults = ['WRONG:(', 'TOO BAD', 'WHOOPS!', 'TRY AGAIN', 'GO STUDY MORE', 'GITGUD', 'NATURAL SELECTION DOES\'NT FAVOUR YOU']
    list_of_compliments = ['smarty pants', 'mugger', 'good job', 'nerd', 'k, fine you passed ig', 'we are proud of you']
    cat1 = '''\n|\---/|
| o_o |
 \_^_/'''
    cat2 = '''\n|\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
|,4-  ) )-,_. ,\ (  `'-'
'---''(_/--'  `-'\_)'''
    cat3 = ''' \n_._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-'''
    cat4 = '''\n                 __        .-.
             .-"` .`'.    /\\|
     _(\-/)_" ,  .   ,\  /\\\/
    {(#b^d#)} .   ./,  |/\\\/
    `-.(Y).-`  ,  |  , |\.-`
         /~/,_/~~~\,__.-`
        ////~    // ~\\
      ==`==`   ==`   ==`'''


    print('\nThe chemistry quiz questions are as follows:\n(give your answers in their chemical names where applicable)')

    get_corr_ans(list_of_insults, list_of_compliments, cat1, '\nQ1. What is the molecular shape of XeO₃?\n> ', 'trigonal pyramidal')
    get_corr_ans(list_of_insults, list_of_compliments, cat2, '\nQ2. What neutral gas is produced when you decompose gold (II) nitrate?\n> ', 'oxygen')
    get_corr_ans(list_of_insults, list_of_compliments, cat3, '\nQ3. Which metal reacts violently and explosively with dilute acids to give off a lilac flame?\n> ', 'potassium')
    get_corr_ans(list_of_insults, list_of_compliments, cat4, '\nQ4. Chromium(III)Oxide is insoluble and _____, which prevents the iron in steel from rusting.\n> ', 'impervious')

    print('\nYou scratch you head,\nhow are the spys using this chemistry quiz to communicate the town name?')
    sleep(2)
    print('\nWait...')
    sleep(2)
    print('\nYou have an eurika moment!')

    wrong_town = f'You think got the name of the town, but something in your mind thinks otherwise.'
    corr_town = f'Thats it! The facility is in the town of Topi!'
    hint_room1 = 'TAKE THE FIRST LETTER.'
    town_question = '\nThe name of the town that the facility is in is (if you really dont know the answer type "hint"): '
    get_corr_ans(wrong_town, corr_town, '\n:) yay!', town_question, 'topi', hint=hint_room1)

room1()
