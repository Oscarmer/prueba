import string
from tkinter import messagebox
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.conf import settings
from dataclasses import fields
from datetime import datetime, date
# Create your views here.

def lugares(request):
    lugares = lugar.objects.all()
    return render(request, "lugar/index.html", {'lugares': lugares})

def agregar_lg(request):
    formulario = lgForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('lugar')
    return render(request, "lugar/crear.html", {'formulario': formulario})    

def eliminar_lg(request, id):
    lugares = lugar.objects.get(id_lg=id)
    lugares.delete()
    return redirect('lugar')

def log(request, id):
    log = id
    return redirect("/"+ str(log)+ "/" + 'home')

def home(request, lg):
    productos = producto.objects.all()
    lista = []
    for pd in productos:
        if pd.id_lg_id == lg:
            lista.append(pd)
    return render(request, "pages/inicio.html", {'productos': lista, 'lugar': lg})

def nosotros(request):
    return render(request, "pages/nosotros.html")

def productos(request, lg):
    productos = producto.objects.all()
    lista = []
    for pd in productos:
        if pd.id_lg_id == lg:
            lista.append(pd)
    return render(request, "productos/index.html", {'productos': lista, 'lugar': lg})

def agregar_pd(request, lg):
    formulario = productoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('/'+str(lg)+'/'+'productos')
    return render(request, "productos/crear.html", {'formulario': formulario})

def editar_pd(request, id, lg):
    productos = producto.objects.get(id_pd=id)
    formulario = productoForm(request.POST or None, request.FILES or None, instance=productos)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('/'+str(lg)+'/'+'productos')
    return render(request, "productos/editar.html", {'formulario': formulario})

def eliminar_pd(request, id, lg):
    productos = producto.objects.get(id_pd=id)
    productos.delete()
    return redirect('/'+str(lg)+'/'+'productos')

#------------------------------materia_p-------------------------------------------------

def materiap(request, lg):
    materiap = materia_p.objects.all()
    lista = []
    for mp in materiap:
        if mp.id_lg_id == lg:
            lista.append(mp)
    return render(request, "materiap/index.html", {'materiap': lista, 'lugar': lg})

