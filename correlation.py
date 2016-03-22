import scipy as sp
from scipy.stats import pearsonr
import pickle

#load ratings from file
ratings = pickle.load( open( "ratings.p", "rb" ) )

def overlappingbooks(book1, book2):
    count=0
    course1 ={}
    course2 ={}
    for key in book1.keys():
        for key2 in book2.keys():
            if key == key2:
                course1[key]=book1[key]
                course2[key2]=book2[key]
                count = count+1
    return count, course1, course2

key = "DC230"###SET COURSE HERE (a course number)
key2 = "HB250"###SET COURSE HERE (a course number)
counted, course1, course2 = overlappingbooks(ratings[key],ratings[key2])
correlation = pearsonr( sp.array(course1.values()), sp.array(course2.values()) )[0]
print correlation
