from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Query.models import ExtendedUser, Query, Subscriber
from Plans.models import TransformationPlan, MealBox
from Admin_Dashboard.models import FeaturedImage, HomeImage, OM, OT
# from django.contrib.auth import logout
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login_required


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def home(request):
    if request.user.is_staff:
        auth.logout(request)
        return redirect('Login')

    transformation = TransformationPlan.objects.all()
    featured = FeaturedImage.objects.all()
    h1 = HomeImage.objects.get(name="home1")
    h2 = HomeImage.objects.get(name="home2")
    h3 = HomeImage.objects.get(name="home3")
    return render(request, "index2.html", {'trans': transformation, 'featured': featured,
                                           'home1': h1.image, 'home2': h2.image, 'home3': h3.image})


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print(user)
            auth.login(request, user)
            if username == "admin@gmail.com":
                return redirect("AdminHome")
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('Login')

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if(len(contact) != 10):
            messages.info(request, 'Please Enter Valid Phone Number')
            return redirect('Register')

        if(len(password1) < 6 or len(password2) < 6):
            messages.info(request, 'Password length should be at least 6')
            return redirect('Register')
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('Register')
            else:
                user = User.objects.create_user(
                    username=email, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                newUser = ExtendedUser(username=email, password=password1,
                                       email=email, first_name=first_name, last_name=last_name, user=user,
                                       contact=contact)
                newUser.save()
                return redirect('Login')

        else:
            messages.info(request, 'Password not matching..')
            return redirect('Register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def forgot(request):
    return render(request, "forgot-password.html")


def contactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['number']
        email = request.POST['email']
        query = request.POST['query']
        if(len(contact) != 10):
            messages.info(request, 'Please Enter Valid Phone Number')
            return redirect('Contact')
        queryNew = Query(name=name, contact=contact, email=email, query=query)
        queryNew.save()
        messages.info(request, 'Your Query Has Been Submitted Successfully')
        return redirect('Home')

    return render(request, 'contact2.html')


def meals(request):
    return render(request, 'mealplans.html')


def choosePlans(request):
    return render(request, 'choosePlan.html')


def transformationKnowMore(request, name):
    ogName = name
    transformation = TransformationPlan.objects.filter(name=ogName)
    return render(request, 'transform_knowmore.html', {'tran': transformation})


def mealboxKnowMore(request, name):
    ogName = name
    meal = MealBox.objects.filter(name=ogName)
    return render(request, 'knowmore.html', {'meal': meal})


def transformation(request):
    transformation = TransformationPlan.objects.all()
    return render(request, 'transformation.html', {'trans': transformation})


def mealbox(request):
    meals = MealBox.objects.all()
    return render(request, 'mealbox.html', {'meal': meals})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if not Subscriber.objects.filter(email=email).exists():
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            sub = Subscriber(email=email, created=dt_string)
            sub.save()
            messages.info(request, 'You have been subscribed successfully')
        else:
            messages.info(request, 'This email has already been subscribed')

    return redirect('Home')


def aboutUs(request):
    return render(request, "about-us.html")


@login_required(login_url='Login')
def OrderTransformationPlanDef(request):
    vegorjain = request.POST['vegOrJain']
    type = request.POST['type']
    planName = request.POST['planName']
    total = request.POST['total']
    image = request.POST['image']
    return render(request, 'checkout.html', {'vegOrJain': vegorjain,
                                             'type': type, 'total': total, "image": image, 'planName': planName})


@login_required(login_url='Login')
def checkout(request):
    if request.method == 'POST':
        vegorjain = request.POST['vegOrJain']
        type = request.POST['type']
        total = request.POST['total']
        image = request.POST['image']
        flat = request.POST['flat']
        street = request.POST['street']
        location = request.POST['location']
        pincode = request.POST['pincode']
        add = flat+", "+street+", "+location+", "+pincode
        print(add)
        orderID = "ORDERID"+str(random_with_N_digits(3))
        newOrder = OT(
            type=type, total=total, vegOrJain=vegorjain, user=request.user, orderId=orderID, address=add)
        newOrder.save()
        messages.info(request, 'Your order has been placed successfully')

        return redirect('Home')
    return render(request, 'checkout.html')


@login_required(login_url='Login')
def OrderMealPlan(request):
    meal = request.POST['menu']
    total = request.POST['price']
    image = request.POST['image']
    snack = request.POST['snack']
    planName = request.POST['planName']
    breakfast = request.POST['breakfast']
    # print(snack)
    # print(breakfast)
    return render(request, "checkoutForMeal.html",
                  {'meal': meal, 'total': total, 'planName': planName,
                   "image": image, 'snack': snack, 'breakfast': breakfast})


@login_required(login_url='Login')
def checkOutForMeal(request):
    if request.method == 'POST':
        meal = request.POST['meal']
        total = request.POST['total']
        image = request.POST['image']
        flat = request.POST['flat']
        street = request.POST['street']
        location = request.POST['location']
        pincode = request.POST['pincode']
        snack = request.POST['snack']
        breakfast = request.POST['breakfast']
        add = flat+", "+street+", "+location+", "+pincode
        orderID = "ORDERID"+str(random_with_N_digits(3))
        newOrder = OM(
            no_of_meal=meal, total=total, snack=snack, breakfast=breakfast,  user=request.user, orderId=orderID, address=add)
        newOrder.save()
        messages.info(request, 'Your order has been placed successfully')

        return redirect('Home')
    return render(request, 'checkout.html')


@login_required(login_url='Login')
def myOrders(request):
    return render(request, 'myorders.html')


@login_required(login_url='Login')
def orderForMealsUser(request):
    orders = OM.objects.filter(user=request.user)
    if orders.exists():
        return render(request, "ordersMeal.html", {'orders': orders})
    else:
        messages.info(request, 'No Orders Found')
        return redirect('Home')


@login_required(login_url='Login')
def orderForTransUser(request):
    orders = OT.objects.filter(user=request.user)
    if orders.exists():
        return render(request, "orders.html", {'orders': orders})
    else:
        messages.info(request, 'No Orders Found')
        return redirect('Home')