def agregar_mp(request, lg):
    formulario = dtMpForm(request.POST or None, request.FILES or None)
    contacto = "None"
    tiempo = 0
    mincant = 0
    descripcion = "None"
    if formulario.is_valid():
        if formulario.data['contacto'] != '':
            contacto = contacto = formulario.data['contacto']

        if formulario.data['tiempo'] != '':
            tiempo = formulario.data['tiempo']

        if formulario.data['mincant'] != '':    
            mincant = formulario.data['mincant']

        if formulario.data['descripcion'] != '':
            descripcion = formulario.data['descripcion']

        data = {'nombre': formulario.data['nombre'], 'cantidad': int(formulario.data['cantidad']), 'unidad': formulario.data['unidad'], 'costo': int(formulario.data['costo']), 'costo_u': int(formulario.data['costo'])//int(formulario.data['cantidad']), 'proveedor': formulario.data['proveedor'], 'contacto': contacto, 'tiempo': tiempo, 'mincant': int(mincant), 'descripcion': descripcion, 'estado': 'Activo', 'id_lg': lg}
    
        formulario = mpForm(data)
        if formulario.is_valid():
            print("si")
            formulario.save()
        return redirect('/' + str(lg) + '/materiap')
    return render(request, "materiap/crear.html", {'formulario': formulario})

def editar_mp(request, id, lg):
    materiap = materia_p.objects.get(id_mp=id)
    mezclas = mezcla.objects.all()
    formulario = mpForm(request.POST or None, request.FILES or None, instance=materiap)
    if formulario.is_valid() and request.POST:
        formulario.save()
        for mz in mezclas:
            if mz.id_mp_id == id:
                if mz.cantidad > materiap.cantidad:
                    materiap.estado = "Inactivo"
                else:
                    materiap.estado = "Activo"
                materiap.save()
        return redirect('/' + str(lg) + '/materiap')
    return render(request, "materiap/editar.html", {'formulario': formulario})

def eliminar_mp(request, id, lg):
    materia = materia_p.objects.get(id_mp=id)
    materia.delete()
    return redirect('/' + str(lg) + '/materiap')

#------------------------------materia_s-------------------------------------------------

def materias(request, lg):
    materias = materia_s.objects.all()
    lista = []
    for ms in materias:
        if ms.id_lg_id == lg:
            lista.append(ms)
    return render(request, "materias/index.html", {'materias': lista, 'lugar': lg})

def agregar_ms(request, lg):
    formulario = dtMsForm(request.POST or None, request.FILES or None)
    descripcion = "None"
    if formulario.is_valid():
        if formulario.data['descripcion'] != '':
            descripcion = formulario.data['descripcion']
        data = {'nombre': formulario.data['nombre'], 'descripcion': descripcion, 'estado': "Activo", 'id_lg': lg}
        formulario = msForm(data)
        if formulario.is_valid():
            formulario.save()
        return redirect('/'+str(lg)+'/materias')
    return render(request, "materias/crear.html", {'formulario': formulario})

def editar_ms(request, id, lg):
    materias = materia_s.objects.get(id_ms=id)
    formulario = msForm(request.POST or None, request.FILES or None, instance=materias)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('/'+str(lg)+'/materias')
    return render(request, "materias/editar.html", {'formulario': formulario})

def eliminar_ms(request, id, lg):
    materia = materia_s.objects.get(id_ms=id)
    materia.delete()
    return redirect('/'+str(lg)+'/materias')

#------------------------------mezcla-------------------------------------------------

def mezclas(request, id, lg):
    mezclas = mezcla.objects.all()
    materiap = materia_p.objects.all()
    materias = materia_s.objects.get(id_ms=id)
    ingredientes = []
    prm = []
    filtro = []
    for i in mezclas:
        if i.id_ms_id == id:
            filtro.append(i)
            for j in materiap:
                if j.id_mp == i.id_mp_id:
                    if i.cantidad > j.cantidad:
                        j.estado = "Inactivo"
                    else:
                        j.estado = "Activo"
                    j.save()
                    prm.append(j)
    for a, b in zip(prm, filtro):
        b.id_us_id = id
        b.id_mp_id = a.nombre
        b.id_ms_id = materias.nombre
        ingredientes.append(b)
    return render(request, "mezcla/index.html", {'mezclas': ingredientes, 'materias': id, 'lugar': lg})

def agregar_mz(request, id, lg):
    materiap = materia_p.objects.all()
    formulario = dtMzForm(request.POST or None, request.FILES or None)
    data = {}
    if formulario.is_valid():
        for mp in materiap:
            if (mp.nombre).upper() == (formulario.data['materia_p']).upper():
                if mp.id_lg_id == lg:
                    data = {'id_ms': id, 'id_mp': mp.id_mp, 'cantidad': formulario.data['cantidad'], 'costo': int(formulario.data['cantidad']) * mp.costo_u}
        formulario = mzForm(data)
        if formulario.is_valid():
            formulario.save()
            return redirect("/"+ str(lg) +'/mezcla' + str(id))
    return render(request, "mezcla/crear.html", {'formulario': formulario})

def editar_mz(request, id, id2, lg):
    materiap = materia_p.objects.all()
    mezclas = mezcla.objects.get(id_mz=id)
    formulario = mzForm(request.POST or None, request.FILES or None, instance=mezclas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        for mp in materiap:
            if mezclas.cantidad > mp.cantidad:
                mp.estado = "Inactivo"
                mp.save()
        return redirect("/"+ str(lg) +'/mezcla' + str(id2))
    return render(request, "mezcla/editar.html", {'formulario': formulario})

def eliminar_mz(request, id, id2, lg):
    mezclas = mezcla.objects.get(id_mz=id)
    mezclas.delete()
    return redirect("/"+ str(lg) +'/mezcla' + str(id2))

#------------------------------posicion-------------------------------------------------

def posiciones(request, id, lg):
    posiciones = posicion.objects.all()
    productos = producto.objects.get(id_pd=id)
    resultado = []
    filtro = []
    for i in posiciones:
        if i.id_pd_id == id:
            filtro.append(i)
    for a in filtro:
        a.id_us_id = productos.nombre
        resultado.append(a)
    return render(request, "posicion/index.html", {'posiciones': resultado, 'producto': id, 'lugar': lg})

def agregar_ps(request, id, lg):
    formulario = dtPsForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        data = {'nombre': formulario.data['nombre'], 'precio': formulario.data['precio'], 'id_pd': id}
        formulario = psForm(data)
        formulario.save()
        return redirect("/"+str(lg)+'/posicion'+ str(id))
    return render(request, "posicion/crear.html", {'formulario': formulario})

def editar_ps(request, id, id2, lg):
    posiciones = posicion.objects.get(id_ps=id)
    formulario = psForm(request.POST or None, request.FILES or None, instance=posiciones)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("/"+str(lg)+'/posicion'+ str(id2))
    return render(request, "posicion/editar.html", {'formulario': formulario})

def eliminar_ps(request, id, id2, lg):
    posiciones = posicion.objects.get(id_ps=id)
    posiciones.delete()
    return redirect("/"+str(lg)+'/posicion'+ str(id2))

#------------------------------menu-------------------------------------------------

def menus(request, id, lg):
    menus = menu.objects.all()
    materias = materia_s.objects.all()
    posiciones = posicion.objects.get(id_ps=id)
    elementos = []
    sec = []
    filtro = []
    for i in menus:
        if i.id_ps_id == id:
            filtro.append(i)
            for j in materias:
                if j.id_ms == i.id_ms_id:
                    sec.append(j)
    for a, b in zip(sec, filtro):
        b.id_ms_id = a.nombre
        b.id_ps_id = posiciones.nombre
        elementos.append(b)
    return render(request, "menu/index.html", {'menus': elementos, 'posicion': id, 'lugar': lg})

def agregar_mn(request, id, lg):
    materias = materia_s.objects.all()
    formulario = dtMnForm(request.POST or None, request.FILES or None)
    data = {}
    if formulario.is_valid():
        for ms in materias:
            if (ms.nombre).upper() == (formulario.data['materia_s']).upper():
                if ms.id_lg_id == lg:
                    data = {'id_ms': ms.id_ms, 'id_ps': id}
        formulario = mnForm(data)
        if formulario.is_valid():
            formulario.save()
        return redirect("/"+str(lg)+'/menu' + str(id))
    return render(request, "menu/crear.html", {'formulario': formulario})

def editar_mn(request, id, lg):
    menus = menu.objects.get(id_mn=id)
    formulario = mnForm(request.POST or None, request.FILES or None, instance=menus)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("/"+str(lg)+'/menu' + str(menus.id_ps_id))
    return render(request, "menu/editar.html", {'formulario': formulario})

def eliminar_mn(request, id, lg):
    menus = menu.objects.get(id_mn=id)
    menus.delete()
    return redirect("/"+str(lg)+'/menu' + str(menus.id_ps_id))

#------------------------------carrito-------------------------------------------------

def carritos(request, lg):
    armados = armado.objects.all()
    menus = menu.objects.all()
    posiciones = posicion.objects.all()
    productos = producto.objects.all()
    carritos = candycarrito.objects.all()
    preciou = 0
    iter = 0
    lista = []
    presu = []
    pres = []
    precio = 0
    resultado = []
    for cr in carritos:
        if cr.id_lg_id == lg:
            lista.append(cr)
    for i in lista:
        for a in armados:
            if a.id_cr_id == i.id_cr:
                for m in menus:
                    if a.id_mn_id == m.id_mn:
                        for p in posiciones:
                            if p.id_ps == m.id_ps_id:
                                if p.id_ps not in pres:
                                    precio += p.precio
                                    preciou += p.precio
                                    pres.append(p.id_ps)
        presu.append(preciou)
        pres.clear()
        preciou = 0
        for j in productos:
            if i.id_pd_id == j.id_pd:
                i.nombre_pd = j.nombre
                i.precio = presu[iter] + j.precio
                precio += j.precio
                resultado.append(i)
                iter += 1
                break
                                
    return render(request, "carrito/index.html", {'carritos': resultado, 'precio': precio, 'lugar': lg})

def agregar_cr(request, id, lg):
    data = {'id_pd': id, 'nombre_pd': "null", 'precio': 0, 'id_lg': lg} 
    formulario = crForm(data)
    if formulario.is_valid():
        formulario.save()
        return redirect('/'+str(lg)+'/carrito')
    return render(request, "carrito/crear.html", {'formulario': formulario})

def eliminar_cr(request, id, lg):
    carritos = candycarrito.objects.get(id_cr=id)
    carritos.delete()
    return redirect('/'+str(lg)+'/carrito')

#------------------------------armado-------------------------------------------------

def armados(request, id, lg):
    carritos = candycarrito.objects.get(id_cr=id)
    armados = armado.objects.all()
    menus = menu.objects.all()
    posiciones = posicion.objects.all()
    materias = materia_s.objects.all()
    productos = producto.objects.all()
    precio = 0 # precio
    pres = [] #lista de posiciones ecogidas para regular precio
    arm = [] # lista de adiciones escogidas
    mats = [] # materias secundarias
    filtro = [] # variaciones del producto escogido con los nombres de las materias secundarias 
    for pd in productos:
        if pd.id_pd == carritos.id_pd_id:
            prod=pd
            break
    for ps in posiciones:
        if ps.id_pd_id == prod.id_pd:
            ps.id_pd_id = prod.nombre
            filtro.append(ps)
    for fl in filtro:           
        for mn in menus:
            if mn.id_ps_id == fl.id_ps:
                for ms in materias:
                    if ms.id_ms == mn.id_ms_id:
                        ms.id_ms = id
                        ms.descripcion = fl.id_ps
                        ms.estado = mn.id_mn
                        mats.append(ms)
                        for ar in armados:
                            if ar.id_cr_id == carritos.id_cr:
                                if ar.id_mn_id == mn.id_mn:
                                    if fl.id_ps not in pres:
                                        precio += fl.precio
                                        pres.append(fl.id_ps)
                                    ar.nombre_ms = ms.nombre
                                    arm.append(ar)
    if len(arm) == 0:
        precio = 0                    
    return render(request, "armado/index.html", {'posiciones': filtro, 'materias': mats, 'armados': arm, 'precio': precio, 'lugar': lg})

def agregar_ar(request, id, id2, lg):
    data = {'id_cr': id, 'id_mn': id2, 'nombre_ms': 'null', 'precio': 0}
    formulario = arForm(data)
    if formulario.is_valid():
        formulario.save()
        return redirect("/"+str(lg)+"/armado"+ str(id))
    return render(request, "armado/crear.html", {'formulario': formulario})

def eliminar_ar(request, id, id2, lg):
    print(id)
    print(id2)
    armados = armado.objects.get(id_ar=id)
    armados.delete()
    return redirect("/"+str(lg)+"/armado"+ str(id2))

#------------------------------entregado-------------------------------------------------

def entregados(request, lg):
    entregados = entregado.objects.all()
    filtro = []
    for et in entregados:
        if et.id_lg_id == lg:
            filtro.append(et)
    rep = []
    mesas = []
    for en in filtro:
        if en.mesa not in rep:
            rep.append(en.mesa)
            mesas.append([en.mesa, "|  Precio: "+ str(en.preciot), " |  Cliente: " + str(en.cliente)])
        else:
            lugar = rep.index(en.mesa)
            rep.pop(lugar)
            rep.append(en.mesa)
            mesas.pop(lugar)
            mesas.append([en.mesa, "|  Precio: "+ str(en.preciot), " |  Cliente: " + str(en.cliente)])
    return render(request, "entregado/index.html", {'entregados': entregados, 'mesas': mesas, 'lugar': lg})

def agregar_en(request, lg):
    carritos = candycarrito.objects.all()
    productos = producto.objects.all()
    armados = armado.objects.all()
    posiciones = posicion.objects.all()
    menus = menu.objects.all()
    materias = materia_s.objects.all()
    mezclas = mezcla.objects.all()
    materiap = materia_p.objects.all()
    pres = []
    precio = 0
    preciof = 0
    arm = " "
    formulario = dtEnForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        for car in carritos:
            for ar in armados:
                if ar.id_cr_id == car.id_cr:
                    for mn in menus:
                        if mn.id_mn == ar.id_mn_id:
                            for ms in materias:
                                if ms.id_ms == mn.id_ms_id:
                                    arm += str(ms.nombre) + " - "
                                    for mz in mezclas:
                                        if mz.id_ms_id == ms.id_ms:
                                            for mp in materiap:
                                                if mp.id_mp == mz.id_mp_id:
                                                    estado = "activo"
                                                    if mp.cantidad - mz.cantidad <= 0 or mp.cantidad - mz.cantidad < mz.cantidad:
                                                        estado = "inactivo"
                                                    mp.cantidad = mp.cantidad - mz.cantidad
                                                    mp.estado = estado
                                                    mp.save()

                            for p in posiciones:
                                if p.id_ps == mn.id_ps_id:
                                    if p.id_ps not in pres:
                                        precio += p.precio
                                        preciof += p.precio
                                        pres.append(p.id_ps)
            pres.clear()
            for prod in productos:
                if prod.id_pd == car.id_pd_id:
                    if arm == " ":
                        arm = "Sin adiciones"
                    else:
                        dis = len(arm)
                        arm = arm[:dis-2]
                    data = {'mesa': formulario.data['mesa'], 'cliente': formulario.data['cliente'], 'id_cr': prod.nombre, 'descripcion': arm, 'precio': precio, 'preciot': preciof, 'id_lg': lg} 
                    form = enForm(data)
                    arm = " "
                    precio = 0
                    if form.is_valid():
                        form.save()
        carritos.delete()                
        return redirect('/'+str(lg)+'/entregado') 
    return render(request, "entregado/crear.html", {'formulario': formulario})

def eliminar_en(request, id, lg):
    entregados = entregado.objects.get(id_eg=id)
    entregados.delete()
    return redirect('/'+str(lg)+'/entregado')

#------------------------------factura-------------------------------------------------
def agregar_ft(request, mesa, lg):
    data = {'id_lg': lg}
    formulario = ftForm(data)
    if formulario.is_valid():
        formulario.save()
        agregar_inft(mesa, lg)
        return redirect('/'+str(lg)+'/entregado') 
    return render(request, "factura/crear.html", {'formulario': formulario})

#------------------------------infoft-------------------------------------------------

def infactura(request, lg):
    infactura = infofactura.objects.all()
    lugares = lugar.objects.all()
    for lug in lugares:
        if lug.id_lg == lg:
            maps = lug.nombre
            break
    filtro = []
    for inf in infactura:
        if inf.lugar == maps:
            filtro.append(inf)
    titulos = []
    tablas = []
    for ft in filtro:
        if ft.id_ft not in tablas:
            tablas.append(ft.id_ft)
            titulos.append([ft.id_ft, [ft.producto], ft.precio, ft.fecha])
        else:
            lugars=tablas.index(ft.id_ft)
            titulos[lugars][1].append(ft.producto)
            titulos[lugars][2] += ft.precio
        
    return render(request, "infofactura/index.html", {'informaciones': filtro, 'titulos': titulos, 'lugar': lg, 'nombre': maps})

def masinfo(request, id, lg):
    infactura = infofactura.objects.all()
    lugares = lugar.objects.all()
    for lug in lugares:
        if lug.id_lg == lg:
            maps = lug.nombre
            break
    info = []
    for ft in infactura:
        if ft.id_ft == id:
            info.append(ft)
    return render(request, "infofactura/masinfo.html", {'infos': info, 'lugar': maps})


def agregar_inft(mesa, lg):
    facturas = factura.objects.all()
    lugares = lugar.objects.all()
    for lug in lugares:
        if lug.id_lg == lg:
            lugars = lug.nombre  
            break 
    for i in facturas:
        id = i.id_ft
        break
    carritos = candycarrito.objects.all()
    entregados = entregado.objects.all()
    for en in entregados:
        if en.mesa == mesa:
            fecha = datetime.now()
            data = {'precio': en.precio, 'entregado': en.id_eg, 'producto': en.id_cr, 'adiciones': en.descripcion, 'fecha': "  " + str(date.today()) + "  |  " + str(fecha.strftime("%X")), 'id_ft': id, 'lugar': lugars}
            formulario = inftForm(data)
            if formulario.is_valid():
                formulario.save() 
            en.delete()
    facturas.delete()
    return redirect('/'+str(lg)+'/entregado')


#---------------------------------------------------------------------------------------------

def admins(request, lg):
    return render(request, "admins/index.html")

#--------------------------------------------------------------------------------------------

def enviarp(request, nombrep, lg):
    lugares = lugar.objects.all()
    materiap = materia_p.objects.all()
    formulario = enviarForm(request.POST or None, request.FILES or None)
    pas = "no"
    if formulario.is_valid() and request.POST:
        for lug in lugares:
            if (lug.nombre).upper() == (formulario.data['lugar']).upper():
                for mp in materiap:
                    if (mp.nombre).upper() == (nombrep).upper():
                        if mp.id_lg_id == lug.id_lg:
                            mp.cantidad += int(formulario.data['cantidad'])
                            pas = "si"
                            mp.save()
                        elif mp.id_lg_id == lg:
                            mp.cantidad -= int(formulario.data['cantidad'])
                            mp.save()
                if pas == "no":
                    for mp in materiap:
                        if mp.id_lg_id == lg:
                            data = {'nombre': mp.nombre, 'cantidad': int(formulario.data['cantidad']), 'unidad': mp.unidad, 'costo': mp.costo, 'costo_u': mp.costo_u, 'proveedor': mp.proveedor, 'contacto': mp.contacto, 'tiempo': mp.tiempo, 'mincant': mp.mincant, 'descripcion': mp.descripcion, 'estado': mp.estado, 'id_lg': lug}
                            formulario = mpForm(data)
                            if formulario.is_valid():
                                formulario.save()
        return redirect('/'+str(lg)+'/materiap')
    return render(request, "enviarp/enviar.html", {'formulario': formulario})


    