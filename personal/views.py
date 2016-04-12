from translate import Translator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.staticfiles import storage
from .forms import NameForm
from django.http import HttpResponse

def trans(request):
    return render(request, 'personal/header.html')

def gosl(request):
    inpu = request.POST.get('intext', '')
    print "THis is inpu: "
    print inpu
    #go = input("enter your text here")
    translator= Translator(to_lang="fr")
    out = translator.translate(str(inpu))
    # file = open("newfile.txt", "w")
    # file.write(out)
    # file.close()
    print out 
       
    return HttpResponse(out)

def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'personal/answer.html',{'form':form})
