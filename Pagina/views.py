from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Tecnico
from .models import Orden
from .models import Cliente



def pagina_cliente(request):
	form = Cliente()

	if request.method == "POST":

		form.Nombre_cliente = request.POST['nombre']
		form.Rut = request.POST['rut']
		form.Direccion = request.POST['direccion']
		form.Ciudad = request.POST['ciudad']
		form.Comuna = request.POST['comuna']
		form.Telefono = request.POST['telefono']
		form.Email = request.POST['email']
		form.save()

	return render(request, 'Ascensores/cliente.html')

def pagina_formulario(request):
	form = Tecnico()

	if request.method == "POST":

		form.Nombre_Tecnico = request.POST['nombre']
		form.Email = request.POST['email']
		form.Contraseña = request.POST['contraseña']
		form.save()

	return render(request, 'Ascensores/formulario.html')

def pagina_index(request):
    return render(request, 'Ascensores/index.html')

def pagina_orden(request):
	form = Orden()

	if request.method == "POST":

		form.Nombre_cliente = request.POST['clienteatendido']
		form.Fecha = request.POST['fec']
		form.Hora_inicio = request.POST['horainicio']
		form.Hora_fin = request.POST['horafin']
		form.Codigo_ascensor = request.POST['codigoascensor']
		form.Modelo_ascensor = request.POST['modeloascensor']
		form.Fallas = request.POST['fallas']
		form.Reparaciones = request.POST['reparacion']
		form.Piezas_cambiadas = request.POST['piezas']
		form.Nombre_cliente = request.POST['nombrecliente']
		form.save()

	return render(request, 'Ascensores/orden.html')

def pagina_ordenesdetrabajo(request):
    orden = Orden.objects.all()
    contexto = {'ordenes':orden}
    return render(request,'Ascensores/ordenesdetrabajo.html', contexto)
    
def pagina_login(request):
    return render(request, 'Ascensores/login.html')

def pagina_ordenes(request):
	return render(request, 'Ascensores/ordenes.html')

def pagina_listaclientes(request):
	cliente = Cliente.objects.all()
	contexto = {'clientes':cliente}
	return render(request, 'Ascensores/listaclientes.html', contexto)

def pagina_clientes(request):
	return render(request, 'Ascensores/clientes.html')

