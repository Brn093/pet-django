from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet 

# Criando as views

@login_required(login_url='/login/')
def set_pet(request):     
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    cidade = request.POST.get('cidade')
    descricao = request.POST.get('descricao')
    foto = request.FILES.get('foto')    
    usuario = request.user
    pet_id = request.POST.get('pet_id')
    
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        
        if usuario == pet.user:
            pet.email = email
            pet.telefone = telefone
            pet.cidade = cidade
            pet.descricao = descricao            
            
            if foto:
                pet.foto = foto
            
                pet.save()
    
    else:
        pet = Pet.objects.create(email=email, telefone=telefone, cidade=cidade, 
                usuario=usuario, descricao=descricao, foto=foto)        
    
    url = '/pet/detail/{}/'.format(pet.id)
        
    return redirect(url)

@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.usuario == request.user:
            
            return render(request, 'register-pet.html', {'pet':pet})
    
    return render(request, 'register-pet.html')

@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    
    if pet.usuario == request.user:
        pet.delete()
        
    return redirect("/")    

@login_required(login_url='/login/')    # acessa apenas a tela de login
def list_all_pets(request):
    pet = Pet.objects.filter(ativo=True)
    
    return render(request, 'list.html', { 'pet' : pet})

@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True, usuario=request.user)
    return render(request, 'list.html', {'pet':pet})

@login_required(login_url='/login/')
def pet_detail(request, id):
    pet = Pet.objects.get(ativo=True, id=id)
    print(pet.id)
    return render(request, 'pet.html', {'pet':pet})

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

def login_user(request):    
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)   # método do django
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválida. Por favor tentar novamente.')
    
    return redirect('/login/')