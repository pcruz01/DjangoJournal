from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexPageView(request) :
    return render(request, 'homepages/index.html')

def aboutPageView(request) :
    return render(request, 'homepages/about.html')

def genConfPageView(request) :
    context = {
        "type" : "General Conference",
        "background" : "img/conference-center.jpeg"
    }
    return render(request, 'homepages/showJournal.html', context)

def stakeConfPageView(request) :
    context = {
        "type" : "Stake Conference",
        "background" : "img/stake-conference.webp"
    }
    return render(request, 'homepages/showJournal.html', context)

def churchPageView(request) :
    context = {
        "type" : "Church",
        "background" : "img/chapel.jpg"
    }
    return render(request, 'homepages/showJournal.html', context)

def byuPageView(request) :
    context = {
        "type" : "BYU",
        "background" : "img/byu.jpg"
    }
    return render(request, 'homepages/showJournal.html', context)

def missionPageView(request) :
    context = {
        "type" : "Mission",
        "background" : "img/mission.jpg"
    }
    return render(request, 'homepages/showJournal.html', context)