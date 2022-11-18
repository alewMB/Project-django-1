from django.shortcuts import render
from django.http import Http404
from django.http import HttpRequest
from .models import *
from django.views.generic import TemplateView, ListView

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)


def index(request):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(),
        'FormAtion' :formation.objects.all(), 
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(),
        'ProduitServic' : ProduitService.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),       
    }
    return render(request, "index.html",context)



def serveur(request, slug):
    try:
        context={
            'categorys':Category.objects.all(),
            'ProduitServeur':produitserveur.objects.all(),
            'ProduitCamera':produitcamera.objects.all(),
            'ProduitCameraptz':produitcameraptz.objects.all(),
            'ProduitCameraBullet':produitcamerabullet.objects.all(),  
            'Produittelephone':produitelephone.objects.all(),
            'Produitswitch':produitswitch.objects.all(),
            'Produitroute':produitroute.objects.all(),
            'Produitcable':produitcable.objects.all(),
            'Produitserveurappel':produitserveurappel.objects.all(),
            'ProduitActualit' : ProduitActualite.objects.all(),
            'ProduitAPropo' : ProduitAPropos.objects.all(),            
            'ProduitServic' : ProduitService.objects.all(), 
            'FormAtion' : formation.objects.all(),   
            'Produitserveur':produitserveur.objects.get(slug=slug),             
        }
    except context.DoesNotExist:    
        raise Http404
    return render(request, "produitServeur.html",context)
   
def camera(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),            
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),  
        'Produitcamera':produitcamera.objects.get(slug=slug),
        
    }
    return render(request, "produitCamera.html",context)
def cameraptz(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),            
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),  
        'ProduitCameraPTZ':produitcameraptz.objects.get(slug=slug),
        
    }
    return render(request, "produitCameraptz.html",context)
def camerabullet(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),           
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),  
        'ProduitcameraBullet':produitcamerabullet.objects.get(slug=slug),
        
    }
    return render(request, "produitCameraBullet.html",context)



def switchs(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(),

        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),    
        
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(), 
        'ProduitSwitch':produitswitch.objects.get(slug=slug),

            
    }
    return render(request, "produitswitch.html",context)

def router(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),          
        'Produitswitch':produitswitch.objects.all(),
        'ProduitRoute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'Produitrouter':produitroute.objects.get(slug=slug),

            
    }
    return render(request, "produitrouter.html",context)

def cable(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),           
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(), 
        'ProduitCable':produitcable.objects.get(slug=slug),

            
    }
    return render(request, "produitcable.html",context)



def telephone(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),          
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(), 
        'ProduitTelephone':produitelephone.objects.get(slug=slug), 

           
    }
    return render(request, "produitTelephone.html",context)

def serveurappel(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),         
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitServeurappel':produitserveurappel.objects.get(slug=slug), 
            }
    return render(request, "produitserveurappel.html",context)


def formaTion(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),           
        'ProduitServic' : ProduitService.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitFormation':formation.objects.get(slug=slug), 
        
            }
    return render(request, "produitFormation.html",context)

def service(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),         
        'ProduitServic' : ProduitService.objects.all(), 
        'Produitservice':ProduitService.objects.get(slug=slug), 

            }
    return render(request, "produitService.html",context)

def actualite(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitServic' : ProduitService.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),          
        'ProduitActualit' : ProduitActualite.objects.all(),         
        'Produitactualit':ProduitActualite.objects.get(slug=slug), 

            }
    return render(request, "produitActualite.html",context)

def apropos(request, slug):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitServic' : ProduitService.objects.all(), 
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),          
        'Produitapropo':ProduitAPropos.objects.get(slug=slug), 

            }
    return render(request, "produitPropos.html",context)


def videoserveur(request):
    context={
        'categorys':Category.objects.all(),
        'ProduitServeur':produitserveur.objects.all(),
        'ProduitCamera':produitcamera.objects.all(),
        'ProduitCameraptz':produitcameraptz.objects.all(),
        'ProduitCameraBullet':produitcamerabullet.objects.all(), 
        'Produittelephone':produitelephone.objects.all(),
        'Produitswitch':produitswitch.objects.all(),
        'Produitroute':produitroute.objects.all(),
        'Produitcable':produitcable.objects.all(),
        'Produitserveurappel':produitserveurappel.objects.all(), 
        'FormAtion' : formation.objects.all(),
        'ProduitServic' : ProduitService.objects.all(), 
        'ProduitActualit' : ProduitActualite.objects.all(),
        'ProduitAPropo' : ProduitAPropos.objects.all(),    
        

            }
    return render(request, "videosurveillances.html",context)


