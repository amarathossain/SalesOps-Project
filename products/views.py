import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Division, Zone, Area, Route, Outlet
from django.contrib.auth.models import User

def product_dashboard(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        try:
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():
                Product.objects.create(
                    name=row['Name'],
                    price=row['Price'],
                    stock=row['Stock']
                )
            messages.success(request, 'Data updated successfully!')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('dashboard')

    products = Product.objects.all().order_by('-created_at')
    return render(request, 'base.html', {'products': products})

def product_content(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'product_table.html', {'products': products})

def user_content(request):
    users = User.objects.all()
    return render(request, 'user_list_content.html', {'users': users})

def division_content(request):
    divisions = Division.objects.all()
    return render(request, 'division_list.html', {'divisions': divisions})

def zone_content(request):
    zones = Zone.objects.all()
    return render(request, 'zone_list.html', {'zones': zones})

def area_content(request):
    areas = Area.objects.all()
    return render(request, 'area_list.html', {'areas': areas})

def route_content(request):
    routes = Route.objects.all()
    return render(request, 'route_list.html', {'routes': routes})

def outlet_content(request):
    outlets = Outlet.objects.all()
    return render(request, 'outlet_list.html', {'outlets': outlets})