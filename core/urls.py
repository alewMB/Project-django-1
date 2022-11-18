from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index' ),
    path('Serveur de surveillances/<slug:slug>', serveur, name='produitServeur'),
    path('Cameras/<slug:slug>', camera, name='produitCamera'),
    path('Camera PTZ/<slug:slug>', cameraptz, name='produitCameraptz'),
    path('Camera Bullet<slug:slug>', camerabullet, name='produitCameraBullet'),
    path('Switch/<slug:slug>', switchs, name='produitswitch'),
    path('Router/<slug:slug>', router, name='produitrouter'),
    path('Cables/<slug:slug>', cable, name='produitcable'),
    path('Telephone/<slug:slug>', telephone, name='produitTelephone'),
    path('serveur d appel/<slug:slug>', serveurappel, name='produitserveurappel'),
    path('Formations/<slug:slug>', formaTion, name='produitFormation'),
    path('Services/<slug:slug>', service, name='produitService'),
    path('Actualite/<slug:slug>', actualite, name='produitActualite'),
    path('À propos/<slug:slug>', apropos, name='produitPropos'),
    path('Video Surveillances/<slug:slug>', videoserveur, name='videosurveillances'),

]



