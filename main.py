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
    print('You are a scientist and investigaor from the World Health Organisation (WHO)')
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
    Scientists have named this metal Elumium, with the chemical symbol El, and much of its
    properties is currently unknown. WHO has advised everyone to
    abstain from using this metal in production until further research despite its many ideal
    properties and can be found abundant in that area and therefore very affordable.
    The WHO has been tipped off about a secret facility that is using this
    metal for nefarious purposes.

    You, as the lead investigator and one of the best scientists in the WHO, are tasked with heading
    to the facility and discovering for yourself what exactly they are doing. You are told that collaborators of the facility are using
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
    print('At one glance, you know this is the metal this facility is researching - Elumium')
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
            A solution of Elumium ions is pink.
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
                print('\nAs you are falling, you lose grip of the pieces of Elumium in you hand.')
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

    get_corr_ans(insult, compliment, '', '\nQ1. Elumium is a __________ metal.\n> ', 'transition')
    get_corr_ans(insult, compliment, '', '\nQ2. What process is used to separate group I metals from their salts?\n> ', 'electrolysis')
    get_corr_ans(insult, compliment, '', '\nQ3. Water is known to have a high surface tension. This is because of ________ _______.\n> ', 'hydrogen bonds', 'hydrogen bonding')
    get_corr_ans(insult, compliment, '', '\nQ4. Which metal is Elumium directly below in, in the reactivity series?\n> ', 'sodium')
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
    Q3a_qn = 'Besides its uses in question 2, transition metals are usually used as catalysts\nGiven that Elumium has 3 oxidation states, is iron a better catalyst than ellumium?'
    Q3b_qn = 'Choose a reasoning:\na. Iron has more oxidation states\nb. Elumium is more reactive\nc. Oxidation states do not determine a catalyst’s potential\nd. Iron is a more abundant metal'
    Q4a_qn = '''Elumium is naturally found in an ore, Elumium(III) Oxide.
Given that the extraction of Elumium is similar to that of the extraction of iron from haematite,
and given that the first equation is C + O2 —> CO₂,
what is the enthalpy change of this reaction (positive / negative)? '''
    Q4b_qn = 'Which state of matter is Elumium produced?'

    get_corr_ans(wrong, right, '', '\nQ1. Name one specific metal that is classified as a transition metal with 1 valence electron\nand is used to make bronze.\n> ', 'copper')
    get_corr_ans(wrong, right, '', '\nQ2. Elumium is mainly used to make _____\n> ', 'circuits', 'wires')
    get_corr_ans(wrong, right, '', '\nQ3(a). ' + Q3a_qn + '\n> ', 'no')
    get_corr_ans(wrong, right, '', '\nQ3(b). ' + Q3b_qn + '\n> ', 'c')
    get_corr_ans(wrong, right, '', '\nQ4(a). ' + Q4a_qn + '\n> ', 'negative')
    get_corr_ans(wrong, right, '', '\nQ4(b). ' + Q4b_qn + '\n> ', 'liquid')
    enter()

    print('''After collating your answers to the questions, you seem to accidentally knock into a bookshelf
containing the numerous research that the scientists of this research facility have already recorded.
However, you notice that after you slightly moved the bookshelf it suddenly made way and moved to the left
thus revealing a door behind the bookshelf. After further inspection, you realise that the door was transparent
and you can see the Elumium metal being processed. You noticed that there is a ppe suit beside the door and
decided to wear it before entering this mysterious door to further record down any new information. The door
quickly locks behind you. Under the keypad of the door, you notice a small piece of paper sticking out with these
questions. Written on the back of the paper you see it says:

    1. 5th letter of First answer

    2. Take the number of letters in the second answer and use this formula. n*2+2=y. Find the yth letter of the alphabet

    3. Take the answers of the 3rd question and get the number of total letters there are. Let this number be x. Use this formula.
    nx2=p. P will be a double digit number so reverse the number (for example 10 reversed is 01.) Let this new number be w and then find the Wth letter in the alphabet.

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
    print('There are heating elements and loose Elumium metal scattered everywhere.')
    print('\nThere is a newspaper article stuck to the wall. It reads:')
    print('''\tOne of the reasons why Elumium was a metal that the WHO has advised strongly against
    for its usage in any industrial or commercial use due to its toxic properties and the
    environmental issues it can cause. The WHO has not released a full report of the toxicity of the
    metal and scientists have to do a deeper analysis of the metal’s toxic properties.''')
    enter()

    organise_text('open')
    print('''You see another note on the desk. The note reads:
        LOG 2:
            I have broken some Elumium metal to smaller pieces for it to be used to make wires.
            However, it appears that Ellumium can suspend in the air as Elumium particles.
            Moreover, is extremely reactive and hence needs to be stored as a stable compound.''')
    organise_text('close')

    print('\nThere is yet another keypad next to the door.')
    print('You are getting sick of seeing keypads.')
    print('This one is asking series of questions that you feel you can use the knowledge you have gained to solve.')
    enter()

    Q1 =  '''There are a few metals already recorded in our periodic table
that are toxic or radioactive to humans which can cause mutations or metal poisoning. Name one.'''
    Q3 = '''Name one stable halide that Elumium can form given that it needs
to be broken down into its metal, given that Elumium is made to have a charge of +3.
(Give your answers in the chemical name)'''
    Q4 = 'Explain how the Elumium compound previously stated can be stored in relatively high temperatures and remain in its solid state.'
    Q5 = '''How can Elumium be harmful to your body based on your prior chemistry knowledge?
    a. The Elumium can form an acid that lowers the pH of the stomach that can corrode your stomach
    b. The Elumium can explode in your body
    c. The Elumium will displace sodium from sodium chloride in your body which\n\twill therefore reduce the amount of sodium chloride in your body which inhibits growth
    d. The Ellumium can form a alkali that increase the pH of the body that is not optimal for enzyme function'''
    dying = '''An alarm starts blaring. You wait for something to start attacking you,
        but nothing ever comes. You are confused but casually continue to answer the questions.'''
    right = 'A robotic voice seems to be coming from everywhere in the room, "CORRECT!"'


    get_corr_ans(dying, right, '', '\nQ1. ' + Q1 + '\n> ', 'arsenic', 'cadmium', 'lead', 'mercury', 'radium', 'uranium', 'francium', 'bismuth')
    get_corr_ans(dying, right, '', '\nQ2. Name another metal that is toxic in the same way that Elumium is.\n> ', 'lead')
    get_corr_ans(dying, right, '', '\nQ3. ' + Q3 + '\n> ', 'elumium (iii) bromide', 'elumium (iii) iodide', 'elumium (iii) chloride', 'elumium (iii) fluoride')
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
    print('''                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \\  =  /
                 |\\___/|
        ___ ____/:     :\\____ ___
      .'   `.-===-\\   /-===-.`   '.
     /      .-"""""-.-"""""-.      \\
    /'             =:=             '\\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\\   '.)
  /' ._/   ".     --:--     ."   \\_. '\\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \\ : |       |_____._____|       | : /
  /   (       |----|------|       )   \\
 /... .|      |    |      |      |. ...\\
|::::/''     /     |       \\     ''\\::::|
'""""       /'    .L_      `\\       """"'
           /'-.,__/` `\__..-'\\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \\___|
          :===|            |==|
           \\  /            |__|
           /\/\           /"""`8.__
           |oo|           \\__.//___)
           |==|
           \\__/)''')
    print('It seems as if they found out that you were sneaking around in their facility.')
    print('The last thing you remember something slamming hard into the side of your head before you black out.')
    enter()

def room5():
    print('You wake up in a room that parallels a prison cell.')
    print('''The door seems to be locked by a number keypad. You are seriously questioning your sanity after seeing so many keypads.
