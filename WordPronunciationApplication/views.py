from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from .models import Word
from K5.settings import AUDIO_DIR, AUDIO_DIR_NAME
import os
from mutagen.flac import FLAC
import re


# Create your views here.

def add_words_to_db():
    print("reading files to database")
    for file in os.listdir(AUDIO_DIR):
        if file.endswith(".flac"):
            print("file:    " + AUDIO_DIR_NAME + '/' + file)
            word = Word(word=FLAC(os.path.join(AUDIO_DIR, file))['title'][0])
            word.pronunciation.put(open(AUDIO_DIR_NAME + '/' + file, 'rb'), file_name=file)
            word.save()
    print("Done.")


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')



class WordView(View):
    def get(self, request, searchword):
        print(searchword)
        r = re.compile(".*" + searchword + ".*")
        words = Word.objects(__raw__={'word' : {'$regex' : r}})[:5]
        results = {}
        for i, w in enumerate(words):
            print(w.pronunciation.file_name)
            results[i] = {"word": w.word, "file_name":"/static/audio_files/" + w.pronunciation.file_name}
        return JsonResponse(results)

