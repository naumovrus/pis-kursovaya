from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.http import require_safe, require_http_methods

from .forms import CustomerForm, ProductsForm, Deal, Barter
from .models import Customer, Products


# TODO: add delete user and delete product from DB


def index(request):
    return render(request, 'index.html')


def del_product(request, id):
    prod = Products.objects.filter(id=id)
    prod.delete()
    return redirect('ProductInfo')


def del_customer(request, id):
    cust = Customer.objects.filter(id=id)
    cust.delete()
    return redirect('CustomerBase')


def addProduct(request):
    error = ''
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ProductInfo')
        else:
            error = 'Неверно заполненная форма'

    form = ProductsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'addproduct.html', data)


def addclient(request):
    error = ''
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Неверно заполненная форма'

    form = CustomerForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'addclient.html', data)


def CustomerBase(request):
    data = Customer.objects.all()
    return render(request, 'clientbase.html', {'data': data})


def ProductInfo(request):
    data = Products.objects.all()
    return render(request, 'productbase.html', {'data': data})


def CheckCustomer(request):
    data = Customer.objects.all()
    return render(request, 'checkclient.html', {'data': data})


def MakeDeal(request):
    return render(request, 'makedeal.html')


def cash(request):
    if request.method == 'POST':
        form = Deal(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['cust']
            prod = form.cleaned_data['prod']
            if cust.cust_balance >= prod.price and prod.prod_amount:
                cust.cust_balance -= prod.prod_cost
                cust.amount_of_purchases += prod.prod_cost
                prod.prod_amount -= 1
                cust.save()
                prod.save()
                return redirect('index')
            else:
                return HttpResponse('Недостаточно средств')
    else:
        form = Deal()
    return render(request, 'cash.html', {'form': form})


def realcash(request):
    if request.method == 'POST':
        form = Deal(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['cust']
            prod = form.cleaned_data['prod']
            if prod.prod_amount:
                cust.amount_of_purchases += prod.prod_cost
                prod.prod_amount -= 1
                cust.save()
                prod.save()
                return redirect('index')
            else:
                return HttpResponse('Товара нет на складе')
    else:
        form = Deal()
    return render(request, 'realcash.html', {'form': form})


def credit(request):
    if request.method == 'POST':
        form = Deal(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['cust']
            prod = form.cleaned_data['prod']
            if prod.prod_amount and cust.cust_ceiling >= prod.cost:
                prod.prod_amount -= 1
                cust.amount_of_purchases += prod.prod_cost
                cust.credit_ceiling -= prod.price
                cust.client_debt += prod.cost
                cust.save()
                prod.save()
                return redirect('index')
            else:
                return HttpResponse('Ошибка')
    else:
        form = Deal()
    return render(request, 'credit.html', {'form': form})


def barter(request):
    if request.method == 'POST':
        form = Barter(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['cust']
            homeproduct = form.cleaned_data['homeprod']
            clientproduct = form.cleaned_data['clientprod']
            if homeproduct.prod_cost - clientproduct.prod_cost < 0:
                if cust.cust_balance >= homeproduct.prod_cost - clientproduct.prod_cost:
                    homeproduct.prod_amount -= 1
                    clientproduct.prod_amount += 1
                    cust.cust_balance += homeproduct.prod_cost - clientproduct.prod_cost
                    cust.save()
                    homeproduct.save()
                    clientproduct.save()
                    return redirect('index')
                else:
                    return HttpResponse('Недостаточно средств')
            else:
                homeproduct.prod_amount -= 1
                clientproduct.prod_amount += 1
                cust.client_count += homeproduct.prod_cost - clientproduct.prod_cost
                cust.save()
                homeproduct.save()
                clientproduct.save()
                return redirect('index')
    else:
        form = Barter()
    return render(request, 'barter.html', {'form': form})


def netting(request):
    if request.method == 'POST':
        form = Deal(request.POST)
        if form.is_valid():
            cust = form.cleaned_data['cust']
            prod = form.cleaned_data['prod']
            if cust.cust_debt >= prod.prod_cost:
                cust.client_debt -= prod.price
                cust.cust_ceiling += prod.price
                prod.prod_amount += 1
                cust.save()
                prod.save()
                return redirect('index')
            else:
                return HttpResponse('Не достаточно кредита')
    else:
        form = Deal()
    return render(request, 'netting.html', {'form': form})
