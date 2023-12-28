from django.shortcuts import render
from PIL import Image
import os
from django.conf import settings
import datetime
from django.http import HttpResponse
from .models import MyFile


# !!!!!!!  Method to save image at a remote folder!   !!!!!


# def app(request):
#     if request.method == "GET":
#         return render(request, "index.html")
#     elif request.methot == "POST":
#         file = request.FILES.get("my_file")
#         img = Image.open(file)
#         img_resized = img.resize((200, 200))
#         path = os.path.join(
#             settings.BASE_DIR,
#             f"media/{datetime.datetime.now()}-{file.name}"
#         )
#         img = img_resized.save(path)

#         return HttpResponse("Imagem salva com Sucesso!")


def app(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        image_name = "{}-{}".format(datetime.datetime.now(), file.name)

        img = MyFile(image_name=image_name, image_url=file)
        img.save()

        return HttpResponse("Imagem salva com Sucesso!")