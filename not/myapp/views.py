from django.shortcuts import render
from ultralytics import YOLO
import os
from django.conf import settings
from django.core.files import File
from .forms import ImageForm
from .models import Images, ImagesModel


def upload_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            image_instance = form.save()
            model_path = os.path.join(settings.BASE_DIR, 'Best.pt')
            model = YOLO(model_path)
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

                with open(image_path, 'rb') as f:
                    image_model_instance.img_model.save(image_name, File(f), save=True)

                image_model_instance.save()  # Сохраняем экземпляр ImagesModel

            image = Images.objects.get(img=f'images/{image_name}')

            image_model = ImagesModel.objects.get(image=image)


            return render(request, 'index.html', {'form': form, 'image_model': image_model, 'image': image})
    else:
        form = ImageForm()
        return render(request, 'index.html', {'form': form})
