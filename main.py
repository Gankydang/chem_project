import random
from time import sleep

def is_correct(given_ans, correct_ans):
    if given_ans == '':
        return False
    if given_ans in correct_ans:
        return True
    return False

def is_correct_keywords(given_ans, *correct_ans, either_or=False):
    if given_ans == '':
        return False
    new_correct_ans = list(correct_ans)
    for i in correct_ans:
        if i in given_ans:
            new_correct_ans.remove(i)
    if len(new_correct_ans) == 0:
        for thing in either_or:
            if thing in given_ans:
                return True
    else:
        return False

def organise_text(open_or_close):
    if open_or_close == 'open':
        print('-' * 60)
        print('|' + ' ' * 58 + '|')
    else:
        print('|' + ' ' * 58 + '|')
        print('-' * 60)

def enter():
    input('---Press enter to continue---')

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
    print('WELCOME TO OUR ESCAPE ROOM')
    print('You are a scientist from the World Health Organisation (WHO)')
    print('''       .-""-.
      /-.{}  \\
      | _\\__.|
      \/^)^ \\/
       \\ =  /
  .---./`--`\\.--._
 /     `;--'`     \\
;        /`       ;
|       |*        |
/   |   |     |    \\
|    \\  |*    /    |
\_   |\\_|____/|  __/
  \\__//======\\\\__/
  / //_      _\\\\ \\
  -'  |`""""`|  `-
      |  L   |
      >_ || _<
      |  ||  |
      |  ||  |
     /   ||   \\
    /    /,    \\
     `|"|`"|"|"`
     /  )  /  )
    /__/  /__/
    ''')
    print(' ^ \n | \nYou')
    enter()
    print('''Background:
    A new metal has been discovered in one of the deepest parts of the ocean.
    Scientists have named this metal Ellumium, with the chemical symbol El, and much of its
    properties is currently unknown. WHO has advised everyone to
    abstain from using this metal in production until further research despite its many ideal
    properties and can be found abundant in that area and therefore very affordable.
    You are from the WHO. The WHO has been tipped off about a secret facility that is using this
    metal for nefarious purposes. You are tasked with heading to the facility and discovering for
    yourself what exactly they are doing. You are told that collaborators of the facility are using
    a newspaper to transmit information, and in this case, the name of the town that the facility is located in.
''')
    print('''()_________)
 \\ ~~~~~~~~ \\
  \\ ~~~~~~   \\
   \\__________\\
    ()__________))''')
    enter()
    print(''''You get a copy of the newspaper in question and inspect it.
There is a very sus chemistry quiz and you decide to take a look.''')

def room1():
    list_of_insults = ['WRONG:(', 'TOO BAD', 'WHOOPS!', 'TRY AGAIN', 'GO STUDY MORE', 'GITGUD', 'NATURAL SELECTION DOES\'NT FAVOUR YOU']
    list_of_compliments = ['smarty pants', 'mugger', 'good job', 'nerd', 'k, fine you passed ig', 'we are proud of you']
    cat1 = '''\n|\\---/|
| o_o |
 \\_^_/'''
    cat2 = '''\n|\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
|,4-  ) )-,_. ,\\ (  `'-'
'---''(_/--'  `-'\\_)'''
    cat3 = ''' \n_._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \ )-`( , o o)
          `-    \\`_`"'-'''
    cat4 = '''\n                 __        .-.
             .-"` .`'.    /\\\\|
     _(\\-/)_" ,  .   ,\\  /\\\\\\/
    {(#b^d#)} .   ./,  |/\\\\\\/
    `-.(Y).-`  ,  |  , |\\.-`
         /~/,_/~~~\\,__.-`
        ////~    // ~\\\\
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
    hint_room1 = 'TAKE THE FIRST LETTERS.'
    town_question = '\nThe name of the town that the facility is in is (if you really dont know the answer type "hint"): '
    get_corr_ans(wrong_town, corr_town, '\n:) yay!', town_question, 'topi', hint=hint_room1)

def room2():
    insp1 = insp2 = insp3 = False
    print('''                 _ _.-'`-._ _
                ;.'________'.;
     _________n.[____________].n_________
    |""_""_""_""||==||==||==||""_""_""_""]
    |"""""""""""||..||..||..||"""""""""""|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    |.. .. .. ..||..||..||..||.. .. .. ..|
    |LI LI LI LI||LI||LI||LI||LI LI LI LI|
 ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;''')
    print('\nYou head to the facility in the dead of night and see a giant building looming up in front of you.')
    print('''It gave an eerie atmosphere with the silence in the night sky,
