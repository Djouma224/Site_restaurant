from django.urls import reverse
from .models import Card, Commentaires
def cart(request):
    #recuperer le panier de l'utilisateur. la fn ci_dessous renvoi l'objet s'il exite ou renvoie une erreur sinon
    if request.user.is_authenticated:
        cart = Card.objects.get(user = request.user)
        nb = cart.orders.count()
    else:
        nb =0
    context={"nb":nb}# tout les elements de notre panier
    return context

def commentaire(request):
    
    if request.method == 'POST':
        msg = request.POST.get('message')
        com = Commentaires.objects.create(
            message=msg,
            userP=request.user)
        com.save()
    comment = Commentaires.objects.all()
    context = {'comment':comment}
    return context