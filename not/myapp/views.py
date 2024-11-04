from django.shortcuts import render, redirect, HttpResponse
from ultralytics import YOLO
import os
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File
from .forms import ImageForm, CustomUserForm, CustomAuthentication
from .models import Images, ImagesModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def upload_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            model_path = os.path.join(settings.BASE_DIR, 'Best.pt')
            model = YOLO(model_path)
            # image_instance.user = request.user
            # image_instance.save()
            results = model.predict(
                source=f'D:\coding\\Not\\not\media\{image_instance.img}',
                save=True,
                project='D:\coding\\Not\\not\\results',
                name='',
                exist_ok=True
            )
            folder_path = 'D:\coding\\Not\\not\\results\predict'
            image_name = str(image_instance.img)[7:]
            print(image_name)
            image_path = os.path.join(folder_path, image_name)
            print(image_path)

            if os.path.exists(image_path):
                image_model_instance = ImagesModel()
                image_model_instance.image = image_instance  # Устанавливаем связь с Images
                if not request.user.is_authenticated:
                    user = User.objects.get(username='if_not_auth')
                    image_model_instance.user = user
                else:
                    image_model_instance.user = request.user

                with open(image_path, 'rb') as f:
                    image_model_instance.img_model.save(image_name, File(f), save=True)
                print('#################')

                image_model_instance.save()  # Сохраняем экземпляр ImagesModel

            image = Images.objects.get(img=f'images/{image_name}')

            image_model = ImagesModel.objects.get(image=image)
            # print('user = ', type(request.user))
            # user_model = ImagesModel.objects.filter(user=request.user)
            # print(user_model)
            return render(request, 'index.html', {'form': form, 'image_model': image_model, 'image': image})
    else:
        form = ImageForm()
        return render(request, 'index.html', {'form': form})


def UserCreation(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            aunt = authenticate(username=user, password=password)
            login(request, aunt)
            return redirect('index')
        else:
            return render(request, 'UserCreationForm.html', {'form': form})
    else:
        form = CustomUserForm()
        return render(request, 'UserCreationForm.html', {'form': form})


def Authenticate(request):
    if request.method == 'POST':
        form = CustomAuthentication(request.POST, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            aunt = authenticate(username=user, password=password)
            login(request, aunt)
            return redirect('index')
        else:
            print('#####################')
            print('Error')
            return render(request, 'AuthenticationForm.html', {'form': form})
    else:
        form = CustomAuthentication()
        return render(request, 'AuthenticationForm.html', {'form': form})


def _logout(request):
    logout(request)
    return redirect('index')


def personal_account(request):
    user_img = ImagesModel.objects.filter(user=request.user)
    contex = {
        'show_footer': True,
        'user_img': user_img
    }
    return render(request, 'personal_account.html', contex)

