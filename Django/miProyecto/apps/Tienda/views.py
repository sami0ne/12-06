from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def cargarInicio(request):
    productos = Producto.objects.all()
    cate_perros = Producto.objects.filter(categoria_id = 1)
    cate_gatos = Producto.objects.filter(categoria_id = 2)
    return render(request, "inicio.html",{"prod":productos, "cate_perro":cate_perros,"cate_gato":cate_gatos})



def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    return render(request,"agregarProducto.html",{"cate":categorias})

def agregarProducto(request):
    #print("AGREGAR PRODUCTO", request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_descripcion= request.POST['txtDescripcion']
    v_stock= request.POST['txtStock']
    v_precio= request.POST['txtPrecio']
    v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])
    v_image = request.FILES['txtImg']

    Producto.objects.create(sku = v_sku, nombre = v_nombre, descripcion = v_descripcion, stock = v_stock, precio = v_precio,fecha_vencimiento = v_fecha_vencimiento,categoria_id = v_categoria, image_url = v_image )
    
    return redirect('/agregarProducto')