##! python3

import sys
from BinarySearchTree import Tree
import os, re

def EuclideanDistance(v1, v2):
    sum =0
    for x in range(len(v1)):
        sum = sum + pow(v1.pop() - v2.pop(), 2)
    sum = pow(sum, 0.5)
    return sum






def frequencyVector(C,F):
    array = []
    #a=[]
    a = C.listOfwords()
    for words in a:
        array.append(wordFrequencyInFile(words, F))
    return array

def combinedList(f1,f2):
    cl = Tree()
    file1 = open(f1).read()
    i = 0
    file1 = str.lower(file1)
    file1 = re.sub(r'[^\w]', ' ', file1)

    for word in file1.split(' '):
        value = value_gen(word)
        cl.insert(value, word, i)
        i += 1
    file2 = open(f2).read()
    i = 0
    file2 = str.lower(file2)
    file2 = re.sub(r'[^\w]', ' ', file2)

    for word in file2.split(' '):
        value = value_gen(word)
        cl.insert(value, word, i)
        i += 1
    return cl



def wordFrequencyInFile(w,f):

    value = value_gen(w)
    v = f.wordfreq(value)
    return v



def value_gen(string):
    i= 0
    sum=0
    if(string!=None):
        for items in string:
            var = ord(items)
            sum = sum + var*pow(9, i)
            i += 1
    return sum


def main():
    c= Tree()

    c = combinedList('a2.txt', 'a3.txt')

    a = frequencyVector(c,'a2.txt')
    print(a)

if __name__=='__main__':
    main()