from django.urls import path
from gestion_produit.views import list_menu,all_products,detail_produit,plats,boissons,desserts,recherche,contact,apropos,add_to_card,cart,view_comment
urlpatterns = [
    # url pour affihcer les details d'un produit
    path('detail_produit/<int:my_id>/',detail_produit,name='detail_produit'),
    # url pour ajouter un prodduit au panier
    path('detail_produit/add_to_card<int:my_id>',add_to_card,name='add_to_card'),
    # url pour afficher tout les produits dans index2
    path('',list_menu,name='list_menu'),
    # url du panier
    path('cart/',cart,name='cart'),
    # url pour afficher tout les produits dans all
    path('all_products',all_products,name='all_products'),
    # url pour afficher la categorie plats
    path('plats',plats,name='plats'),
    # url pour afficher la categorie boissons
    path('boissons',boissons,name='boissons'),
    # url pour afficher la categorie desserts
    path('desserts',desserts,name='desserts'),
    # url pour afficher les recherches
    path('recherche',recherche,name='recherche'),
    # url pour les commentaires
    # path('commentaire/',commentaire,name='commentaire'),
    # url pour voir les commentaires
    path('view_comment/',view_comment,name='view_comment'),
    path('contact',contact,name='contact'),
    path('apropos',apropos,name='apropos'),
    # path('detail',ind,name='detail'),

     

    
]