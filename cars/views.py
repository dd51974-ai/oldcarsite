from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    return HttpResponse("Hello,world. You're at the cars index.")

from .models import Car
#画像を表示するページ
def showall(request):
    images = Car.objects.all()
    context = {'images':images}
    return render(request, 'cars/showall.html', context)

#アップロード用のview関数
from django.shortcuts import render, redirect
from .models import Car
from .forms import ImageForm

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars:showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'cars/upload.html', context)
