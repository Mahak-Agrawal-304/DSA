import termcolor
from logic import *

harry = Symbol("Mr. Harry is the murderer")
raj = Symbol("Prof. Raj is the murderer")
mark = Symbol("Col. Mark is the murderer")
Names = [harry, raj, mark]  # List of names for the symbols

hallroom = Symbol("Hallroom is the murder venue")
kitchen = Symbol("Kitchen is the murder venue")
bedroom  = Symbol( "Bedroom is the murder venue" )
Place = [ hallroom, kitchen, bedroom ]   # List of possible murder venues

knife = Symbol("Knife is the murder weapon")
gun = Symbol("Gun is the murder weapon")
sword = Symbol("Sword is the murder weapon")
Weapon = [ knife, gun, sword ]          # List of possible weapons

symbols = Names + Place + Weapon

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge,symbol):
            termcolor.cprint(f"{symbol} : Yes","green")
        elif not model_check(knowledge,Not(symbol)):
            termcolor.cprint(f"{symbol} : Maybe")
        

# basic rules/knowledge of clue game
knowledge = And(
    Or(harry, raj, mark),
    Or(hallroom, kitchen, bedroom),
    Or(knife, gun, sword)
)

# additional knowledge added as  per clues given in the game
knowledge.add(Not(harry))
knowledge.add(Not(knife))
knowledge.add(Or(
    Not(mark),
    Not(bedroom),
    Not(gun)
))
knowledge.add(Not(raj))
knowledge.add(And(
    Not(knife),
    Not(bedroom),
    Not(harry)
))
knowledge.add(Or(
    bedroom,
    Not(sword)
))
knowledge.add(Not(hallroom))

# running the function
check_knowledge(knowledge)
