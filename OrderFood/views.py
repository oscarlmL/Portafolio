from django.shortcuts import redirect, render
from django import views
from .models import *


# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def generar_cuenta(request):
    if request.method == 'GET':
        return render(request, 'generarCuenta.html')
    else:
        postData = request.POST
        nom_enc_coc = postData.get('nombre')
        titulo = postData.get('titulo')
        exp_laboral = postData.get('experiencia_laboral')
        email_enc_coc = postData.get('email_enc_cocina')
        contraseña1 = postData.get('contraseña1')
        contraseña2 = postData.get('contraseña2')
        encCocina = EncCocina(nom_enc_coc=nom_enc_coc,
                            titulo=titulo,
                            exp_laboral=exp_laboral,
                            email_enc_coc=email_enc_coc,
                            contraseña1=contraseña1,
                            contraseña2=contraseña2)
        encCocina.cuentaEncargadoCocina()
    return redirect('BUENA')
