# Task 5 – 5 points
#
# Theory:
# A sample set of rules is given, defined as follows:
#
# ***  **-  *-*  *--  -**  -*-  --*  ---
#  _     *     -     *     *     -     *     -
#  0     1     0     1     1     0     1     0
#
# This is marked as "Rule 90" (binary 01011010), which assigns individual elements 
# to each subsequent group of three elements from a sequence composed of * and _, 
# forming a new sequence (the next generation) in the shown manner.
# A new sequence (next generation) is created based on the previous one.
# The symbol * represents a living cell, while _ represents an empty space.
# A detailed explanation can be found at: 
# https://en.wikipedia.org/wiki/Cellular_automaton in the "Elementary cellular automaton" section.
#
# Program:
# Write a program called automaton, in which:
#
# 1. You define the following parameters:
#    - n: int – the length of the initial chain of cells.
#    - k: int – the number of steps (generations) to calculate.
#    - cels: str – a text string composed of the symbols * and _ representing the initial state.
#    - rule: int – a number from the range 0 to 255, whose binary representation corresponds 
#           to the rule for calculating the next state of the cells.
#
# 2. You calculate the cell states for subsequent generations starting from cels, using the rule.
#
# 3. You display the generations on the screen as a sequence of * and _.

def cellular_automaton(n, k, rule, cels):
    """
    Generates the output table for a 1D cellular automaton based on the binary representation of the rule.
    """
    # Convert the rule to its binary representation
    rule_bin = f"{rule:08b}"  # 8-bit representation
    rule_map = {f"{7-i:b}".zfill(3): int(rule_bin[i]) for i in range(8)}

    # Convert the input string to a list of 0s and 1s
    current_gen = [1 if char == '*' else 0 for char in cels]

    # Print the initial state
    print_generation(current_gen)

    # Iterate through generations
    for _ in range(k):
        # Add 0s at the ends to simulate an infinite chain
        extended_gen = [0] + current_gen + [0]
        next_gen = []

        # Compute the new state based on the rule
        for i in range(n):
            neighborhood = "".join(map(str, extended_gen[i:i+3]))
            next_gen.append(rule_map[neighborhood])

        # Update the state
        current_gen = next_gen
        # Print the new generation
        print_generation(current_gen)


def print_generation(current_gen):
    """
    Helper function to print the current state
    """
    print("".join(['*' if cell else '_' for cell in current_gen]))


n = 21
k = 10
rule = 90
cels = '__________*__________'

cellular_automaton(n, k, rule, cels)
