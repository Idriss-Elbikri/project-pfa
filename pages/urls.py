from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blogi/', views.blogi, name='blogi'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('contact/', views.contact, name='contact'),

    path('blog/', views.blog, name='blog'),
    path('product/', views.product, name='product'),
    path('shop/', views.shop, name='shop'),

    path('shopDresses/', views.shopDresses, name='shopDresses'),
    path('shopJackets/', views.shopJackets, name='shopJackets'),
    path('shopPants/', views.shopPants, name='shopPants'),
    path('shopShoes/', views.shopShoes, name='shopShoes'),
    path('shopTshirts/', views.shopTshirts, name='shopTshirts'),

    path('connect/', views.connect, name='connect'),

    path('cartsum/', views.total, name='total'),
    # path('delete/<int:id>/', views.delete, name='delete'),
    # path('cartdelete/', views.delete, name='delete'),

    # path('add/<int:id>/', views.add, name='add'),
    # path('cartadd/', views.add, name='add'),
    # path('cartdele/', views.dele, name='dele'),
    path('cartdelconn/', views.delconn, name='delconn'),
    path('getresponse',views.getresponse,name="getresponse"),
]