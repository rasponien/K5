from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from .models import Word
from K5.settings import AUDIO_DIR, AUDIO_DIR_NAME, WORDS, FILES
import os
from mutagen.flac import FLAC
import re
import uuid
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def add_words_to_db():
    print("reading files to database")
    for i, file in enumerate(os.listdir(AUDIO_DIR)):
        if file.endswith(".flac"):
            WORDS.insert(
                {
                    "word": FLAC(os.path.join(AUDIO_DIR, file))['title'][0],
                    "pronunciation": FILES.put(open(AUDIO_DIR_NAME + '/' + file, 'rb'), file_name=file)
                }
            )
        if (i == 5):
            break
    print("Done.")


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class FileUpload(View):

    def get(self, request):
        return render(request, "uploadform.html")

    @csrf_exempt
    def post(self, request):
        print("tere")
        if "word" in request.POST and "file" in request.FILES:
            print(AUDIO_DIR_NAME + '/' + str(request.FILES["file"]))
            print(request.POST["word"])
            word = Word(word=request.POST["word"])
            word.pronunciation.put(open(AUDIO_DIR_NAME + '/' + str(request.FILES["file"]), 'rb'),file_name=str(request.FILES["file"]))
            word.save()
            return JsonResponse({"success":True,"msg":"File successfully uploaded"})
        else:
            return JsonResponse({"success":False,"msg":"must contain 'word' and 'file' params and enctype='multipart/form-data'"})


def save_file(file, filename):
    with open(os.path.join(os.path.dirname(__file__), "static","audio_files",filename), "w") as f:
        for chunk in file.chunks():
            f.write(str(chunk))

class WordView(View):
    def get(self, request, searchword):
        for word in WORDS.find():
            file = FILES.get(word["pronunciation"])
            file.read()
            print(file.file_name)


        r = re.compile(searchword + ".*")
        words = Word.objects(__raw__={'word' : {'$regex' : r}})[:5]
        results = {}
        for i, w in enumerate(words):
            #print(w.pronunciation.file_name)
            results[i] = {"word": w.word, "file_name":"/static/audio_files/" + w.pronunciation.file_name, "id":str(w.id)}
        return JsonResponse(results)

