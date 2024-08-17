from django.db import models
from django.utils import timezone

# Create your models/DB tables here.

#table users
class Users(models.Model):
    username = models.CharField(max_length=50)
    passwords = models.CharField(max_length=50) 
    def __str01__(self):
        return self.username
    def __str02__(self):
        return self.passwords

#table Assets
class Assets(models.Model):
    pname = models.CharField(max_length=100)
    pprice = models.CharField(max_length=50)
    pnumber = models.CharField(max_length=50)
    pimage = models.CharField(max_length=100)
    bought_number = models.CharField(max_length=100, default="0")
    def __str01__(self):
        return self.pname
    def __str02__(self):
        return self.pprice
    def __str03__(self):
        return self.pnumber
    def __str04__(self):
        return self.pimage
    def __str05__(self):
        return self.bought_number

#table userCart
class userCart(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.CharField(max_length=50)
    p_image = models.CharField(max_length=100)
    c_number = models.CharField(max_length=50)
    user_nm = models.CharField(max_length=50)
    def __str01__(self):
        return self.p_name
    def __str02__(self):
        return self.p_price
    def __str04__(self):
        return self.p_image    
    def __str03__(self):
        return self.c_number
    def __str05__(self):
        return self.user_nm
#table feedback
class Feedback(models.Model):
    user_feedback = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    def __str01__(self):
        return self.user_feedback
    def __str02__(self):
        return self.username
#table Predictions
class Fitness(models.Model):
    ex1 = models.CharField(max_length=100)
    ex2 = models.CharField(max_length=100)
    ex3 = models.CharField(max_length=100)
    ex4 = models.CharField(max_length=100)
    ex5 = models.CharField(max_length=100)
    ex6 = models.CharField(max_length=100)
    ex7 = models.CharField(max_length=100)
    ex8 = models.CharField(max_length=100)
    ex9 = models.CharField(max_length=100)
    ex10 = models.CharField(max_length=100)
    ex11 = models.CharField(max_length=100)
    ex12 = models.CharField(max_length=100)
    ex13 = models.CharField(max_length=100)
    ex14 = models.CharField(max_length=100)
    ex15 = models.CharField(max_length=100)
    ex16 = models.CharField(max_length=100)
    ex17 = models.CharField(max_length=100)
    ex18 = models.CharField(max_length=100)
    ex19 = models.CharField(max_length=100)
    ex20 = models.CharField(max_length=100) 
    ex21 = models.CharField(max_length=100)
    ex22 = models.CharField(max_length=100)
    ex23 = models.CharField(max_length=100)
    ex24 = models.CharField(max_length=100)
    ex25 = models.CharField(max_length=100)
    ex26 = models.CharField(max_length=100)
    ex27 = models.CharField(max_length=100)
    ex28 = models.CharField(max_length=100)
    ex29 = models.CharField(max_length=100)
    ex30 = models.CharField(max_length=100)
    ex31 = models.CharField(max_length=100)
    ex32 = models.CharField(max_length=100)
    ex33 = models.CharField(max_length=100)
    ex34 = models.CharField(max_length=100)
    ex35 = models.CharField(max_length=100)
    ex36 = models.CharField(max_length=100)
    ex37 = models.CharField(max_length=100)
    ex38 = models.CharField(max_length=100)
    ex39 = models.CharField(max_length=100)
    ex40 = models.CharField(max_length=100)
    ex41 = models.CharField(max_length=100)
    ex42 = models.CharField(max_length=100)
    ex43 = models.CharField(max_length=100)
    ex44 = models.CharField(max_length=100)
    ex45 = models.CharField(max_length=100)
    ex46 = models.CharField(max_length=100)
    ex47 = models.CharField(max_length=100)
    ex48 = models.CharField(max_length=100)
    ex49 = models.CharField(max_length=100)
    ex50 = models.CharField(max_length=100)
    ex51 = models.CharField(max_length=100)
    ex52 = models.CharField(max_length=100)
    ex53 = models.CharField(max_length=100)
    ex54 = models.CharField(max_length=100)
    ex55 = models.CharField(max_length=100)
    ex56 = models.CharField(max_length=100)
    ex57 = models.CharField(max_length=100)
    ex58 = models.CharField(max_length=100)
    ex59 = models.CharField(max_length=100)
    ex60 = models.CharField(max_length=100)
    ex61 = models.CharField(max_length=100)
    ex62 = models.CharField(max_length=100)
    ex63 = models.CharField(max_length=100)
    ex64 = models.CharField(max_length=100)
    ex65 = models.CharField(max_length=100)
    ex66 = models.CharField(max_length=100)
    ex67 = models.CharField(max_length=100)
    ex68 = models.CharField(max_length=100)
    ex69 = models.CharField(max_length=100)
    ex70 = models.CharField(max_length=100)
    ex71 = models.CharField(max_length=100)
    ex72 = models.CharField(max_length=100)
    ex73 = models.CharField(max_length=100)
    ex74 = models.CharField(max_length=100)
    ex75 = models.CharField(max_length=100)
    ex76 = models.CharField(max_length=100)
    ex77 = models.CharField(max_length=100)
    ex78 = models.CharField(max_length=100)
    ex79 = models.CharField(max_length=100)
    ex80 = models.CharField(max_length=100)
    ex81 = models.CharField(max_length=100)
    def __str01__(self):
        return self.ex1
    def __str02__(self):
        return self.ex2
    def __str03__(self):
        return self.ex3
    def __str04__(self):
        return self.ex4
    def __str05__(self):
        return self.ex5
    def __str06__(self):
        return self.ex6    
    def __str07__(self):
        return self.ex7
    def __str08__(self):
        return self.ex8
    def __str09__(self):
        return self.ex9
    def __str10__(self):
        return self.ex10
    def __str011__(self):
        return self.ex11
    def __str012__(self):
        return self.ex12
    def __str013__(self):
        return self.ex13
    def __str014__(self):
        return self.ex14
    def __str015__(self):
        return self.ex15
    def __str016__(self):
        return self.ex16    
    def __str017__(self):
        return self.ex17
    def __str018__(self):
        return self.ex18
    def __str019__(self):
        return self.ex19
    def __str20__(self):
        return self.ex20            
    def __str021__(self):
        return self.ex21
    def __str022__(self):
        return self.ex22
    def __str023__(self):
        return self.ex23
    def __str024__(self):
        return self.ex24
    def __str025__(self):
        return self.ex25
    def __str026__(self):
        return self.ex26    
    def __str027__(self):
        return self.ex27
    def __str028__(self):
        return self.ex28
    def __str029__(self):
        return self.ex29
    def __str30__(self):
        return self.ex30
    def __str031__(self):
        return self.ex31
    def __str032__(self):
        return self.ex32
    def __str033__(self):
        return self.ex33
    def __str034__(self):
        return self.ex34
    def __str035__(self):
        return self.ex35
    def __str036__(self):
        return self.ex36    
    def __str037__(self):
        return self.ex37
    def __str038__(self):
        return self.ex38
    def __str039__(self):
        return self.ex39
    def __str40__(self):
        return self.ex40
    def __str041__(self):
        return self.ex41
    def __str042__(self):
        return self.ex42
    def __str043__(self):
        return self.ex43
    def __str044__(self):
        return self.ex44
    def __str045__(self):
        return self.ex45
    def __str046__(self):
        return self.ex46    
    def __str047__(self):
        return self.ex47
    def __str048__(self):
        return self.ex48
    def __str049__(self):
        return self.ex49
    def __str50__(self):
        return self.ex50
    def __str051__(self):
        return self.ex51
    def __str052__(self):
        return self.ex52
    def __str053__(self):
        return self.ex53
    def __str054__(self):
        return self.ex54
    def __str055__(self):
        return self.ex55
    def __str056__(self):
        return self.ex56    
    def __str057__(self):
        return self.ex57
    def __str058__(self):
        return self.ex58
    def __str059__(self):
        return self.ex59
    def __str60__(self):
        return self.ex60
    def __str061__(self):
        return self.ex61
    def __str062__(self):
        return self.ex62
    def __str063__(self):
        return self.ex63
    def __str064__(self):
        return self.ex64
    def __str065__(self):
        return self.ex65
    def __str066__(self):
        return self.ex66    
    def __str607__(self):
        return self.ex67
    def __str068__(self):
        return self.ex68
    def __str069__(self):
        return self.ex69
    def __str70__(self):
        return self.ex70
    def __str071__(self):
        return self.ex71
    def __str072__(self):
        return self.ex72
    def __str073__(self):
        return self.ex73
    def __str074__(self):
        return self.ex74
    def __str075__(self):
        return self.ex75
    def __str076__(self):
        return self.ex76    
    def __str077__(self):
        return self.ex77
    def __str078__(self):
        return self.ex78
    def __str079__(self):
        return self.ex79
    def __str80__(self):
        return self.ex80
    def __str81__(self):
        return self.ex81