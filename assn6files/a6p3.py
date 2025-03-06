#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Assignment 6 Problem 3 Student Solution
# Version 1.0
# Copyright Janurary 2025 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Problem 3
"""

from sys import flags


'''
Use this section to implement your code from A6P2 
-- alternativly you can import your file but make sure to import the entire module
    Sometimes using import from your own files can cause issues in the grading script


def keyScore(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> float:
    raise NotImplementedError()
'''



def bestSuccessor(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> dict:
    raise NotImplementedError()

def breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB):
    """
    Break the tie between two successor mappings that have the same keyscore

    originalMapping: mapping the the other parameters are successors to
    successorMappingA: mapping that has had two keys swapped
    successorMappingB: mapping that has had two other keys swapped

    Example usage:
    originalMapping = {"A": "A", "B": "B", "C": "C"}
    # Mapping with B and C switched
    successorMappingA = {"A": "A", "B": "C", "C": "B"}
    # Mapping with A and C switched
    successorMappingB = {"A": "C", "B": "B", "C": "A"}

    # AC < BC so this function will return successorMappingB
    assert breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB) == successorMappingB
    """
    aSwapped = "".join(sorted(k for k, v in (
        set(successorMappingA.items()) - set(originalMapping.items()))))
    bSwapped = "".join(sorted(k for k, v in (
        set(successorMappingB.items()) - set(originalMapping.items()))))
    return successorMappingA if aSwapped < bSwapped else successorMappingB

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C"}, {"A": "A", "B": "C", "C": "B"}, {
                            "A": "C", "B": "B", "C": "A"}) == {"A": "C", "B": "B", "C": "A"}
    assert breakKeyScoreTie({"A": "A", "B": "B", "C": "C", "D": "D"}, {
                            "A": "B", "B": "A", "C": "C", "D": "D"}, {"A": "A", "B": "B", "C": "D", "D": "C"}) == {"A": "B", "B": "A", "C": "C", "D": "D"}

if __name__ == "__main__" and not flags.interactive:
    test()