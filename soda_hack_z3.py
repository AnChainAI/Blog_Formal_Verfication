#!/usr/bin/env python3

'''
Soda.Finance Smart Contract Hack Z3 Formal Verification Script.
AnChain.AI 2020/10/1
'''

__author__ = 'Tianyi Zhang'
__copyright__ = 'Copyright 2020, AnChain.AI'
__credits__ = ['Tianyi Zhang', 'Reviewer:Tomo', 'Reviewer:Victor']

# to run this script, install Z3 first by running 'sudo pip3 install z3-solver'
from z3 import *

# check the buggy version
def checkBuggy(amount, interest, factor):
    s = Solver()
    # add constraints to variables
    s.add([amount >= 0, interest >= 0])
    s.add([factor > 0, factor < 1])
    loanTotal = amount + interest
    maximumLoan = amount * factor
    # negate statement to prove that no solution exists to satisfy loanTotal < maximumLoan
    s.add(loanTotal < maximumLoan)
    return s.check()

# check the fixed version
def checkFixed(amount, interest, factor, lockedAmount):
    s = Solver()
    # add constraints to variables
    s.add([amount >= 0, interest >= 0, lockedAmount >= 0])
    s.add([factor > 0, factor < 1])
    loanTotal = amount + interest
    maximumLoan = lockedAmount * factor
    # negate statement to prove that solutions exist to satisfy loanTotal < maximumLoan
    s.add(loanTotal < maximumLoan)
    return s.check()

# initialize symbolic variables
amount = Int('amount')
interest = Int('interest')
lockedAmount = Int('lockedAmount')
factor = Real('factor')
# print solver result: unsat and sat
print(checkBuggy(amount, interest, factor))
print(checkFixed(amount, interest, factor, lockedAmount))
