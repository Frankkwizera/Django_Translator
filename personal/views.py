from translate import Translator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.staticfiles import storage
from .forms import NameForm
from django.http import HttpResponse

def trans(request):
    if request.method == 'POST':
        inpu = request.POST.get('intext', '')
        translator= Translator(to_lang="fr")
        out = translator.translate(str(inpu))
        print out
        return HttpResponse(out)
    else:
         return render(request, 'personal/header.html')
