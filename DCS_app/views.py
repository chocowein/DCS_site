from django.shortcuts import render, redirect
from django.http import HttpResponse

from DCS_app import models

def detail(request):
    return HttpResponse("detail page[no data]")
    
def index(request):
    return render(request, "DCS_app/index.html")


from .forms import ImageForm


def upload_image(request):
    if request.method == 'POST':
        image= request.FILES["image"]

        document = models.Image(
            image = image,
        )
        document.save()
        print("アップロード完了")
        return redirect("/")

    documents = models.Image.objects.all()
    return render(request, "DCS_app/index.html" , context = {
        "files": documents
    })