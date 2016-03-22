import pickle
import operator

def recbook(course):
    print course+' '+coursenames[course]
    if len(sims[course])<1:
        return "Nothing yet"
    simlist = sims[course]
    totals={}
    counts={}
    recs = {}
    for key in simlist.keys():
        for isbn in ratings[key].keys():
            if isbn in ratings[course]:
                #print 'already read this book '+isbn+' '+booktitles[isbn]
                continue
            rating = str(ratings[key][isbn])
            factor = sims[course][key]
            department=0
            weighted = (int(rating)*factor)+department
            #already saw this book in another record
            if isbn in counts:
                #print key+' isbn '+isbn
                count = counts[isbn]
                #print count
                count=count+1
                counts[isbn]=count
                existing = totals[isbn]
                new = existing+weighted
                #print 'existing '+str(existing)
                #print 'new '+str(new)
                totals[isbn]=new
            #havent seen this yet
            else:
                totals[isbn]=weighted
                counts[isbn]=1
    for key in totals.keys():
        recs[key]=totals[key]/counts[key]
    max = 0
    maxisbn = 0
    if len(recs) >0:
        sorted_x = sorted(recs.iteritems(), key=operator.itemgetter(1))
        sorted_x.reverse()
        print str(sorted_x[0][0])+" "+str(sorted_x[1][0])+" "+str(sorted_x[2][0])+" "+str(sorted_x[3][0])+" "+str(sorted_x[4][0])
        print '\t'+booktitles[sorted_x[0][0]]+' '+sorted_x[0][0]+' '+str(sorted_x[0][1])
        print '\t'+booktitles[sorted_x[1][0]]+' '+sorted_x[1][0]+' '+str(sorted_x[1][1])
        print '\t'+booktitles[sorted_x[2][0]]+' '+sorted_x[2][0]+' '+str(sorted_x[2][1])
        print '\t'+booktitles[sorted_x[3][0]]+' '+sorted_x[3][0]+' '+str(sorted_x[3][1])
        print '\t'+booktitles[sorted_x[4][0]]+' '+sorted_x[4][0]+' '+str(sorted_x[4][1])


ratings = pickle.load( open( "newRatings.p", "rb" ) )
sims = pickle.load( open( "newSims.p", "rb" ) )
coursenames = pickle.load( open( "coursenames.p", "rb" ) )
booktitles = pickle.load( open( "newBookTitles.p", "rb" ) )

recbook("NE200")
