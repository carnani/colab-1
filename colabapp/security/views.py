from django.shortcuts import render
from security.forms import StudentForm
from django.contrib.auth.models import Permission

# Create your views here.
def v_signup(request):
    if request.method == "POST":
        data = request.POST.copy() # Tomo todos los datos del frontend
        data['username'] = data['email'] # Alteramos previamente

        form = StudentForm(data) # Comparo con el backend
        if form.is_valid(): # Valido
            us = form.save()# Se guarda en base de datos

            us.is_staff = True # Doy mas capacidades a ese registro de db
            us.is_active = True # Doy mas capacidades a ese registro de db
            us.set_password(data['password']) # Se cifra la contraseña
            us.save() # Se vuelve a guardar la bd
            perm = Permission.objects.get(name = "Can add subscription")
            us.user_permissions.add(perm) # Asignamos permiso

        else:
            print(">>", form.errors)

    context ={}
    return render(request, 'signup.html', context)