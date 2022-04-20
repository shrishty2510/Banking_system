from ast import And
from django.contrib import messages
from django.shortcuts import render

from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import*

# Create your views here.
def Home(request):
    return render(request,'customers/index.html')
# def customers(request):
#     customers = Customer.objects.all()
#     if request.method == "POST":
#         email = request.POST.get('email')
#         senemail = request.POST.get('senemail')
#         amt = request.POST.get('amt')
#         try:
#             amt = intamt1
#         except:
#             print("enter amount")
#         for i in customers:
#             #print(email)
#             if i.email == email:
#                 j = i
#                 id = i.id
#                 break
#         for i in customers:
#             print(i.email,i.avail_bal,senemail)
#             if i.email==senemail and amt< i.avail_bal and amt>0 :
#                 avail_bal = i.avail_bal - amt
#                 avail_bal2 = j.avail_bal + amt
#                 try:
#                     query1 = Transaction(name=i.name, email=i.email,
#                                                 debit_amt=amt ,credit_amt=0 , account_bal=avail_bal)

#                     query2 = Customer(id=i.id, avail_bal=avail_bal, email=i.email
#                                                     , name=i.name)
#                     query3 = Transaction(name=j.name, email=j.email,
#                                                 debit_amt=0 ,credit_amt=amt , account_bal=avail_bal2)
#                     query4 = Customer(id=id, avail_bal=avail_bal2, email=j.email
#                                                     , name=j.name)
#                     query2.save()
#                     query1.save()
#                     query4.save()
#                     query3.save()
                    
#                     return redirect('/customers')
#                 except:
#                     print("transection failed")
#                     break
#         else:
#             print("invalid data")
#     return render(request,'customers/customers.html',{'customers':customers})
def customers(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        senemail = request.POST.get('senemail')
        amt = request.POST.get('amt')
        email = request.POST.get('email')
        if amt == '' :
               messages.error(request,'please enter valid amount!!')
               redirect('/customers')
        elif amt: 
            amt1=int(amt)
            for i in customers:
                    if senemail != i.email:
                        messages.error(request,'Email does not exist!!')
                        break
                    else:
                        for i in customers:        
                            if i.email==senemail and amt1 < i.avail_bal and amt1>0 :
                                print(i,amt1)
                                avail_bal1 = i.avail_bal-amt1
                                print(avail_bal1)
                                query1=Customer(id=i.id,name=i.name,email=i.email,avail_bal=avail_bal1)
                                query2=Transaction(name=i.name,email=i.email,credit_amt=0,debit_amt=amt1,account_bal=avail_bal1)   
                                query1.save()
                                query2.save()
                                break
                        for i in customers:
                            if i.email==email and amt1>0:
                                avail_bal2 = i.avail_bal+amt1
                                print(avail_bal2)
                                query3=Customer(id=i.id,name=i.name,email=i.email,avail_bal=avail_bal2)
                                query4=Transaction(name=i.name,email=i.email,credit_amt=amt1,debit_amt=0,account_bal=avail_bal2)   
                                query3.save()
                                query4.save()   
                                messages.success(request,'Transaction done successfully!!')
                                HttpResponseRedirect('/customers/')
        else:
            print("invalid data")
    return render(request,'customers/customers.html',{'customers':customers})      
                    






def trans(request):
    trans = Transaction.objects.all()
    return render(request,'customers/transactions.html',{'trans':trans})