the only sound being the croaking of frogs and crickets.
You see guards stationed at the outside and think of a way to get inside.

SUDDENLY, the lights in the facility turn off in unison and you know something is not right.
Maybe the facility lost power for a brief time?
Does that mean the doors have become unlocked briefly?
The guards can't see in the pitch dark can they?''')
    enter()
    print('''You decide to take a gamble.
You sprint for the door, past the unsuspecting guards.
They do not notice you and you push the door to the facility open.
You made it!

But just as you set foot into the room, the power is returned and
the room illuminates.You try the door you came in through but, just as you expected,
it is locked. After all, your mission is to explore the facility,
so you decide to delve deeper into the facility.

The room looks to be a typical chemistry lab,
except for pieces of a peculiar metal sitting primly on a table.
You noticed that there is a ppe suit beside the door and decided to wear it before
continuing into this mysterious room to further record down any new information.''')

    print('\nYou pick up the pieces distinctly pink coloured metal.')
    print('At one glance, you know this is the metal this facility is researching - Ellumium')
    enter()
    while not all((insp1, insp2, insp3)):
        inspect = None
        while not (inspect == '1' or inspect == '2' or inspect == '3'):
            print('''\nThere are 3 items in the room that catch your eye:
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
                enter()
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
                enter()
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
                enter()
                insp3 = True

    print('\nSomething else catches your eye.')
    print('Beside the door, a paper with a series of questions\nsits atop a number pad')
    sleep(4)
    print('\nThe number pad accepts a 2-digit number\nand you realise that the password to the door must be related to the questions.')
    print('You try to answer the questions first\nusing knowledge gained from inspecting the items.')
    enter()

    insult = '\nEven though you thought of an answer,\nyour chemistry instincts kick in and tell you that your answer is wrong.'
    compliment = '\nYour chemistry tingle tells you that your answer is right'
    dying = '''\nAn alarm starts wailing and you know guards are on the way
however, as come in from the door behind you,
your martial arts training kicks in and you win a 1 v 10 fight.
\nYou casually continue as if nothing happened at all.'''
    open_door = '\nThe door slides upward with a hiss. You advance to the next room!'
    hint2 = 'Count the number of letters.'

    get_corr_ans(insult, compliment, '', '\nQ1. Ellumium is a __________ metal.\n> ', 'transition')
    get_corr_ans(insult, compliment, '', '\nQ2. What process is used to separate group I metals from their salts?\n> ', 'electrolysis')
    get_corr_ans(insult, compliment, '', '\nQ3. Water is known to have a high surface tension. This is because of ________ _______.\n> ', 'hydrogen bonds', 'hydrogen bonding')
    get_corr_ans(insult, compliment, '', '\nQ4. Which metal is Ellumium directly below in, in the reactivity series?\n> ', 'sodium')
    get_corr_ans(dying, open_door, '', '\nYou type in the 2-digit password on the number pad. (type "hint" if you really don\'t know)\nThe psw is: ', '41', '43', hint=hint2)
    enter()

def room3():
    print('''This room much the same as the previous one,
except for a few stray pieces of wire and circuit boards scattered everywhere.
At the other end of the room, there is a door and beside it, a screen that seems to be waiting for some input.
Beside the screen, there is a series of questions.

You decide to answer the questions first.''')
    enter()

    wrong = 'You have an answer, but it just seems wrong for some reason.'
    right = ['Yes! You pump your fist in the air in celebration!', 'Yes! You jump so high that your head hits the celing with a thump, ouch!', 'Thats right!']
    Q3a_qn = 'Besides its uses in question 2, transition metals are usually used as catalysts\nGiven that Ellumium has 3 oxidation states, is iron a better catalyst than ellumium?'
    Q3b_qn = 'Choose a reasoning:\na. Iron has more oxidation states\nb. Ellumium is more reactive\nc. Oxidation states do not determine a catalyst’s potential\nd. Iron is a more abundant metal'
    Q4a_qn = '''Elumium is naturally found in an ore, Elumium(II) Oxide(El2O).
Given that the extraction of Elumium is similar to that of the extraction of iron from haematite,
and given that the first equation is C + O2 —> CO₂,
what is the enthalpy change of this reaction (+ / -)? '''
    Q4b_qn = 'Which state of matter is Ellumium produced?'

    get_corr_ans(wrong, right, '', '\nQ1. Name one specific metal that is classified as a transition metal with 1 valence electron\nand is used to make bronze.\n> ', 'copper')
    get_corr_ans(wrong, right, '', '\nQ2. Ellumium is mainly used to make _____\n> ', 'circuits', 'wires')
    get_corr_ans(wrong, right, '', '\nQ3(a). ' + Q3a_qn + '\n> ', 'no')
    get_corr_ans(wrong, right, '', '\nQ3(b). ' + Q3b_qn + '\n> ', 'c')
    get_corr_ans(wrong, right, '', '\nQ4(a). ' + Q4a_qn + '\n> ', '-')
    get_corr_ans(wrong, right, '', '\nQ4(b). ' + Q4b_qn + '\n> ', 'liquid')
    enter()

    print('''After collating your answers to the questions, you seem to accidentally knock into a bookshelf
containing the numerous research that the scientists of this research facility have already recorded.
However, you notice that after you slightly moved the bookshelf it suddenly made way and moved to the left
thus revealing a door behind the bookshelf. After further inspection, you realise that the door was transparent
and you can see the ellumium metal being processed. You noticed that there is a ppe suit beside the door and
decided to wear it before entering this mysterious door to further record down any new information. The door
quickly locks behind you. Under the keypad of the door, you notice a small piece of paper sticking out with these
questions. Written on the back of the paper you see it says:

    1. 5th letter of First answer

    2. Take the number of letters in the second answer and use this formula. n*2+2=y. Find the yth letter of the alphabet

    3. Take the answers of the 3rd question and get the number of total letters there are. Let this number be x. Use this formula.
    nx2=p. P will be a double digit number so inverse the number (for example 10 inversed is 01.) Let this new number be w and then find the Wth letter in the alphabet.

    4. Take the total number of letters in the both the answers of the 4th questions and let it be Q.
    Then use the formula Q*2-2/2=v. Then find the Vth letter of the alphabet.
''')
    enter()
    print('''You realise that this is the key to the password that the screen beside the door was asking for!
You work to get the code and enter it.''')
    dying = '''You input the password...

Alarms start blaring and a machine gun magically appeared from the celing.
It aims at you with a red lazer and you know what you have to do.

Your martial arts training kicks in again. You are like Neo from the matrix,
dodging and weaving through the volley of bullets that start raining down at you.
The machine gun gets confused, it has never met a worthy opponent before.
It uses all its might to land a shot but it never got the chance to fire the first
bullet.

YOU SEND A FLYING KICK TOWARDS THE MACHINE GUN. A cracking sound can be heard and
it retracts. You casually continue inputing the password.'''
    correct = 'You hear the chiming of a bell, signaling that you got the correct password.'
    get_corr_ans(dying, correct, '', '\nThe name of the lead scientist is: ', 'elum')
    print('The door opens with a hiss, leading to another room. But something\'s bothering you.')
    print('Elum, hmm...\nWhy does that name sound so familiar?\nYou keep the name in the back of your mind as you progress.')
    enter()

def room4():
    print('\nThis next room has a different odur and different layout altogether.')
    print('There are heating elements and loose Ellumium metal scattered everywhere.')
    print('\nThere is a newspaper article stuck to the wall. It reads:')
    print('''\tOne of the reasons why ellumium was a metal that the WHO has advised strongly against
    for its usage in any industrial or commercial use due to its toxic properties and the
    environmental issues it can cause. The WHO has not released a full report of the toxicity of the
    metal and scientists have to do a deeper analysis of the metal’s toxic properties.''')
    enter()

    organise_text('open')
    print('''You see another note on the desk. The note reads:
        LOG 2:
            I have broken some Ellumium metal to smaller pieces for it to be used to make wires.
            However, it appears that Ellumium can suspend in the air as Ellumium particles.
            Moreover, is extremely reactive and hence needs to be stored as a stable compound.''')
    organise_text('close')

    print('\nThere is yet another keypad next to the door.')
    print('You are getting sick of seeing keypads.')
    print('This one is asking series of questions that you feel you can use the knowledge you have gained to solve.')
    enter()

    Q1 =  '''There are a few metals already recorded in our periodic table
that are toxic or radioactive to humans which can cause mutations or metal poisoning. Name one.'''
    Q3 = '''Name one stable halide that Ellumium can form given that it needs
to be broken down into its metal, given that Ellumium is made to have a charge of +3.
(Give your answers in the chemical name)'''
    Q4 = 'Explain how the Ellumium compound previously stated can be stored in relatively high temperatures and remain in its solid state.'
    Q5 = '''How can Ellumium be harmful to your body based on your prior chemistry knowledge?
    a. The ellumium can form an acid that lowers the pH of the stomach that can corrode your stomach
    b. The ellumium can explode in your body
    c. The elumium will displace sodium from sodium chloride in your body which\nwill therefore reduce the amount of sodium chloride in your body which inhibits growth
    d. The ellumium can form a alkali that increase the pH of the body that is not optimal for enzyme function'''
    dying = '''An alarm starts blaring. You wait for something to start attacking you,
        but nothing ever comes. You are confused but casually continue to answer the questions.'''
    right = 'A robotic voice seems to be coming from everywhere in the room, "CORRECT!"'


    get_corr_ans(dying, right, '', '\nQ1. ' + Q1 + '\n> ', 'arsenic', 'cadmium', 'lead', 'mercury', 'radium', 'uranium')
    get_corr_ans(dying, right, '', '\nQ2. Name another metal that is toxic in the same way that Ellumium is.\n> ', 'lead')
    get_corr_ans(dying, right, '', '\nQ3. ' + Q3 + '\n> ', 'ellumium (iii) bromide', 'ellumium (iii) iodide', 'ellumium (iii) chloride', 'ellumium (iii) fluoride')
    given_ans = ''
    while not is_correct_keywords(given_ans, 'giant ionic structure', 'break', 'strong electrostatic forces of attraction', either_or=('a lot of energy', 'high energy', 'much energy')):
        organise_text('open')
        given_ans = input('\nQ4. ' + Q4 + '\n> ').lower().strip()
        organise_text('close')
        if not is_correct_keywords(given_ans, 'giant ionic structure', 'break', 'strong electrostatic forces of attraction', either_or=('a lot of energy', 'high energy', 'much energy')):
            print(dying)
        else:
            print(right)
    get_corr_ans(dying, right, '', '\nQ5. ' + Q5 + '\n> ', 'd')

    enter()
    print('The door opens with a "ding" sound.')
    print('However, as the door slides open, you see a very buff guard staring right at your face...')
    print('It seems as if they found out that you were sneaking around in their facility.')
    print('The last thing you remember something slamming hard into the side of your head before you black out.')
    enter()

def room5():
    print('You wake up in a room that parallels a prison cell.')
    print('''The door seems to be locked by a number keypad. You wait a couple of hours
till it is night time and until then you think of how you’re gonna escape but you feel hopeless.
Suddenly a piece of paper gets slipped under your door. You quickly grab it and it has this written. Odd-43. Even-36. Count!. And the following questions.
It is also written on the note, "I am undercover in this facility and I am here to help you escape. Meet me at the exit,
you will have to make your way there yourself.''')
    enter()

    Q1 = 'When elumium gets oxidised, the oxide can then react with both acids and bases. So, Elumiumi Oxide is _____'
    Q2 = 'Elumium can readily react with oxygen in the air to for a insoluble oxide layer.\nIn order to prevent this what is a method that can be used other than surface protection?'
    Q3 = 'Elumium and Graphite have a similar property of conducting electricity.\nWhat is the common thing that brings this common property?'
    Q4 = 'Elumium reacts with cold water to form _____ and water.'

    get_corr_ans('wrong', 'right', '', '\nQ1. ', Q1, '\n> ', 'amphoteric')
    get_corr_ans('wrong', 'right', '', '\nQ2. ', Q2, '\n> ', 'galvanising', 'sacrificial protection')
    get_corr_ans('wrong', 'right', '', '\nQ3. ', Q3, '\n> ', 'delocalised electrons')
    get_corr_ans('wrong', 'right', '', '\nQ1. ', Q4, '\n> ', 'ellumium hydroxide')
    get_corr_ans('wrong', 'right', '', 'You enter the pin into the keypad: ', '151', hint='Check whether each answer is even or odd\nThen add the corresponding number')

    print('''The door slides open with a whir and you hurry around the facility, trying to find the exit
while not getting spotted by guards. You see the exit and run at full throttle!''')
    enter()

def end():
    print('''You burst out the front door and scramble out. It is night time,
and the guards seem half asleep so you slowly sneak out of the facility.
Just at the exit, you see a guard standing tall and staring at you.

He says this, “Took you long enough. I slipped you that paper. WHO bought me over to their side when
they had an inkling you were in danger."

You reply, "We need to destroy this facility right now. This place is obviously evil
and we cannot allow it to go on. How are we gonna destroy it?"

He beamed, "I know just the right thing. Now, there is a small room in the far north of the
facility where a large clump of ellumium is. Right above is a large pipe of water.
You know what would happen if you were to break the pipe. It is very risky, but it's for the greater good.
Or do you wish to save yourself and run away? The choice is yours to make. I trust you will make the right decision.''')


room4()
