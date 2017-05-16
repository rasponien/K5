from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse, FileResponse
from .models import Word
from K5.settings import AUDIO_DIR, AUDIO_DIR_NAME, WORDS, FILES
import os
from mutagen.flac import FLAC
import re, json
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
        return render(request, "static/angular_templates/upload.html")

    @csrf_exempt
    def post(self, request):
        """
        :param request-POST param:"word","file",["force"]: 
        :return Json response: 
        """

        if "word" in request.POST and "pronunciation" in request.FILES:
            file = request.FILES["pronunciation"]
            #if word is already in database:
            if Word.objects.filter(word=request.POST["word"]).count() > 0:

                # Is change forced?
                if "force" in request.POST and request.POST["force"] == "on":

                    #Change is forced
                    word = Word.objects.get(word=request.POST["word"])
                    word.pronunciation.replace(file)
                    word.save()
                    return JsonResponse({"msg":"File successfully modified"})
                else:
                    # Not forced
                    return JsonResponse({"msg":"File already exists in the database."})
            else:
                # If file not in database, add it
                word = Word(word=request.POST["word"])
                word.pronunciation.put(file)
                word.save()
                return JsonResponse({"msg":"File successfully uploaded"})
        else:
            return JsonResponse({})


def save_file(file, filename):
    with open(os.path.join(os.path.dirname(__file__), "static","audio_files",filename), "w") as f:
        for chunk in file.chunks():
            f.write(str(chunk))

class WordView(View):
    def get(self, request, searchword):
        r = re.compile(searchword)
        #print(WORDS.find({'word' : r}))
        words = Word.objects(__raw__={'word' : {'$regex' : r}})[:5]
        print(words)
        results = {}
        for i, w in enumerate(words):
            #print(w.pronunciation.file_name)
            results[i] = {"word": w.word, "id":str(w.id)}
        return JsonResponse(results)


def get_sound(request):
    if "id" not in request.GET:
        return JsonResponse({"success":False,"msg":"'id' param is not in request"})
    word = Word.objects.get(id=request.GET["id"])
    print(word.word)
    print(word.pronunciation)
    sound = word.pronunciation
    return FileResponse(sound)