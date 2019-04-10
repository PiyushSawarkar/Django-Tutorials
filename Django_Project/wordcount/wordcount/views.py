from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #return HttpResponse("<p>Home Page</p>")
    return render(request,'home.html')
def count(request):
    data=request.GET['fulltextarea']
    l=data.split()
    c=0
    m=set(l)
    occ=0
    # n=[]
    # for i in m:
    #     occ=0
    #     for j in l:
    #         if i==j:
    #             occ+=1
    #     n.append([i,occ])
    dictionary_of_word={}
    for a_word in l:
        if a_word in dictionary_of_word:
            dictionary_of_word[a_word]+=1
        else:
            dictionary_of_word[a_word]=1
    length = len(l)
    sortlist=sorted(dictionary_of_word.items(),key=operator.itemgetter(1),reverse=True)
    #reverse = True is used for decending order...
    #if not given then ascending ...
    #or you can also use len=len(l) . . . that gives length...
    return render(request,'count.html',{'word_count':length,'occurences':sortlist})

def about(request):
    return render(request,'about.html')
