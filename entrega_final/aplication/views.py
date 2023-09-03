from django.shortcuts import render, redirect
from .models import Posteo, Avatar
from .forms import PostForm, RegisterUserForm, UserEditForm, AvatarFormulario
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request): 
    return render(request , "aplication/index.html")

def about(request): 
    return render(request , "aplication/about.html")

def contact(request): 
    return render(request , "aplication/contact.html")

@login_required
def post(request): 
    return render(request , "aplication/post.html")
@login_required
def categories(request): 
    categoria = Posteo.objects.all()
    return render(request,"aplication/categories.html", {'categoria' : categoria } )


#-CRUD-
@login_required
def postForm(request): 
    if request.method == "POST":
        post = Posteo(titulo=request.POST['titulo'],
                      contenido=request.POST['contenido'],
                      fecha=request.POST['fecha'],
                      autor=request.POST['autor'],
                      categorias=request.POST['categorias'])
        post.save()
    return render(request, "aplication/post.html")


@login_required
def updatePost(request, id_post):
    updatePost = Posteo.objects.get(id=id_post)
    if request.method == "POST":
        miForm = PostForm(request.POST)
        if miForm.is_valid():
            updatePost.titulo = miForm.cleaned_data.get('titulo')
            updatePost.contenido = miForm.cleaned_data.get('contenido')
            updatePost.autor = miForm.cleaned_data.get('autor') 
            updatePost.categorias = miForm.cleaned_data.get('categoria') 
            
            updatePost.save()
            return redirect(reverse_lazy('categories'))   
    else:
        miForm = PostForm(initial={
            'titulo': updatePost.titulo,
            'contenido': updatePost.contenido,
            'autor': updatePost.autor,
            'categorias': updatePost.categorias,
        })
    return render(request, "aplication/update_post.html", {'miForm': miForm})

@login_required
def deletePost(request, id_post):
    deletePost = Posteo.objects.get(id=id_post)
    deletePost.delete()
    return redirect(reverse_lazy('categories'))



#-Login-Logout-Registro- 

def userLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                
                
                return render(request, "aplication/index.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplication/login.html", {'form': form, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplication/login.html", {'form': form, 'mensaje': f'Los datos son inválidos'})

    form = AuthenticationForm()      

    return render(request, "aplication/login.html", {"form":form})   

def userRegister(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplication/index.html")
    else:
        form = RegisterUserForm()      
    return render(request, "aplication/register.html", {"form2":form}) 


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplication/index.html")
        else:
            return render(request,"aplication/edit_profile.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplication/edit_profile.html", {'form': form, 'usuario': usuario.username})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

           
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

        
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplication/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplication/agregarAvatar.html", {'form': form })






 




