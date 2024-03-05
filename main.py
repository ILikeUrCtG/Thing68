#NOT AI program

import random
import time
import mpmath


seconds = 2

def delay():
    time.sleep(seconds)


def half_delay():
    time.sleep(seconds/2)


def quick_delay():
    time.sleep(seconds/8)


def long_delay():
    time.sleep(seconds * 2)


def enter():
    print("\n")

# study_tier = ['mind maps', 'active recall', 'reading notes', 'question banks', 'making notes', 'anki', 'rewatching lectures', 'pomodoro technique', 'spaced repetition', 'study with music', 'past papers', 'online videos', 'rote learning', 'teaching others']

# ost = ['images', 'acronyms and mnemonics', 'connect the information to something you already know well', 'say the information out loud', "teach other people what you've learned", 'use colors', 'draw tables and diagrams', 'flashcards']




print(f'============================{topic}============================')

while len(abilities) != 0:
    cross = input('')
    if cross in abilities:
        del(abilities[abilities.index(cross)])
    else:
        exit()

print('====================Study Techniques Tier List===================')
while len(study_tier) != 0:
    cross = input('')
    if cross in study_tier:
        del(study_tier[study_tier.index(cross)])
    else:
        exit()
print('===========================SMART Goals===========================')
while len(smart) != 0:
    cross = input('')
    if cross in smart:
        del(smart[smart.index(cross)])
    else:
        exit()

print('===============Other Study Techniques (in order)=================')
while len(ost) != 0:
    cross = input('')
    if cross == ost[0]:
        del(ost[0])
    else:
        exit()
print('======================Career Decision Making Process=====================')
while len(cdmp) != 0:
    cross = input('')
    if cross in cdmp:
        del(cdmp[cdmp.index(cross)])
    else:
        exit()
print('Hooray! You did it!')
