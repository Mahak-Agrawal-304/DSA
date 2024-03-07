from logic import *

Aknight = Symbol("A is a Knight")
Aknave = Symbol("A is a Knave")

Bknight = Symbol("B is a Knight")
Bknave = Symbol("B is a Knave")

Cknight = Symbol("C is a Knight")
Cknave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(Aknight,Aknave),
    Biconditional(Aknight,And(Aknave,Aknight)) 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(Aknave,Aknight),
    Or(Bknave,Bknight),
    Biconditional(Aknight,And(Aknave,Bknave)),
    Biconditional(Aknave,Bknight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(Aknave,Aknight),
    Or(Bknave,Bknight),
    Biconditional(Aknight,And(Aknight,Bknight)),
    Biconditional(Aknave,Bknight),
    Biconditional(Bknight,And(Bknight,Aknave)),
    Implication(Bknave,Aknave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(Aknave,Aknight),
    Or(Bknave,Bknight),
    Or(Cknave,Cknight),
    Biconditional(Aknight,Or(Aknight,Aknave)),
    Biconditional(Bknight,(Implication(Aknight,Aknave))),
    Biconditional(Bknave,(Implication(Aknight,Aknight))),
    Biconditional(Bknave,Cknight),
    Biconditional(Bknight,Cknave),
    Biconditional(Cknight,Aknight),
    Biconditional(Cknave,Aknave)
)


def main():
    symbols = [Aknight, Aknave, Bknight, Bknave, Cknight, Cknave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
