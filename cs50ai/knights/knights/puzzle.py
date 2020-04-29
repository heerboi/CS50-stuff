from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave") 

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Cannot be both a knight and a knave but one of those
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # If A is a knight (not lying), then his statement is correct
    Implication(AKnight, And(AKnight, AKnave)),
    # Else, his statement is false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)
    
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Cannot be both a knight and a knave but one of those
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # If A is a knight (not lying), then A and B both are knaves, but then A would be lying
    Implication(AKnight, And(AKnave, BKnave)),
    # So, if A is a knave, then B has to be a knight because both of them cannot be knaves
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# If A is telling the truth, then they're both knaves or knights
# If they're both knaves, then A would be lying, so they aren't both knaves
# If they're both knights, then B's statement would be incorrect, so they aren't both knaves
# Which proves that A's statement is incorrect, hence A is a knave
# If A is a knave, then B is a knight because they have to be different
knowledge2 = And(
    # Cannot be both a knight and a knave but one of those
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # If A is a knight or B is a knave, then they're both either Knights or Knaves
    Implication(Or(AKnight, BKnave), Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If B is a knight or A is a knave, then A is a knight and B is knave or B is knight and A is knave
    Implication(Or(BKnight, AKnave), Or(And(AKnight, BKnave), And(AKnave, BKnight)))
) 

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# If A is a knight then he is a knight, if not, all his statements are incorrect
# If B says A said it is a knave, B is lying because if A was a knight,  it would say it is a knight and if A was a knave
# it would still say it is a knight as he has to be lying,
# So, B is a knave.
# Hence, C cannot be a knave, and so, C is a knight
knowledge3 = And(
    # Cannot be both a knight and a knave but one of those
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # If A is a knight, then it doesn't matter what he said, he has to be a knight
    Implication(AKnight, AKnight),
    # If A is a knave, however, whatever he said would be incorrect, meaning if he said he is a knight
    # then it is false, as he has to be lying
    Implication(AKnave, Not(Or(AKnave, AKnight))),
    # If B is a knight, and A is a knight, then A is a knave, or A is a knight and C is a knave
    Implication(BKnight, And(Or(Implication(AKnight, AKnave), Implication(AKnave, AKnight)), CKnave)),
    # If B is a knave, and A is a knight, then A is a knight or he is a Knave and C is a knight
    Implication(BKnave, And(Or(Implication(AKnight, AKnight), Implication(AKnave, AKnave)), CKnight)),
    # If C is a knight, then A is a knight
    Implication(CKnight, AKnight),
    # If C is a knave, then A is a knave
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
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
