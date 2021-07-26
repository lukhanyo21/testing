from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect

from PIL import Image, ImageEnhance

from .forms import UploadForm

# Create your views here.

@login_required
def pics(request):
    context = {}
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        img = form.cleaned_data['file']
        con = float(form.cleaned_data['contrast'])
        bright = float(form.cleaned_data['brightness'])
        image = Image.open(img)

        if image.format.lower() in ['jpg', 'jpeg']:

            contrast = ImageEnhance.Contrast(image)
            contrast = contrast.enhance(con)
            brightness = ImageEnhance.Brightness(contrast)
            brightness.enhance(bright).save(img.name)

            messages.success(request, 'Image done')
            return redirect('picmix:upload')

        else:
            messages.error(request, 'Hi, jpg and jpeg image accepted')
            return render(request, 'picmix/upload.html', context)

    context['form'] = form
    return render(request, 'picmix/upload.html', context)

