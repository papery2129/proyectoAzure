from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import prodForm
from .models import comentarios
from .import forms

# Create your views here.
def home(request):
    return render( request, 'app\home.html')

@login_required
def prod(request):
    return render( request, 'app/prod.html')

@login_required
def seg(request):
    return render ( request, 'app/seguns.html')

def acerca(request):
    return render(request, 'app/acerca.html')

def exit(request):
     logout(request)
     return redirect('home')
    

def create(request):
    form = prodForm()
    return render (request, 'app/prod.html', {'form' : form})

@login_required
def form_user_view(request):
    form = forms.FormUser()

    #print(request.method)
    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            print("VALIDADO!")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Email: ", form.cleaned_data['email'])
            print("fecha: ", form.cleaned_data['fecha'])
            print("Text: ", form.cleaned_data['text'])
            comment = comentarios.objects.get_or_create(nombre=form.cleaned_data['nombre'],
                                                     email=form.cleaned_data['email'],
                                                     fecha=form.cleaned_data['fecha'],
                                                     text=form.cleaned_data['text'])[0]
            comment.save()


    return render(request, 'app/formulario.html', {'form' : form})

@login_required
def tabla(request):
    com_list = comentarios.objects.order_by('fecha')
    my_context = {
        'coment' : com_list
        }
    return render(request, 'app/tabla_com.html', context= my_context)