from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('register/',register, name='register'),
    path('',PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(),name='create'),
    path('login/',LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
    path('busqueda/',busqueda, name = 'busqueda'),
    path('recientes/',recientes, name = 'recientes'),
    path('antiguos/',antiguos, name = 'antiguos'),
    path('generales/',generales, name = 'generales'),
    path('accion_clima/',accionclima, name='accion_clima'),
    path('agua_limpia/',agualimpia, name='agua_limpia'),
    path('alianza_objetivos/',alianzaobjetivos, name='alianza_objetivos'),
    path('ciudades_sostenibles/',ciudadessostenibles, name='ciudades_sostenibles'),
    path('educacion_calidad/',educacioncalidad, name='educacion_calidad'),
    path('energia_sostenible/',energiasostenible, name='energia_sostenible'),
    path('fin_pobreza/',finpobreza, name='fin_pobreza'),
    path('hambre_cero/',hambrecero, name='hambre_cero'),
    path('igualdad_genero/',igualdadgenero, name='igualdad_genero'),
    path('industria/',industria, name='industria'),
    path('paz_justicia/',pazjusticia, name='paz_justicia'),
    path('produccion_consumo/',produccionconsumo, name='produccion_consumo'),
    path('reduccion_desigualdad/',reducciondesigualdad, name='reduccion_desigualdad'),
    path('salud_bienestar/',saludbienestar, name='salud_bienestar'),
    path('trabajo_decente/',trabajodecente, name='trabajo_decente'),
    path('vida_ecosistema/',vidaecosistema, name='vida_ecosistema'),
    path('vida_submarina/',vidasubmarina, name='vida_submarina'),
    path('<slug>/', PostDetailView.as_view(),name='detail'),
    path('<slug>/update', PostUpdateView.as_view(),name='update'),
    path('<slug>/delete', PostDeleteView.as_view(),name='delete'),
    path('<slug:slug>',detallePost, name = 'detalle_post'),
    path('like/<slug>/', like, name='like'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
