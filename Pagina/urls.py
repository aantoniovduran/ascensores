from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^pagina_index/',views.pagina_index, name='pagina_index'),
    url(r'^pagina_cliente/',views.pagina_cliente, name='pagina_cliente'),
    url(r'^pagina_clientes/',views.pagina_clientes, name='pagina_clientes'),
    url(r'^pagina_formulario/',views.pagina_formulario, name='pagina_formulario'),
    url(r'^pagina_orden/',views.pagina_orden, name='pagina_orden'),
    url(r'^pagina_listaclientes/',views.pagina_listaclientes, name='pagina_listaclientes'),
    url(r'^pagina_ordenes/',views.pagina_ordenes, name='pagina_ordenes'),
    url(r'^pagina_ordenesdetrabajo/',views.pagina_ordenesdetrabajo, name='pagina_ordenesdetrabajo'),
    url(r'^',views.pagina_login, name='pagina_login'),
    
]