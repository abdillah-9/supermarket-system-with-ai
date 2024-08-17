from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Users
import re

# Create your views here.

def index(request):
    #fetch all data from Question table and put them in an object
    userAccounts = Users.objects.all()

    #check if submit button is clicked
    if request.method == 'POST' and request.POST.get('submit'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        
        #vars declaration and compile regex
        unameValid = pwordValid ='false'
        regUname =re.compile(r'^[a-zA-Z]+$')
        regPword =re.compile(r'^[a-zA-Z0-9]+$')
        #regPword =re.compile(r'^[a-zA-Z0-9(_)]+$')

        #validate the inputs (uname and pword)
        if(regUname.search(uname)):
            unameValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Only letters are allowed", extra_tags='uErr') 
        if(regPword.search(pword)):
            pwordValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Password must have numbers and letters", extra_tags='pErr') 
        #show errors for wrong inputs
        if(unameValid =='true' and pwordValid=='true'):
            #do something    
            #fetch username and passwords from DB if data are valid
            fetchAccount = Users.objects.filter(username=uname).exists()
            if(uname=='Admin' and pword=='Admin'):
                #redirect administrator
                return redirect('adminHome')

            if(fetchAccount):
                #Check password because the username is valid
                userPassword = authenticate(request, username=uname, passwords=pword)

                if(userPassword is not None):
                    #redirect to patient page coz this user pword and uname are valid
                    return redirect('patientHome')
            
                else:
                    #Password is not correct
                    messages.add_message(request,messages.INFO,"Password is not correct",extra_tags='passwordNot')

            else:    
                #show alert that user name account doesn't exists
                messages.add_message(request,messages.INFO,"Account does not exist", extra_tags='accountNot')            

        
    #redirect to given template
    return render(request, "polls/index.html")

def signUp(request):
    
    #fetch all data from Question table and put them in an object
    userAccounts = Users.objects.all()

    #check if submit button is clicked
    if request.method == 'POST' and request.POST.get('submit'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        cpword = request.POST.get('cpword')
        encryptedpword = make_password(pword) 
        
        #vars declaration and compile regex
        unameValid = pwordValid ='false'
        cpValid = 'true'
        regUname =re.compile(r'^[a-zA-Z]+$')
        regPword =re.compile(r'^[a-zA-Z0-9]+$')
        regCPword =re.compile(r'^[a-zA-Z0-9]+$')

        #validate the inputs (uname, cpword and pword)
        if(regUname.search(uname)):
            unameValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Only letters are allowed", extra_tags='uErr') 
        if(regPword.search(pword)):
            pwordValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Password must have numbers and letters", extra_tags='pErr') 
        if(cpword != pword):
            messages.add_message(request,messages.INFO,"Password and Confirm password fields should match", extra_tags='pErr') 
            cpValid ='false' 

        #show errors for wrong inputs
        if(unameValid =='true' and pwordValid =='true' and cpValid =="true"):
            #do something    
            #fetch username and passwords from DB if data are valid
            fetchAccount = Users.objects.filter(username=uname).exists()
            if(fetchAccount):
                #Check password because the username exists
                userPassword = authenticate(request, username=uname, passwords=pword)
                if(userPassword is not None):
                    #send alert message that user account exists
                    messages.add_message(request,messages.INFO,"Account exists", extra_tags='sErr') 
                else:
                    #save this new account in database
                    insertNewUser = Users(username = uname, passwords = encryptedpword)
                    insertNewUser.save()
                    #redirect to sign In
                    return redirect("../../polls/")            
            else:    
                #save this new account in database
                insertNewUser = Users(username = uname, passwords = encryptedpword)
                insertNewUser.save()
                #redirect to sign In
                return redirect("../../polls/")            

        
    #redirect to given template
    return render(request, "polls/signUp.html")

def patientHome(request):
    return render(request, "polls/patientHome.html")

def adminHome(request):
    return render(request, "polls/adminHome.html")

def signUpCopy(request):
    
    #fetch all data from Users table and put them in an object
    userAccounts = Users.objects.all()

    #check if submit button is clicked
    if request.method == 'POST' and request.POST.get('submit'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')

        #vars declaration and compile regex
        unameValid = pwordValid ='false'
        regUname =re.compile(r'^[a-zA-Z]+$')
        regPword =re.compile(r'^[a-zA-Z0-9]+$')
        #regPword =re.compile(r'^[a-zA-Z0-9(_)]+$')

        #validate the inputs (uname and pword)
        if(regUname.search(uname)):
            unameValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Only letters are allowed", extra_tags='uErr') 
        if(regPword.search(pword)):
            pwordValid = 'true'
        else:
            messages.add_message(request,messages.INFO,"Password must have numbers and letters", extra_tags='pErr') 
        
        #add data to db if user does not exist and viceversa
        if(pwordValid != "true" or unameValid != "true"):
            isValid ="false"
        if(userAccounts.username != uname and userAccounts.passwords != pword):
            #insert user in db
            insertNewUser = Users(username = uname, passwords = pword)
            insertNewUser.save()
            return HttpResponseRedirect('signIn')
        else:
            #alert user that this account exists
            return HttpResponseRedirect('adminHome')

    #redirect to given template/html
    return render(request, "polls/signUp.html")