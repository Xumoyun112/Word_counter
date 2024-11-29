from django.shortcuts import render
from django.http import HttpResponse


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file', None)
        if not uploaded_file:
            return HttpResponse("Iltimos, fayl yuklang.", status=400)

        file_content = uploaded_file.read().decode('utf-8')

        words = file_content.split()
        word_count = len(words)

        return render(request, 'upload.html', {'word_count': word_count, 'words': words})

    return render(request, 'upload.html')
