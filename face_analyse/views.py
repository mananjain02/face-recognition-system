from django.shortcuts import render
from django.http import HttpResponse
# from face_unlock.project_files import face_unlock

# Create your views here.
def index(request):
    # face = face_unlock.face_recog
    face = False
    if face:
        return render(request, 'face_analyse/index.html')
    else:
        return render(request, 'face_analyse/entrydenied.html')