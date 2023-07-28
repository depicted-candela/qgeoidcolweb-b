from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import SubirArchivo
from .forms import SubirArchivoForm


# Inicio de la aplicación
def home(request):
    return render(request, "home.html")


class RecibirDatosReactViewSet(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):

        user = User.objects.last()
        name = request.data['nombre']
        file = request.FILES.get("archivo")
        tipo = request.data['tipo']
        detalles = request.data['detalle']
        SubirArchivo.objects.create(user=user, name=name, file=file,
                                    tipo=tipo, detalles=detalles)
        
        return Response('Datos recibidos')


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

            print(object)

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

            return HttpResponseRedirect(reverse("home"))

        else:

            message = "Los datos de proporcionados de usuario no existen"

            return render(request, "entrar.html", {"message": message})
        
    else:

        ## Entrar a página de registro
        return render(request, "entrar.html")


def salir(request, *args, **kwargs):

    logout(request)

    return HttpResponseRedirect(reverse("home"))