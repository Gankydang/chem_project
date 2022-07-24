import random
from time import sleep

def is_correct(given_ans, correct_ans):
    if given_ans == '':
        return False
    if given_ans in correct_ans:
        return True
    return False

def organise_text(open_or_close):
    if open_or_close == 'open':
        print('-' * 60)
        print('|' + ' ' * 58 + '|')
    else:
        print('|' + ' ' * 58 + '|')
        print('-' * 60)

def get_corr_ans(insults, compliments, catpic,  question, *corr_ans, hint=False):
    given_ans = ''
    while not is_correct(given_ans, corr_ans):
        organise_text('open')
        given_ans = input(question).lower().strip()
        organise_text('close')
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

def room2():
    insp1 = insp2 = insp3 = False
    print('\nYou pick up the pieces distinctly pink coloured metal.')
    print('At one glance, you know this is the metal this facility is researching - Ellumium')

    while not all((insp1, insp2, insp3)):
        break
        inspect = None
        while not (inspect == '1' or inspect == '2' or inspect == '3'):
            print('''\nThere are 3 items that catch your eye:
        1) a note
        2) a solution of calcium nitrate
        3) a setup of some sort ''')
            print('\nWhich item would you like to inspect? (1, 2 or 3)')
            inspect = input('> ').strip()

            if inspect == '1':
                organise_text('open')
                print('''\nYou pick up the note, it reads:
        LOG 1:
            A solution of Ellumium ions is pink.
            Ellumium metal has a high melting point.''')
                organise_text('close')
                sleep(5)
                insp1 = True
            if inspect == '2':
                organise_text('open')
                print('\nYou walk toward the solution of calcium nitrate.')
                sleep(2)
                print('\nHowever, you suddenly trip over your UN-TIED SHOELACES!')
                sleep(2)
                print('\nYou are sent sprawling to the ground, but...')
                sleep(2)
                print('\nAs you are falling, you lose grip of the pieces of Ellumium in you hand.')
                sleep(3)
                print('\nMuch to your consternation, one piece of it plops directly\ninto the solution of calcium nitrate!')
                sleep(3)
                print('\nYou brace for something bad\nbut all you see is the solution turning from colourless to pink\nand a grey metal forming.')
                sleep(3)
                print('\nYou breathe a sigh of relief,\nand curse your laziness to tie your shoelaces.')
                organise_text('close')
                insp2 = True
            if inspect == '3':
                organise_text('open')
                print('\nYou walk toward the set up\nand immediately recognise it for a thermal decomposition set up.')
                sleep(3)
                print('\nA pink compound is contained in a test tube\nwhich is situated above a bunsen burner.')
                sleep(3)
                print('\nA delivery tube connects to the test tube which leads to\nblue cobalt (II) chloride paper.')
                sleep(3)
                print('\nYou turn on the bunsen burner and watch\nas the pink compound becomes a pink metal')
                print('and the blue cobalt (II) chloride paper turns pink.')
                organise_text('close')
                sleep(5)
                insp3 = True

    print('\nSomething else catches your eye.')
    print('Beside the door, paper with a series of questions\natop a number pad')
    sleep(4)
    print('\nThe number pad accepts a 2-digit number\nand you realise that the password to the door must be related to the questions.')
    print('You try to answer the questions first\nusing knowledge gained from inspecting the items.')
    sleep(4)

    insult = '\nEven though you thought of an answer,\nyour chemistry instincts kick in and tell you that your answer is wrong.'
    compliment = '\nYour chemistry tingle tells you that your answer is right'
    dying = '''\nAn alarm starts wailing and you know guards are on the way
however, as come in from the door behind you,
your martial arts training kicks in and you win a 1 v 10 fight.
\nYou continue as if nothing happened at all.'''
    open_door = '\nThe door slides upward with a hiss. You advance to the next room!'

    get_corr_ans(insult, compliment, '', '\nQ1. Ellumium is a __________ metal.\n> ', 'transition')
    get_corr_ans(insult, compliment, '', '\nQ2. What process is used to separate group I metals from their salts?\n> ', 'electrolysis')
    get_corr_ans(insult, compliment, '', '\nQ3. Water is known to have a high surface tension. This is because of ________ _______.\n> ', 'hydrogen bonds', 'hydrogen bonding')
    get_corr_ans(insult, compliment, '', '\nQ4. Which metal is Ellumium directly below in the reactivity series?\n> ', 'sodium')
    get_corr_ans(dying, open_door, '', '\nYou type in the 2-digit password on the number pad.\nThe psw is: ', '41', '43')

def room3():
    Q3a_qn = 'Besides its uses in question 2, transition metals are usually used as catalysts\nGiven that Ellumium has 3 oxidation states, is iron a better catalyst than ellumium?'
    Q3b_qn = 'Choose a reasoning:\na. Iron has more oxidation states\nb. Ellumium is more reactive\nc. Oxidation states do not determine a catalyst’s potential\nd. Iron is a more abundant metal'
    get_corr_ans('wrong', 'right', '', '\nQ1. Name one specific metal that is classified as a transition metal with 1 valence electron.\n> ', 'copper', 'chromium')
    get_corr_ans('wrong', 'right', '', '\nQ2. Ellumium is mainly used to make _____\n> ', 'circuits', 'wires')
    get_corr_ans('wrong', 'right', '', '\nQ3(a). ', Q3a_qn, '\n> ', 'no')
    get_corr_ans('wrong', 'right', '', '\nQ3(b). ', Q3b_qn, '\n> ', 'no') # idk what going on
    get_corr_ans('wrong', 'right', '', '\nQ3(b). ', Q3b_qn, '\n> ', 'no')

room2()
