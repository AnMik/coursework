# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from hashlib import md5
from time import localtime

from myapp.models import MyImage
from myapp.forms import MyImageForm


allowed_types = {'jpg', 'gif', 'png', 'bmp', 'jpeg'}


def upload_image(request):
    if request.method == 'POST':

        form = MyImageForm(request.POST, request.FILES)
        if form.is_valid():
            up_file = request.FILES['image']
            print("".join(x for x in up_file.name if x.isalnum()))
            image = MyImage(image=up_file,
                            original_name=up_file.name.rsplit('/', 1),
                            code=md5(str(localtime()).encode('utf-8')).hexdigest()[:20])

            if up_file.name.split('.')[-1] in allowed_types:
                image.save()
                response_redirect = HttpResponseRedirect(
                    reverse('myapp.views.upload_image'))
            else:
                response_redirect = upload_trouble(request, True)

            return response_redirect
    else:
        form = MyImageForm()

    images = MyImage.objects.all()

    return render_to_response(
        'gallery.html',
        {'images': images, 'form': form},
        context_instance=RequestContext(request)
    )


def upload_trouble(request, need_redirect=False):
    print("trouble")

    if need_redirect:
        return HttpResponseRedirect(reverse('myapp.views.upload_trouble'))
    else:
        return render_to_response(
            'upload_trouble.html',
            {},
            context_instance=RequestContext(request))
