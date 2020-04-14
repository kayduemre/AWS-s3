from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import boto3
from botocore.exceptions import ClientError
import logging
from .form import Fileform
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .form import Fileform
from django.views.generic import(
    TemplateView,
)

def home_page(request):
    bucket_object_key_list = []
    contex = {}
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('selfbox')
    for bucket_obj in bucket.objects.all():
        file_url = 'https://selfbox.s3.eu-central-1.amazonaws.com/%s' % (bucket_obj.key)
        bucket_object_key_list.append(file_url)

        str(bucket_object_key_list)[1:-1]
    contex['obj'] = bucket_object_key_list

    return render(request, 'home_page.html', contex)
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = 'https://selfbox.s3.eu-central-1.amazonaws.com/%s' % (filename)
        #version = request.POST['versioning']
        s3 = boto3.resource('s3')
       
        s3.Bucket('selfbox').put_object(Key=filename, Body=filename)

        return render(request, 'input.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'input.html')

def delete(request):
    bucket_object_key_list = []
    contex = {}
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('selfbox')
    for bucket_obj in bucket.objects.all():
        bucket_object_key_list.append(bucket_obj.key)
    contex['form'] = bucket_object_key_list

    if request.method == 'POST' and len(bucket_object_key_list) != 0:
        form = request.POST['value']
        s3.Object('selfbox', form).delete()
        return render(request, 'successalert.html')
    return render(request, 'delete.html', contex, )