You slide to the algae covererd floor, utterly defeated. After waiting a couple of hours,
you see the sun making its descent through the bars of your cell, casting a magnificent red glow across the sky.
You try to remember who Elum was again but to no avail.

Before long, night befell and everything is silent and dark. You think of how you’re gonna escape but after
exhausting all options, hope of an escape now seems like an untouchable dream.

Not only do you have to escape, but you have to warn the WHO about this place.
It seems like they are using toxic Elumium metal as a cheap
substitute for copper to make wires. Moreover, in the fleeting moments that you regained consciousness
while they were dragging you to your cell, you caught glimpses of weapons with the distinct pink
metal incorporated into it.

What will happen if they continue doing this?
Am I stuck here for the rest of my life?
Will my family know that I am still here?

The sound of crackling paper rouses you out of your melancholic reverie. You get up and head towards the sound.
You feel the ground in pitch dark until your fingers touch a piece of paper. It seems that someone has slipped it
into your cell. You quickly grab it and use the moonlight to read untidy words scrawled there.
It reads, "I am undercover in this facility and I am here to help you escape. Meet me at the exit,
you will have to make your way there by yourself..."

"The following information will help you to escape this room."

Odd - 43. Even - 36. Count!. And the following questions.''')
    enter()

    Q1 = 'When Elumium gets oxidised, the oxide can then react with both acids and bases. So, Elumium Oxide is _____'
    Q2 = 'Elumium can readily react with oxygen in the air to for a insoluble oxide layer.\nIn order to prevent this what is a method that can be used other than surface protection?'
    Q3 = 'Elumium and Graphite have a similar property of conducting electricity.\nWhat is the common thing that brings this common property?'
    Q4 = 'Elumium reacts with cold water to form _____ and water.'
    wrong = '''A giant red 'X' appears across the screen, accompanying a sound of disapproval. You hear something moving behind you...
