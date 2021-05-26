from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Query.models import Subscriber, ExtendedUser, Query
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import HomeImage, FeaturedImage, OM, OT
from .forms import HomeImageForm, MealBoxForm, TransFormationForm
from Plans.models import MealBox, TransformationPlan


@staff_member_required(login_url='/login')
def orders(request):
    return render(request, "Admin/orders_menu.html")


@staff_member_required(login_url='/login')
def customers(request):
    customers = ExtendedUser.objects.all()
    return render(request, "Admin/customers.html", {'cust': customers})


@staff_member_required(login_url='/login')
def subscribers(request):
    subs = Subscriber.objects.all()
    return render(request, "Admin/subscribers.html", {'subs': subs})


@staff_member_required(login_url='/login')
def queries(request):
    queries = Query.objects.all()
    return render(request, "Admin/queries.html", {'query': queries})


@staff_member_required(login_url='/login')
def upload(request):
    # queries = Query.objects.all()
    return render(request, "Admin/img_menu.html")


@staff_member_required(login_url='/login')
def viewImage(request, name):
    print(name)
    ogname = name
    if name == "HomeImage":
        plan = HomeImage.objects.all()
        name = "Home Images"
    elif name == "MealBox":
        plan = MealBox.objects.all()
        name = "MealBox Images"
    elif name == "FeaturedImage":
        plan = FeaturedImage.objects.all()
        name = "Featured Images"
    else:
        plan = TransformationPlan.objects.all()
        name = "Transformation Plans Images"
    # plan = name.objects.all()

    return render(request, "Admin/viewimages.html", {'plans': plan, 'Name': name, 'Ogname': ogname})


@staff_member_required(login_url='/login')
def addNewImage(request, name, plan):

    ogname = name
    ogplan = plan
    if name == "HomeImage":
        message = "Width: 1539px Height: 800px"
        pname = HomeImage.objects.filter(name=plan)
        name = "Home Images"
    elif name == "MealBox":
        message = "Width: 392px Height: 280px"
        pname = MealBox.objects.filter(name=plan)
        name = "MealBox Images"
    elif name == "FeaturedImage":
        message = "Width: 270px  Height: 271px"
        pname = FeaturedImage.objects.filter(name=plan)
        name = "Featured Images"
    else:
        message = "Width: 392px Height: 280px"
        pname = TransformationPlan.objects.filter(name=plan)

    if request.method == 'POST':
        print(request.POST['name'])

        if ogname == "HomeImage":
            database = HomeImage.objects.get(name=request.POST['name'])
            database.image = request.FILES['myFile']

            database.save()

        elif ogname == "MealBox":
            database = MealBox.objects.get(name=request.POST['name'])
            database.image = request.FILES['myFile']

            database.save()

        elif ogname == "FeaturedImage":
            database = FeaturedImage.objects.get(name=request.POST['name'])
            database.image = request.FILES['myFile']
            database.save()
        else:
            database = TransformationPlan.objects.get(
                name=request.POST['name'])
            database.image = request.FILES['myFile']
            message = "Width: 392px Height: 280px"
            database.save()
            final = ""
        return redirect('ViewImage', name=ogname)
    return render(request, "Admin/newslide.html", {'plan': pname, 'ogname': ogname, 'ogplan': ogplan, 'size': message})


@staff_member_required(login_url='/login')
def orderForMeals(request):
    orders = OM.objects.all()
 
    return render(request, "Admin/ordersMeal.html", {'orders': orders})


@staff_member_required(login_url='/login')
def orderForTrans(request):
    orders = OT.objects.all()

    return render(request, "Admin/orders.html", {'orders': orders})


@staff_member_required(login_url='/login')
def orderTransEdit(request, orderId):
    order = OT.objects.get(orderId=orderId)
    print(order.user)
    user = ExtendedUser.objects.get(email=order.user)
    contex = {
        'orderId': order.orderId,
        'type': order.type,
        'vegOrJain': order.vegOrJain,
        'total': order.total,
        'status': order.status,
        'name': user.first_name+" "+user.last_name,
        'contact': user.contact
    }
    if request.method == 'POST':
        status = request.POST['status']
        order = OT.objects.get(orderId=orderId)
        order.status = status
        order.save()
        messages.info(request, 'Status changed successfully')
        return redirect('OrderForTrans')

    return render(request, "Admin/orders_form_transform.html", contex)

@staff_member_required(login_url='/login')
def orderMealsEdit(request,orderId):
    order = OM.objects.get(orderId=orderId)
    print(order.user)
    user = ExtendedUser.objects.get(email=order.user)
    contex = {
        'orderId': order.orderId,
        'meal': order.no_of_meal,
        'snack': order.snack,
        'breakfast': order.breakfast,
        'total': order.total,
        'status': order.status,
        'name': user.first_name+" "+user.last_name,
        'contact': user.contact
    }
    if request.method == 'POST':
        status = request.POST['status']
        order = OM.objects.get(orderId=orderId)
        order.status = status
        order.save()
        messages.info(request, 'Status changed successfully')
        return redirect('OrderForMeals')

    return render(request, "Admin/orders_form_mealbox.html", contex)
