from django.shortcuts import render, get_object_or_404, redirect
from .models import Division

# ১. সব ডিভিশন লিস্ট আকারে দেখার জন্য
def division_list(request):
    divisions = Division.objects.all()
    return render(request, 'locations/division_list.html', {'divisions': divisions})

# ২. নতুন ডিভিশন যোগ করার জন্য
def division_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            Division.objects.create(name=name)
            return redirect('division_list')
    return render(request, 'locations/division_form.html')

# ৩. ডিভিশন এডিট বা আপডেট করার জন্য
def division_update(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        division.name = request.POST.get('name')
        division.save()
        return redirect('division_list')
    return render(request, 'locations/division_form.html', {'division': division})

# ৪. ডিভিশন ডিলিট করার জন্য
def division_delete(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == "POST":
        division.delete()
        return redirect('division_list')
    return render(request, 'locations/division_confirm_delete.html', {'division': division})