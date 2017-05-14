from django.shortcuts import render
from django.views.generic.base import View
from .models import Word
from K5.settings import AUDIO_DIR, AUDIO_DIR_NAME
import os
from mutagen.flac import FLAC

# Create your views here.

def addWordsToDB():
    print("reading files to database")
    for file in os.listdir(AUDIO_DIR):
        if (file.endswith(".flac")):
            print("file:    " + AUDIO_DIR_NAME + '/' + file)
            word = Word(word=FLAC(os.path.join(AUDIO_DIR, file))['title'][0])
            word.pronunciation.put(open(AUDIO_DIR_NAME + '/' + file, 'rb'), file_name=file)
            word.save()
    print("Done.")




class IndexView(View):

    def get(self, request):
        return render(request, 'index.html', {'words' : Word.objects()[:5]})