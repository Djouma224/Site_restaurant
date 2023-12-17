# from django.shortcuts import  get_object_or_404
# from .models import Card
# def cart(request):
#     #recuperer le panier de l'utilisateur. la fn ci_dessous renvoi l'objet s'il exite ou renvoie une erreur sinon
#     cart = get_object_or_404(Card, user=request.user)
#     nb = cart.orders.count()
#     context={"orders":cart.orders.all(),"nb":nb}# tout les elements de notre panier
#     return context