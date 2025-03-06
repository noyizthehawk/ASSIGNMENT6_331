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


def breakKeyScoreTie(originalMapping, successorMappingA, successorMappingB):
    aSwapped = "".join(sorted(k for k, v in (
        set(successorMappingA.items()) - set(originalMapping.items()))))
    bSwapped = "".join(sorted(k for k, v in (
        set(successorMappingB.items()) - set(originalMapping.items()))))
    return successorMappingA if aSwapped < bSwapped else successorMappingB


def bestSuccessor(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> dict:
    original_score = keyScore(mapping, ciphertext, frequencies, n)
    
    best_successor = mapping
    best_score = original_score
    
    swappable_chars = [char for char in mapping.keys() if char != ' ']
    
    for i in range(len(swappable_chars)):
        for j in range(i + 1, len(swappable_chars)):
            char1 = swappable_chars[i]
            char2 = swappable_chars[j]
            
            successor = mapping.copy()
            successor[char1], successor[char2] = successor[char2], successor[char1]
            
            successor_score = keyScore(successor, ciphertext, frequencies, n)
            
            if successor_score > best_score:
                best_successor = successor
                best_score = successor_score
            elif successor_score == best_score and successor != mapping:
                best_successor = breakKeyScoreTie(mapping, best_successor, successor)
    
    return best_successor


def test():
    original_mapping = {char: char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "}
    
    frequencies = {"AB": 0.5, "BA": 0.1, "AC": 0.05}
    
    ciphertext = "ABACAB"
    
    original_score = keyScore(original_mapping, ciphertext, frequencies, 2)
    
    swapped_mapping = original_mapping.copy()
    swapped_mapping['B'], swapped_mapping['C'] = swapped_mapping['C'], swapped_mapping['B']
    swapped_score = keyScore(swapped_mapping, ciphertext, frequencies, 2)
    
    best = bestSuccessor(original_mapping, ciphertext, frequencies, 2)
    
    print("Original mapping score:", original_score)
    print("Swapped B/C mapping score:", swapped_score)
    
    if swapped_score > original_score:
        print("Expected: Best successor should swap B and C")
    else:
        print("Expected: Original mapping should be the best")
    
    if best == swapped_mapping and swapped_score > original_score:
        print("Test passed: Best successor correctly swapped B and C")
    elif best == original_mapping and original_score >= swapped_score:
        print("Test passed: Original mapping correctly identified as best")
    else:
        print("Test failed: Unexpected best successor found")
        
    frequencies = {"AB": 0.5, "BA": 0.5, "BC": 0.5, "CB": 0.5}
    ciphertext = "ABCBA"
    
    successor1 = original_mapping.copy()
    successor1['A'], successor1['B'] = successor1['B'], successor1['A']
    
    successor2 = original_mapping.copy()
    successor2['B'], successor2['C'] = successor2['C'], successor2['B']
    
    score1 = keyScore(successor1, ciphertext, frequencies, 2)
    score2 = keyScore(successor2, ciphertext, frequencies, 2)
    
    print("\nTie-breaking test:")
    print("Successor 1 (swap A/B) score:", score1)
    print("Successor 2 (swap B/C) score:", score2)
    
    expected_winner = breakKeyScoreTie(original_mapping, successor1, successor2)
    
    best_with_tie = bestSuccessor(original_mapping, ciphertext, frequencies, 2)
    
    if best_with_tie == expected_winner:
        print("Tie-breaking test passed: Correct successor chosen in tie")
    else:
        print("Tie-breaking test failed: Wrong successor chosen in tie")


if __name__ == "__main__" and not flags.interactive:
    test()