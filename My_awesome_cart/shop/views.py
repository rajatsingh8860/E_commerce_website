from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Contact,Order,orderUpdate,Register
from math import ceil
import json

# Create your views here.
def index(request):
    products=Product.objects.all()
    
    #n=len(products)
    #nSlides=n//4+ceil((n/4)+(n//4))
    #params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    #allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    allProds=[]
    catProds=Product.objects.values('category','id')
    cats={item['category'] for item in catProds}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(products)
        nSlides=n//4+ceil((n/4)+(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={"allProds" : allProds}          
    return render(request,"shop/index.html",params)

def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower() :
        return True
    else:
        return False    


def search(request):
    products=Product.objects.all()
    query=request.GET.get('search')
    allProds=[]
    catProds=Product.objects.values('category','id')
    cats={item['category'] for item in catProds}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n=len(products)
        nSlides=n//4+ceil((n/4)+(n//4))
        if len(prod)!=0:
           allProds.append([prod,range(1,nSlides),nSlides])
    params={"allProds" : allProds,'msg':""}      
    if len(allProds)==0 or len(query)<3:
        params={'msg': "Please make sure to enter relevant search query"}    
    return render(request,"shop/search.html",params)

def about(request):
    return render(request,"shop/about.html")    

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone_no=request.POST.get('phone_no','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone_no=phone_no,desc=desc)
        contact.save()
        thank=True
        return render(request,"shop/contact.html",{'thank':thank}) 
    return render(request,"shop/contact.html")

def tracker(request):
    if request.method=="POST": 
         orderId=request.POST.get('orderId','')
         email=request.POST.get('email','')
         try:
             order=Order.objects.filter(order_id=orderId,email=email)
             if len(order)>0 :
                 update=orderUpdate.objects.filter(order_id=orderId)
                 updates=[]
                 for item in update:
                     updates.append({'text':item.update_desc,'time':item.timestamp})
                     response=json.dumps([updates,order[0].item_json],default=str)
                 return HttpResponse(response)
             else:
                 return HttpResponse('{}')    

         except Exception as e: 
             return HttpResponse('{}')

   
    return render(request,'shop/tracker.html')



def productview(request,myid):
    #fetch the product using id .id is by default created by django as primary key
    product=Product.objects.filter(id=myid)
    return render(request,"shop/productview.html",{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        print(request)
        item_json=request.POST.get('itemJson','')
        amount=request.POST.get('amount','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone_no=request.POST.get('phone_no','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','') 
        zip_code=request.POST.get('zip_code','') 
        order=Order(item_json=item_json,name=name,email=email,phone_no=phone_no,address=address
                    ,city=city,state=state,zip_code=zip_code,amount=amount)
        order.save() 
        update=orderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,"shop/checkout.html",{'thank':thank,'id':id}) 
    return render(request,"shop/checkout.html")


#Register function

def register(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        user_name=request.POST.get('user_name','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        confirm_password=request.POST.get('confirm_password','')

        if Register.objects.filter(email=email).exists():
             welcome=True
             return render(request,"shop/register.html",{'welcome':welcome})

        elif password != confirm_password:
            hello=True     
            return render(request,"shop/register.html",{'hello':hello})

        else:
            welcome=True
            register=Register(first_name=first_name,last_name=last_name,user_name=user_name,email=email,password=password,confirm_password=confirm_password)
            register.save() 
            return render(request,"shop/register.html",{'welcome':welcome})        
    return render(request,"shop/register.html")