You whirl around to be greeted by the toilet, which was previously situated at the other corner of the room,
which had sprouted arms and legs. It makes a flushing sound and starts vomitting toilet water at you.

You try to dodge it but still get a facefull of disgusting toilet water. The toilet returns back to its
original resting spot and its arms and legs retract. Disgusted, this makes you want to escape this place
even more. You try again.'''
    right = '''The door clicks but seems to be jammed. You pry it open with all your might,
biceps bulging.'''
    incorrect = '''Ths isn't the time to be fooling around. You try again.'''
    correct = 'You are one step closer to escaping this wretched place!'

    get_corr_ans(incorrect, correct, '', '\nQ1. ' + Q1 + '\n> ', 'amphoteric')
    get_corr_ans(incorrect, correct, '', '\nQ2. ' + Q2 + '\n> ', 'galvanising', 'sacrificial protection')
    get_corr_ans(incorrect, correct, '', '\nQ3. ' + Q3 + '\n> ', 'delocalised electrons')
    get_corr_ans(incorrect, correct, '', '\nQ4. ' + Q4 + '\n> ', 'elumium (iii) hydroxide')
    get_corr_ans(wrong, right, '', 'You enter the pin into the keypad: (if you really don\'t know enter "hint")', '151', hint='Check whether each answer is even or odd\nThen add the corresponding number')

    print('''Finally, the door slides open and you hurry around the facility, trying to find the exit
while not getting spotted by guards. After some time, you suddenly spot the exit and run at full throttle towards it!''')
    enter()

