from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the file here (e.g., save it, read its contents, etc.)
            # For now, we'll just redirect to a success page
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            return HttpResponseRedirect(reverse('upload_success'))
    else:
        form = FileUploadForm()
    return render(request, 'App/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'App/upload_success.html')
