from django.urls import path
from UserSide.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        
    path('signup/',signupPageView,name='signup-page'),
    path('login/',loginPageView,name='login-page'),
    path('logout/',logoutPageView,name='logout-page'),


    path('',indexPage,name='index-page'),
    path('home/',homePage,name='home-page'),
    path('option/<int:category>/',optionPage,name="option-page"),
    path('dish/<int:option>/',dishPage,name="dish-page"),
    path('cart/<int:id>',addToCart,name="cart"),
    path('cart/',cartPage,name="cart-page"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