def end():
    print('''You burst out the front door and into the night.
The guards seem half asleep so you slowly sneak past them. Then, someone
touches your shoulder. You jump, startled, and turn to face the foe.
A guard is standing tall and staring at you. You prepare to throw him an uppercut when
he says, “Took you long enough. I slipped you that paper. WHO notified when
they had an inkling that you were in danger."''')
    enter()
    print('''You are surprised that WHO actually had a "man on the inside" for this facility

You reply, "We need to destroy this facility right now. This place is obviously evil
and we cannot allow it to go on. It is planning to weaponise Ellumium and
use it for wires despite its toxic properites! How are we gonna put a stop to this?
If we don't destroy the facility now, by the time WHO takes action, it may already be too late."

He beamed, "I fully agree with you, I also saw some deadly looking weapons while
walking around the facility. Now, there is a small room in the far north of the
facility where a large clump of Elumium is. Right above is a large water pipe.
You know what would happen if you were to break the pipe. It is very risky, but it's for the greater good.
The place could very well explode and kill everyone inside.

The decision is yours, after all, you are our lead investigator. I trust that you will make the best decision.
Do you wish to make your escape or to take the risk and save millions of lives? I trust you will make the right choice."''')
    enter()
    question = '''What would you like to do?
    a. make your cowardly escape and possibly be indirectly responsible for millions of deaths
    b. destroy the facility and risk dying for the greater good\n> '''
    if_a = '''You decide to be a coward, "I think we should escape. The WHO can take care of this
on their own."'''
    if_b = '''After fully assessing the situation, you decide to take the risk. You are the lead
investigator, one of the best scientists. The WHO hired you for a reason - to always do what is right,
to put others lives before your own. So what if you don't make it out?

You say, "I have made my choice. I'll go in and destroy this place. If I don't make it out in 10
minutes, leave without me."'''
    given_ans = ''


    while not is_correct(given_ans, ['a', 'b']):
        given_ans = input(question).lower().strip()

        if given_ans == 'a':
            print(if_a)
            print('''The guard is slightly disappointed in you but he runs away with you.
A helicopter from the WHO lands and you jump right in.
Although the guard seems only slightly disappointed with your choice,
the pilot is extremely disappointed.

He decides to take matters into his own hands and crashes the chopper
into the facility. As the chopper is careening into the building, you
are petrified. The last thought you have is a quote that you remember
from your chemistry teacher, Mr Lum, all those years back.

Wait...

Mr Lum, Mr Elum...
No way...
He wouldn't do such things...

The whole place explodes in a flurry of flames and had no survivors.''')
            enter()
            print('''Years later, children learn in their textbooks of
the story of this facility. They learn of the scientist, lead investigator,
and how he was a coward. Everyone revolts at the sound of your name.
You are now infamous, are you happy?

THE END ''')

        if given_ans == 'b':
            print(if_b)
            print('''The guard gives an affirmative nod, "You will make it back."
You rush into the facility and locate the small room. There is a very handy gun hanging inside, you pick it up.
As the guard said, there was a large pipe right above a massive container of Elumium metal pieces.
''')
            ans = ''
            while not is_correct(ans, ['yes', 'no']):
                ans = input('Are you sure you want to break the pipe? ').lower().strip()
                if ans == 'no':
                    print('''At the last moment, you decide to chicken out. You try
to sneak out again. However, the guards suddenly hear you trying to sneak out and
they put a bullet through your face (and every hole in your body).
As the bullet bores a hole into your brain, you don't know why, but
you think of your chemistry teacher, Mr Lum.

Hold up...
That was the name of the scientist!
But why...

The bullet fully passes through your skull and you fall to the ground.''')
                    enter()
                    print('''Years later, children learn in their textbooks of
the mass genocide a few years ago. They learn of the scientist, lead investigator,
and how he was a coward. How he could have prevented this with the sacrifice of one life,
his life. Of how he could have prevented the killing of millions of people.

You are remembered as the coward who ran away.
You are held responsible for all those deaths.
Are you happy?

THE END''')
                if ans == 'yes':
                    print('''You break the pipe and run as fast as you can to the exit.
Then you remember you run like a kaushik. The room and corridor becomes engulfed in flames.
The heat of the fire gently kisses your face and then it suddenly slaps you in your face.
The flames lick your face as you struggle to breathe.
Your legs start to melt and then your eyes also liquify.

You think to yourself, “Welp at least I'm dying in glory and saving the world from this facility.
As my chemistry teacher taught me once, sacrifice for the greater good. My chemistry teacher...
WAIT! HE WAS THE LEAD SCIENTIST OF THIS PLACE?
BUT..."

The flames fully engulf you like a blanket, you are glad that it had to be you,
to sacrifice yourself. There is a smile on your face as your vision slowly fades away...''')
                    enter()
                    print('''Years later, children learn in their textbooks of
the scientist, lead investigator, from WHO. And how he single handedly saved the lives
of millions of people. He prevented the facility from producing the weapons and toxic wires.

He is remembered as a hero.
He is remembered as someone who made the right decision when the time came...

THE END :)''')


intro()
room1()
room2()
room3()
room4()
room5()
end()
