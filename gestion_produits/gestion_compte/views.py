from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate # a importer et elle permet de recuperer notre model d'utilisateur pour gerer les utilisateurs dans notre cas ce le model ustilisateurs
from .models import utilisateurs
# User = get_user_model() # permet de rcuperer la classe "utilisateurs"
#fn de creation de compte utilisateur
def singup(request):
    if request.method == "POST":
        # traiter le formulaire
        # recuperer les infos du formulaire de l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        # creer un utilisateurs et le recuperer dans la variable "user"
        user = utilisateurs.objects.create_user(username=username,
                                 password=password,
                                 phone=phone,
                                 email=email,
                                 profile=image                  
                                                               
                                 )
        # if image:
        #     user.profile=image
        # user.save()
        login(request,user) #connecter l'utilisateur il faut import la fonction "login() dans django.contrib.aut"
                #cette fonction a comme parametre request et la variable qui contient l'utilisateur creer precedement "user"
        return redirect('login') # redirige l'utilisateur sur la page de connexion

    return render(request, 'gestion_compte/singup.html')
# fn de deconnexion il faut importer la fn logout
def logout_user(request):
    logout(request)
    return redirect('list_menu')

# fn d'authentification
def login_user(request):
    if request.method == "POST":
        # connecter l'utilisateur
        # recuperer dabord les informations de l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')

        # cette fn permet de verifier que les informations de l'utilisateur sont les bonnes elle est disponible dans meme module que login()
        # la fonction recupère les infos dans la variable "user" pour les manipuler
        user = authenticate(username=username, password=password)
        # si l'authentification a reussi de connecter
        if user:
            login(request,user)
            # ensuite on le redirige vers la page d'accueil 
            return redirect('all_products')


    return render(request, 'gestion_compte/login.html')