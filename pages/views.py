from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Produit, Commande, Client, Cart
import os
import google.generativeai as genai

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

def blog(request):
    return render(request,'pages/blog.html')

def blogi(request):
    return render(request,'pages/blogi.html')

def cart(request):
    return render(request,'pages/cart.html', {'cart':Cart.objects.all()})
def total(request):
    x = Cart.objects.all()
    s=0
    for z in x:
        s+=z.prix
    return  render(request,'pages/cartsum.html', {'sum':s})
# def delete(request, id):
#         data = Client.GET.get(id)
#         data.delete()
#     return render(request,'pages/cart.html', {'cart':Cart.objects.all()})
# def delete(request, id):
#     try:
#         client = Client.objects.get(id=id)
#         client.delete()
#     except Client.DoesNotExist:
#         raise Http404("Client does not exist")
#     return redirect('delete')
def delete(request, id):
    if request.method == 'POST':
        pi=Cart.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/cart/')


def checkout(request):
    if request.method == 'POST':
        nom = request.POST.get('firstname')
        prenom = request.POST.get('lastname')
        email = request.POST.get('email')
        paypal = request.POST.get('paypal')
        phone = request.POST.get('phone')
        adresse = request.POST.get('adresse')
        data = Client(nom=nom, prenom=prenom, email=email, paypal=paypal, phone=phone, adresse=adresse)
        data.save()
        pi=Cart.objects.all()
        for x in pi:
            x.delete()
    return render(request,'pages/checkout.html')

# def checkout(request):
#     if request.method == 'POST':
#         nom = request.POST.get('firstname')
#         prenom = request.POST.get('lastname')
#         email = request.POST.get('email')
#         paypal = request.POST.get('paypal')
#         phone = request.POST.get('phone')
#         adresse = request.POST.get('adresse')
#         data = Client(nom=nom, prenom=prenom, email=email, paypal=paypal, phone=phone, adresse=adresse)
#         data.save()
#     return render(request,'pages/checkout.html')


def contact(request):
    return render(request,'pages/contact.html')

def product(request):
    return render(request,'pages/product.html')

def shop(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.all()})


def shopDresses(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.filter(category='Dresses')})
def shopJackets(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.filter(category='Jackets')})
def shopPants(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.filter(category='Pants')})
def shopTshirts(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.filter(category='T-shirts')})
def shopShoes(request):
    return render(request,'pages/shop.html', {'produit':Produit.objects.filter(category='Shoes')})


def connect(request):
    return render(request,'pages/connect.html')


# def add(request, image):
#     if request.method == 'POST':
#         # pi=Produit.objects.get(pk=id)
#         #pi=request.POST.get('ii')
        
#         # pi1=Produit.objects.get(label=pi)
#         # p = Cart(label=Produit(id).label,content=Produit(id).label,prix=Produit(id).prix,image=Produit(id).image,category=Produit(id).category)
#         # p.save()
#         # label = request.POST.get('label')
#         # content = request.POST.get('label')
#         # prix = request.POST.get('prix')
#         # image = request.POST.get('img')
#         # category = request.POST.get('label')
#         label = request.POST.get('label')
#         content = request.POST.get('label')
#         prix = request.POST.get('prix')
#         # image = Produit.objects.get(image=image)
#         category = request.POST.get('label')
#         data = Cart(label=label, content=content, prix=prix, image=image, category=category)
#         data.save()
#         # return HttpResponseRedirect('/shop/')
#         return render(request,'pages/shop.html', {'produit':Produit.objects.all()})
def add(request, id):
    if request.method == 'POST':
        # pi=Produit.objects.get(pk=id)
        #pi=request.POST.get('ii')
        
        # pi1=Produit.objects.get(label=pi)
        # p = Cart(label=Produit(id).label,content=Produit(id).label,prix=Produit(id).prix,image=Produit(id).image,category=Produit(id).category)
        # p.save()
        # label = request.POST.get('label')
        # content = request.POST.get('label')
        # prix = request.POST.get('prix')
        # image = request.POST.get('img')
        # category = request.POST.get('label')
        # prix = request.POST.get('prix')
        # image = Produit.objects.get(image=image)
        tab = Produit.objects.get(pk=id)
        data = Cart(label=tab.label, prix=tab.prix, category=tab.category)
        data.save()
        # return HttpResponseRedirect('/shop/')
        return render(request,'pages/shop.html', {'produit':Produit.objects.all()})
    

def delconn(request):
    if request.method == 'POST':
        pay = request.POST.get('paypal')
        pi=Cart.objects.all()
        cli=Client.objects.all()
        for z in cli:
            if z.paypal==pay:
                for x in pi:
                    x.delete()
                    return render(request,'pages/cart.html')
        
        s="code n'est pas valide"
        return render(request,'pages/connect.html', {'s':s})
    
# def dele(request):
#     if request.method == 'POST':
#         pi=Cart.objects.all()
#         for x in pi:
#             x.delete()

#         return render(request,'pages/checkout.html')




GOOGLE_API_KEY = 'key here'
dt={}

q=" "  
w = Cart.objects.all()
for y in w:
    
    q+=y.label
    q+=":"
    q+=y.category
    q+="    "
   

    print(q)




genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

instruction="in this chat you could be a normal chatbot or we are a clothes web e-commerce app and we want you to do two things, first one,answering any question we have, second one, to give us clothes recommandation when asked and taking in consideration  the category of the clothes in the cart and giving other clothes with the same category from the products , cart({}) , products(glomart white dress:category=dress ,glomart red dress:categorey=dress ,glomart black dress:category=dress ,glomart crazy pant:categorey=pants ,glomart jean:category=pants ,glomart confy pant:categorey=pants ,glomart blue T-shirt:categorey=T-shirts ,glomart whitelue T-shirt:categorey=T-shirts ,glomart red T-shirt:categorey=T-shirts ,glomart shoe:categorey=shoes ,glomart black nike shoe:categorey=shoes ,glomart nike shoe:categorey=shoes ,glomart brown jacket :categorey=jackets ,glomart blue jacket:categorey=jackets ,glomart brown jacket:categorey=jackets)".format(q)

prompt = ""
response = model.generate_content(instruction+prompt)
print(response.text)
print(instruction)


def getresponse(request):
    usermessage = request.GET.get('usermessage')
    response = model.generate_content(usermessage+instruction)

    return HttpResponse(response.text)
