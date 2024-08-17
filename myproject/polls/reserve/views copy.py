from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.

def index(request):
    
    #fetch all data from Question table and put them in an object
    latest_questions = Question.objects.all()

    #check if submit button is clicked
    if request.method == 'POST' and request.POST.get('submit'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        latest_questions_list = Question(question_text = q, pub_date ='2024-04-12')
        latest_questions_list.save()
        return HttpResponseRedirect('signIn')

    # Updating data in database
    # record = Question.objects.get(id = 1)
    # record.question_text = "Is this new question?"
    # record.pub_date = "2024-05-25"
    # record.save(update_fields = ['question_text'],['pub_date'])
    # OR if you wish to update all data in given row just use save() without ...
    # the update_fields =    

    #redirect to given template
    context = {"latest_questions":latest_questions}
    return render(request, "polls/index.html", context)



def indexCopy(request):
    
    #fetch all data from Question table and put them in an object
    latest_questions = Question.objects.all()

    #send data to database
    
    if request.method == 'POST' and request.POST.get('submit'):
        q = request.POST.get('q')
        latest_questions_list = Question(question_text = q, pub_date ='2024-04-12')
        latest_questions_list.save()
        return HttpResponseRedirect('signIn')

    # Updating data in database
    # record = Question.objects.get(id = 1)
    # record.question_text = "Is this new question?"
    # record.pub_date = "2024-05-25"
    # record.save(update_fields = ['question_text'],['pub_date'])
    # OR if you wish to update all data in given row just use save() without ...
    # the update_fields =    

    #redirect to given template
    context = {"latest_questions":latest_questions}
    return render(request, "polls/index.html", context)

def new(request):
    return HttpResponse(       
        "<html>"
        "<head>"
        "<style>"
        "h1{"
            "color: rgb(120,60,30);"
        "}"
        "</style>"
        "</head>"
        "<body>"
        "<h1>Hello Abdi your at the polls index</h1>"
        "<a href='newPage'>Go to this page...</a>"
        "</body>"
        "</html>"
        )
    name = "juma"

