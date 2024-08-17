from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import re
import os
import numpy as np
from operator import itemgetter 
#Models
from .models import Users
from .models import Assets
from .models import Feedback
from .models import userCart

#for AI
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Create your views here.

def index(request):
    #fetch all data from Question table and put them in an object
    userAccounts = Users.objects.all()

    #check if submit button is clicked
    if request.method == 'POST' and request.POST.get('submit'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        encryptedpword = make_password(pword)
        
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
            fetchAccount = Users.objects.filter(username=uname).exists() #username

            if(uname=='Admin' and pword=='Admin'):
                #redirect administrator
                return redirect('adminHome')

            if(fetchAccount):
                #Check password because the username is valid
                userdata = Users.objects.get(username=uname)
                #then fetch only password from the fetched list
                dbpword = userdata.passwords
                fetchPword= check_password(pword,dbpword)
                if(fetchPword):
                    #redirect to patient page coz this user pword and uname are valid
                    request.session["sessioned_uname"] = uname
                    return redirect('customerHome')
            
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

    #declare variables
    uname=""

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
                #send alert message that user account exists
                messages.add_message(request,messages.INFO,"Account exists", extra_tags='sErr') 
            else:    
                #save this new account in database
                insertNewUser = Users(username = uname, passwords = encryptedpword)
                insertNewUser.save()
                #redirect to sign In
                return redirect("../../polls/")            

        
    #redirect to given template
    user_name = {"user_name":uname}
    return render(request, "polls/signUp.html", user_name)

def customerHome(request):
    #fetch all data from Assets table and put them in an object
    Assets_data = Assets.objects.all()
    if(request.POST.get('submit')):
        if(request.method == "POST"):
            #get posted customer data to save them in respective cart
            p_image = request.POST.get("p_image")
            p_name = request.POST.get("p_name")
            p_price = request.POST.get("p_price")
            p_number = request.POST.get("p_number")
            c_number = request.POST.get("c_number")
            #get username session
            user_nm = request.session["sessioned_uname"]
            #validate c_number from user
            reg=re.compile(r'^[0-9]+$')
            if(reg.search(c_number)):
                #convert strings to number from string
                c_no = int(c_number)
                p_no = int(p_number)
                #check diff btn cno and p_no
                if(p_no > c_no):
                    #put data in the cart DB
                    insertToCart = userCart(p_image=p_image, p_name=p_name, p_price=p_price, c_number=c_number, user_nm=user_nm)
                    insertToCart.save()
                else:
                    #return error that the input should be numbers
                    messages.add_message(request,messages.INFO,"You can't exceed available products' number", extra_tags='cErr') 

            else:
                #return error that the input should be numbers
                messages.add_message(request,messages.INFO,"Only numbers are allowed", extra_tags='cErr') 
        
            
    #Send to html template
    context = {"Assets_data":Assets_data}
    return render(request, "polls/customerHome.html", context)

def feedback(request):
    #check if submit button is clicked
    if(request.method == 'POST' and request.POST.get('submit')):
        #vars declaration and compile regex
        user_feedback = request.POST.get("user_feedback")
        feedbackValid ='false'
        regFeedback =re.compile(r'^[a-z A-Z]+$')
        #get username from sessions
        unamed = request.session["sessioned_uname"]

        #variables validation
        if(user_feedback==""):
            #then generate error message
            messages.add_message(request,messages.INFO,"Please fill this field", extra_tags='fErr') 
        
        else:
            if(regFeedback.search(user_feedback)):
                #save this new feedback message in database
                insertFeedback = Feedback(user_feedback = user_feedback,username = unamed)
                insertFeedback.save()
                
            else:
                #then generate error message
                messages.add_message(request,messages.INFO,"Only letters and white spaces are allowed", extra_tags='fErr') 
               

    return render(request, "polls/feedback.html")
    
def adminHome(request):
    #fetch AI feedback and print them
    fetchFeedbacks = Assets.objects.all()
    productsBought = Assets.objects.values_list('bought_number')
    fetchedF = {"fetchFeedbacks":fetchFeedbacks}
    
    #find maximum purchased product
        #First put the dict in form of single array
    string_array = sorted(productsBought)
        #Then use loop to convert them into int format
    #interger_array = np.array(string_array)
    #interger_array2 = np.array([int(arr) for i in interger_array])   
    #max_purchased_prod = max(interger_array2)
    fetchedF = {"fetchFeedbacks":fetchFeedbacks}

    # ********************** AI MODEL ********************** #
    #define features and target variable
    features = [
    ["red","large"],
    ["green","small"],
    ["red","small"]
    ]
    target_variable = ["apple","lime","strawberry"]

    #Flattern features for encoding
    flattened_features = [item for sublist in features for item in sublist] 

    #use single LabelEncoder for both features and target variable
    le = LabelEncoder()
    le.fit(flattened_features + target_variable)

    #Encode features and target variable
    encoded_features = [le.transform(item) for item in features]
    encoded_target_variable = le.transform(target_variable)

    #Create Cart classifier
    clf = DecisionTreeClassifier()

    #train classifier on training set
    clf.fit(encoded_features, encoded_target_variable)

    #Predict the fruit type for the new instance
    new_instance = ["green","large"]
    encoded_new_instance = le.transform(new_instance)
    predicted_fruit_type = clf.predict([encoded_new_instance])
    decoded_predicted_fruit = le.inverse_transform(predicted_fruit_type)

    #Print the predicted fruit type
    print("Predicted fruit type is: ", decoded_predicted_fruit[0])

    # ********************** AI MODEL ENDING ********************** #

    #then deal with data submition
    if(request.method == 'POST' and request.POST["submit"]):
        #fetch those variables from html temp
        pname = pprice = pnumber = pimage =""
        pname = request.POST["pname"]
        pnumber = request.POST["pnumber"]
        pprice = request.POST["pprice"]
                
        #vars declaration and compile regex
        pnameValid = pnumberValid = ppriceValid = pimageValid ='false'
        regex =re.compile(r'^[a-zA0-Z9\s]+$')
        regex01 =re.compile(r'^[0-9]+$')

        #check if any var is empty
        if(pname !="" and pnumber !="" and pprice !="" and request.FILES["pimage"]):
            #Get file name and extension
            pimage = request.FILES["pimage"]
            #file name
            pimageName = pimage.name

            #file extension
            pimageExtension = pimage.content_type

            #check text inputs with regex
            #start with pname
            if(regex.search(pname)):
                pnameValid = 'true'
            else:
                messages.add_message(request,messages.INFO,"Only letters and white space only", extra_tags='pNameErr') 

            #pnumber
            if(regex01.search(pnumber)):
                pnumberValid = 'true'
            else:
                messages.add_message(request,messages.INFO,"Only numbers are allowed", extra_tags='pNumberErr') 

            #pprice
            if(regex01.search(pprice)):
                ppriceValid = 'true'
            else:
                messages.add_message(request,messages.INFO,"Only numbers are allowed", extra_tags='pPriceErr') 

            #Then check pimage extension
            if(pimageExtension == 'image/jpg' or pimageExtension == 'image/jpeg' or pimageExtension == 'image/png'):
                pimageValid = 'true'
            else:
                messages.add_message(request,messages.INFO," Only jpg, png and jpeg formats are allowed", extra_tags='pExtensionErr') 

            #THEN UPLOAD DATA IF INPUTS ARE VALID
            if(pnameValid =='true' and pnumberValid=='true' and ppriceValid=='true' and pimageValid=='true'):
                #send data in database
                insertAssets = Assets(pname = pname, pnumber = pnumber, pprice = pprice, pimage = pimageName)
                insertAssets.save()
                #send file component in specified folder directory
                fs = FileSystemStorage()
                dir="./polls/static/myproject/imgs/"
                fs.save(dir+pimageName,pimage)
                #send successful message
                messages.add_message(request,messages.INFO,"Products updated successfully", extra_tags='pEmptyErr') 
            
        else:
            #send error message
            messages.add_message(request,messages.INFO,"Please fill all fields", extra_tags='pEmptyErr') 
 
    return render(request, "polls/adminHome.html", fetchedF)

def customerCart(request):
    #fetch all data from userCart table and put them in an object
    Cart_data = userCart.objects.all()
    context = {"Cart_data":Cart_data}
    if(request.method =="POST" and request.POST.get("submit")):
    #if product is bought successful we do three things
        #vars declaration
        p_name = request.POST.get("p_name")
        c_number = int(request.POST.get("c_number"))

        ### First is to reduce the number of goods in Assets table
        Assetsdata = Assets.objects.get(pname=p_name)
        #then fetch the total products number from the fetched list
        old_total = int(Assetsdata.pnumber)
        #then update it and save changes
        Assetsdata.pnumber = old_total-c_number
        Assetsdata.save()

        ### Second is to remove products bought from the userCart table
        remove_bought_product = userCart.objects.get(p_name=p_name)
        remove_bought_product.delete()

        ### Third is to save the number showing how many times the product is bought in Assets table
        #fetch number of products bought from Assets table
        numb_bought = int(Assetsdata.bought_number)
        Assetsdata.bought_number = numb_bought+c_number
        Assetsdata.save()

    #send the object to the html template
    return render(request,"polls/customerCart.html",context)