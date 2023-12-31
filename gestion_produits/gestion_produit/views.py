#from django.http import JsonResponse

from django.shortcuts import render,get_object_or_404,redirect
from .models import Produits,Categorie,Card,Order,Commentaires
from django.urls import reverse 


# Fontion pour afficher tout les produits
def list_menu(request):
    donnees = Produits.objects.all()
    cat = Categorie.objects.all()
    context = {'donnees':donnees,'cat':cat}
   
    return render(request, 'gestion_produit/index_2.html',context)


# Fontion pour afficher les details d'un produit
def detail_produit(request,my_id):
    var = get_object_or_404(Produits,pk=my_id)
    contexte = {'var':var}
    # pour les commentaires


    return render(request,'gestion_produit/single-product.html',contexte)

# fonction permettant d'afficher tout les produits dans all_products.html
def all_products(request):
    donnees = Produits.objects.all()
    context = {'donnees':donnees}


    return render(request, 'gestion_produit/all.html',context)

# afficher les plats
def plats(request):
    donnees = Produits.objects.filter(categorie__nom_categorie='Plats')
    context = {'donnees':donnees}

    return render(request,'gestion_produit/plats.html',context)

# afficher les boissons du restaurant
def boissons(request):
    donnees = Produits.objects.filter(categorie__nom_categorie='boissons')
    context = {'donnees':donnees}
    return render(request,'gestion_produit/boissons.html',context)

# afficher les dessert du restaurant
def desserts(request):
    donnees = Produits.objects.filter(categorie__nom_categorie='desserts')
    context = {'donnees':donnees}
    return render(request,'gestion_produit/desserts.html',context)

# afficher les produits rechercher dans recherche.html
def recherche(request):
    if request.method == 'GET':
        var = request.GET.get("search")
        produit =Produits.objects.filter(nom__icontains=var)|Produits.objects.filter(categorie__nom_categorie__icontains=var)
        context = {'produit':produit}
    return render(request,'gestion_produit/recherche.html',context)

def contact(request):
    
    return render(request,'gestion_produit/contact.html')

def apropos(request):
    
    return render(request,'gestion_produit/about.html')

    # fonction pour les commentaires
def commentaire(request):
    
    # if request.method == 'POST':
    #     msg = request.POST.get('message')
    #     com = Commentaires.objects.create(
    #         message=msg,
    #         userP=request.user)
    #     com.save()
    #     return reverse('list_menu')
    # comment = Commentaires.objects.all()
    # context = {'comment':comment}
    return render(request,'gestion_produit/msg.html')

    

#voit les commentaire
# def view_comment(request):
#     comment = Commentaires.objects.all()
#     return reverse('list_menu')

def add_to_card(request,my_id):
    # recuperer notre utilisateur
    user =request.user
    # recuperer le produit
    product = get_object_or_404(Produits,id=my_id)
    # recuperer le panier de l'utilisateur s'il exite ou le créer sinon
    #elle a besoin de 2 variable la methode retourne 2 elements elle va returner dans "cart" l'objet en question qu'il a été créer ou qu'il exite déjà et
    #retourne dans une 2em variable une information pournon savoir si l'objet à été créer ou non elle va nous servir si l'objet est déja ajouté dans le panier de l'incrémenté
    #par convention on met (_) signifie que la la 2em variable ne sera pas utiliser  
    cart, _ = Card.objects.get_or_create(user=user)
    # recuperer l'élement qui va être dans notre panier  
    order, crated = Order.objects.get_or_create(user=user,
                                                product=product)
    # si l'objet est créer. c'st le cas ou si l'element n'exitait pas dans le panier donc il faut l'ajouter
    if crated:
        cart.orders.add(order)
        cart.save()# sauvegarder le panier
    else:
        order.qte += 1
        order.save()
    return redirect(reverse("list_menu"))


# fn qui affiche le panier de l'utilisateur
def cart(request):
    #recuperer le panier de l'utilisateur. la fn ci_dessous renvoi l'objet s'il exite ou renvoie une erreur sinon
    cart = get_object_or_404(Card, user=request.user)
    # panier = Order.objects.filter(user=request.user)
    # total = sum(product.prix for product in panier.product.all())
    context={"orders":cart.orders.all()}# tout les elements de notre panier
    return render(request, 'gestion_produit/cart.html',context)

# fn pour supprimer un produit dans le panier
def del_prod_card(request,my_id):
    product_del = product_del = get_object_or_404(Order,id=my_id)
    product_del.delete()
    return redirect('cart')
