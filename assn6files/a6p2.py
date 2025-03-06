#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Assignment 6 Problem 2 Student Solution
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
#---------------------------------------------------------------
from sys import flags
def keyScore(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> float:

    
    decipherment = ''
    for char in ciphertext:
        if char in mapping:
            decipherment += mapping[char]
        else:
           
            decipherment += char
    
    
    ngram_counts = {}
    for i in range(len(decipherment) - n + 1):
        ngram = decipherment[i:i+n]
        if ngram in ngram_counts:
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
    
   
    score = 0.0
    for ngram, count in ngram_counts.items():
        
        frequency = frequencies.get(ngram, 0.0)
        score += count * frequency
    
    return score


def test():
    """Run tests for the keyScore function"""
    
    ciphertext = "EEFFFEEF"
    frequencies = {"EE": 0.5, "EF": 0.2, "FE": 0.3}
    
   
    identity_mapping = {char: char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "}
    
   
    score = keyScore(identity_mapping, ciphertext, frequencies, 2)
    expected_score = (2 * 0.5) + (2 * 0.2) + (1 * 0.3)  # Occurrences: EE(2), EF(2), FE(1), FF(2 but frequency is 0)
    
    print(f"Example test case:")
    print(f"Ciphertext: {ciphertext}")
    print(f"Calculated score: {score}")
    print(f"Expected score: {expected_score}")
    print(f"Test {'passed' if abs(score - expected_score) < 0.000001 else 'failed'}\n")
    
    
    swap_mapping = identity_mapping.copy()
    swap_mapping['E'] = 'F'
    swap_mapping['F'] = 'E'
    
    
    swapped_score = keyScore(swap_mapping, ciphertext, frequencies, 2)
    
    expected_swapped = (2 * 0.5) + (2 * 0.3) + (1 * 0.2)  
    print(f"Swapped mapping test case:")
    print(f"Ciphertext: {ciphertext}")
    print(f"Calculated score with swapped E/F: {swapped_score}")
    print(f"Expected score: {expected_swapped}")
    print(f"Test {'passed' if abs(swapped_score - expected_swapped) < 0.000001 else 'failed'}")


if __name__ == "__main__" and not flags.interactive:
    test()



