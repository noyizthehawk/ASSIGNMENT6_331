#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Assignment 6 Problem 1 Student Solution
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

"""
Problem 1
"""

from sys import flags

def ngramsFreqsFromFile(textFile: str, n: int) -> dict:
    """
    textFile: 'wells.txt'   this will be the string which is a path to the file
    """
    ngram_counts = {}
    
    # Read the file
    with open(textFile, 'r', encoding='utf-8') as file:
        content = file.read()
    
    
    content = content.upper()
    
   
    filtered_content = ''.join(char for char in content if char.isupper() or char == ' ')
    
    
    total_ngrams = 0
    for i in range(len(filtered_content) - n + 1):
        ngram = filtered_content[i:i+n]
        if ngram in ngram_counts:
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
        total_ngrams += 1
    
    
    ngram_freqs = {}
    for ngram, count in ngram_counts.items():
        ngram_freqs[ngram] = count / total_ngrams
    
    return ngram_freqs
    

def test():
    "Run tests"
    import tempfile
    
    
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        temp.write("Hello World! This is a test.")
        temp_name = temp.name
    
    
    unigram_freqs = ngramsFreqsFromFile(temp_name, 1)
    print("Unigram frequencies:")
    for unigram, freq in sorted(unigram_freqs.items()):
        print(f"'{unigram}': {freq:.4f}")
    
   
    bigram_freqs = ngramsFreqsFromFile(temp_name, 2)
    print("\nBigram frequencies:")
    for bigram, freq in sorted(bigram_freqs.items()):
        print(f"'{bigram}': {freq:.4f}")
    
   
    import os
    os.unlink(temp_name)
    
    
    try:
        well_freqs = ngramsFreqsFromFile("wells.txt", 3)
        print("\nTop 5 trigrams from wells.txt:")
        top_trigrams = sorted(well_freqs.items(), key=lambda x: x[1], reverse=True)[:5]
        for trigram, freq in top_trigrams:
            print(f"'{trigram}': {freq:.6f}")
    except FileNotFoundError:
        print("\nNote: wells.txt not found in the current directory")


if __name__ == "__main__" and not flags.interactive:
    test()
