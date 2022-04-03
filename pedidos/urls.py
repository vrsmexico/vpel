from django.conf.urls import handler404
from django.contrib.auth import logout
from django.urls import path
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('resfiltro/',views.resfiltro,name="resfiltro"),
   path('',views.inicio, name='catalogo'),
   path('registro/',views.registro,name='registro'),
   path('login/',LoginView.as_view(template_name='login.html'),name='login'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('agregar/',views.agregar,name='agregar'),
   path('perfil/',views.perfil),
   path('perfil/<int:num>/',views.perfil,name='perfil'),
   path('buscar/',views.buscarp,name='buscar'),
   path("agregarp/<int:producto_id><int:pag_actual><int:ini>/",views.agregar_producto,name="agregarp"),
   path("eliminar/<int:producto_id><int:pag_actual><int:ini>/",views.eliminar_producto,name="eliminar"),
   path("limpiar/",views.limpiar_carro,name="limpiar"),
   path("hist/<total_carro>",views.historial,name="hist"),
   path("confi/",views.confirmacion,name="confirmacion"),
   path("vpel1053/",views.vpel1053,name="vpel1053"),
   path("listop/<int:suspedido_id>/",views.listop,name="listop"),
   path("series/",views.serie,name="series"),
   path("gasto/",views.gastos,name="gasto"),
   path("miperfil/<int:num>/",views.miperfil,name="miperfil"),
   path("miperfil/",views.miperfil),
   path("deuda/",views.deuda,name="deuda"),
   path("ayuda/",views.ayuda,name="ayuda"),
   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

