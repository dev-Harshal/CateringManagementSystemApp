from django.shortcuts import render,redirect
from UserSide.models import *
from django.contrib.auth import login, logout, authenticate
from UserSide.decorators import login_required_custom

# Create your views here.


def indexPage(request):
    return render(request,'index.html')


def homePage(request):
    categories = Category.objects.all()
    return render(request, "home.html",context={'categories':categories})

def optionPage(request,category):
    category_title = Category.objects.get(id=category).title
    options = Option.objects.filter(category=category).all()
    return render(request, 'option.html',context={'category_title':category_title,'options':options})


users_cart = []
def dishPage(request,option):
    option_title = Option.objects.get(id=option).option_title
    dishes = Dish.objects.filter(option=option)
    return render(request, 'dish.html',context={'option_title':option_title,'dishes':dishes,'users_cart':users_cart})

@login_required_custom
def addToCart(request,id):
    cart_items = UsersCartItem.objects.filter(user=request.user).all()
    if cart_items.filter(dish=Dish.objects.filter(id)).exists():
        users_cart.remove(id)
    else:
        users_cart.append(id)
    print(users_cart,"CART")
    return redirect(request.META.get('HTTP_REFERER'))



def extractItems():
        items = Dish.objects.filter(id__in=users_cart).all()
        return items

@login_required_custom
def cartPage(request):
    return render(request,'cart.html',context={'items':extractItems()})


def signupPageView(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if Users.objects.filter(email=email).exists():
            return render(request, "Auth/signup.html")
        if password == re_password:
            user = Users(full_name=str(full_name).title(), email=str(email).lower(), password=password,username=str(email).lower())
            user.save()
            login(request,user)
            from_url = request.GET.get('from')
            if from_url == None:
                return redirect('home-page')
            print(from_url)
            return redirect(from_url)
        else:
            return render(request, "Auth/signup.html")
    return render(request, "Auth/signup.html")

def loginPageView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return render(request, "Auth/login.html")
    return render(request, "Auth/login.html")

def logoutPageView(request):
    logout(request)
    return redirect('index-page')