from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from .forms import SubirArchivoForm


# Create your views here.
def home(request):
    return render(request, "home.html")


# Para subir archivos crudos a la página web
def subir_archivos(request, *args, **kwargs):

    if request.method == "GET":

        form = SubirArchivoForm()

        return render(request, "dataentry/dataentry.html", {'form': form})

    else:

        form = SubirArchivoForm(request.POST, request.FILES)

        if form.is_valid():

            object = form.save(commit=False)
            object.user = request.user
            object.save()

            return HttpResponseRedirect(reverse("home"))
        
        else:

            message = "Las entradas proporcionadas no son válidas"

            return render(request, "dataentry/dataentry.html", {'form': form,
                                                                'message': message})


# Registrarse
def registro(request, *args, **kwargs):

    if request.method == "POST":

        username = request.POST["username"]
        email =  request.POST["email"]

        ## Confirmación de contraseña
        password = request.POST["password"]
        confirmation =  request.POST["confirmation"]
        if password != confirmation:
            message = "Las contraseñas no coinciden"
            return render(request, "register.html", {"message": message})
        
        ## Corroborar creación del usuario
        try:
            ## Creación de usuario
            object = User.objects.create_user(username, email, password)
            object.save()
            message = "Usuario creado, ahora puede ingresar al proyecto"
            return render(request, "registro.html", {"message": message})
        
            ## Usuario mal creado
        except IntegrityError:
            message = "El usuario no pudo ser creado"
            return render(request, "registro.html", {"message": message})
        
    else:

        ## Entrar a página de registro
        return render(request, "registro.html")


def entrar(request, *args, **kwargs):

    if request.method == "POST":

        username = request.POST["username"]
        contrase = request.POST["password"]
        user = authenticate(request, username=username, password=contrase)

        if user is not None:

            login(request, user)

            return HttpResponseRedirect(reverse("index"))

        else:

            message = "Los datos de proporcionados de usuario no existen"

            return render(request, "entrar.html", {"message": message})
        
    else:

        ## Entrar a página de registro
        return render(request, "entrar.html")


def salir(request, *args, **kwargs):

    logout(request)

    return HttpResponseRedirect(reverse("home"))