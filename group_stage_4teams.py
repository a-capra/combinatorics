from scipy.special import perm
from itertools import permutations
# k-permutations of n
# ordered arrangements in which no element occurs more than once, 
# but without the requirement of using all the elements from a given set.
# this involves considering arrangements of a fixed length k of elements
# taken from a given set of size n, in other words, these k-permutations 
# of n are the different ordered arrangements of a k-element subset of an n-set 
# (sometimes called variations or arrangements in the older literature). 
# These objects are also known as partial permutations.
# The number of such k-permutations of n
# is given by the product: n*(n-1)*(n-2)...(n-k+1)
# these are k factors
# n!/(n-k)!

def generate_match(teams):
    temp=permutations(teams,2)
    return list(temp)

def generate_standings(matches,fixtures):
    standings={ i : 0 for i in teams}
    for i in zip(matches,fixtures):
        #print(i)
        if i[1] == '1': standings[i[0][0]]+=3
        elif i[1] == '2': standings[i[0][1]]+=3
        else: 
            standings[i[0][0]]+=1
            standings[i[0][1]]+=1
    return standings

from permutations_with_repetition import *
import os

if __name__=='__main__':

    teams=['a','b','c','d']
    print('Number of teams:',len(teams))
    print('Number of matches played:',perm(len(teams),2))
    matches=generate_match(teams)
    
    results=['1','X','2']
    string=''.join(results)

    conf=allLexicographic(string,sequence=len(matches))
    print('Number of possible scenarios:',len(conf))
    fname=os.path.realpath(__file__)+'output.txt'
    with open(fname, 'w') as f: 
        f.write('''Possible standings of 4 teams in a round robin tournament
        when they can tie\n''')
    for i,cf in enumerate(conf):
        fixtures=[s for s in cf]
        standings=generate_standings(matches,fixtures)
        res={key: val for key, val in sorted(standings.items(), key = lambda ele: ele[1], reverse = True)} 
        with open(fname, 'a') as f:
            f.write(f'{i:6d}----------------------------\n')
            for t in res: f.write(f'{t}.....{res[t]:2d}\n')
            f.write('----------------------------------\n')
        #for t in res: print(f'{t}.....{res[t]:2d}')
        #print('----------------------------------')

#for x in stand_1: print(f'{x}...{stand_1[x]}') 
