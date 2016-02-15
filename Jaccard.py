import numpy as np

# open and read in data
with open('starWarsWordBag.csv', 'r') as crawls:
    newHope = np.array(crawls.readline().split(','))
    empire = np.array(crawls.readline().split(','))
    jedi = np.array(crawls.readline().split(','))

def jaccardIndex(A,B):
  A = set(A)
  B = set(B)
  num = len(A.intersection(B))
  return  (float(num) / (len(A) + len(B) - num))

dis1 = jaccardIndex(newHope, empire)### define Jaccard Index function
dis2 = jaccardIndex(newHope, jedi)
dis3 = jaccardIndex(empire, jedi)

print dis1
print dis2
print dis3

def jaccardDistance(A,B):
  A = set(A)
  B = set(B)
  num = len(A.intersection(B))
  return 1 - (float(num) / (len(A) + len(B) - num))
