# from django.shortcuts import render,redirect
# from .models import Member
# from .forms import MemberForm
# from django.contrib import messages

# def home(request):
#     all_members=Member.objects.all
#     return render(request, 'home.html' ,{'all':all_members})

# def join(request):
#     if(request.method =="POST"):
#         form=MemberForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#         messages.success(request,('Your form has been submitted successfull!'))
#         return render(request, 'base.html',{})
#         # return redirect('base')

#     else:
#         return  render(request , 'join.html' ,{})
  

from django.shortcuts import render,redirect
from .models import Member
# from .forms import MemberForm
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv 


# from .forms import MemberForm

def home(request):
    all_members=Member.objects.all
    return render(request, 'home.html' ,{'all':all_members})

def join(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST" :
        
        q1 = request.POST['name1']
        q2 = request.POST['name2']
        q3 = request.POST['name3']
        q4 = request.POST['name4']
        q5 = request.POST['email1']
        q6 = request.POST['email2']
        q7 = request.POST['email3']
        q8 = request.POST['email4']
        q9 = request.POST['roll1']
        q10 = request.POST['roll2']
        q11 = request.POST['roll3']
        q12 = request.POST['roll4']
        q13=request.POST['phone1']
        q14=request.POST['phone2']
        q15=request.POST['phone3']
        q16=request.POST['phone4']
        q17=request.POST['tname']
        
        data=Member.objects.create(
        name1=q1,
        name2=q2,
        name3=q3,
        name4=q4,
        email1=q5,
        email2=q6,
        email3=q7,
        email4=q8,
        roll1=q9,
        roll2=q10,
        roll3=q11,
        roll4=q12,
        phone1=q13,
        phone2=q14,
        phone3=q15,
        phone4=q16,
        tname=q17,




        )
        data.save()
        # with open('participants.csv', 'a' ,newline='') as csvfile:
        #             spamwriter=csv.writer(csvfile, delimiter='',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #             data1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]  

        #             spamwriter.writerow(data1)      


        with open('participants1.csv', 'a', newline='') as csvfile:                 
                    spamwriter= csv.writer(csvfile, delimiter=' ',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    data1=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]
    
                    spamwriter.writerow(data1)

        # create a form instance and populate it with data from the request:
        messages.success(request,('Your form has been submitted successfull!'))
        return render(request, 'thanks.html',{})

     
    return render(request, 'join.html',{})   