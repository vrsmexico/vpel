from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect

import pedidos
from.models import *
from .carro import Carro
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import agregarform,encuesta,deudarocio
from django.core.paginator import Paginator
from django.urls import path
from datetime import datetime

from django.utils import timezone



def inicio(request):
    current_user=request.user
    usua=current_user
    carross=Carro(request)
    cantp=len(carross.carro)

    califs=calificacion.objects.all()
    generos=genero.objects.all()
    peliculasL=servicio.objects.all()
    fechas=fecha.objects.all()
    numpeliculas=len(servicio.objects.all())

    paginator=Paginator(peliculasL,16)
    pagina=request.GET.get("page") or 1
    peliculas=paginator.get_page(pagina)
    pag_actual=int(pagina)
    pagante=pag_actual-1
    sigpag=pag_actual+1
    paginas=range(1,peliculas.paginator.num_pages + 1)
    ini=0
    

    return render(request,'cata.html',{"ini":ini,"cantp":cantp,'user':usua,"generos":generos,"fechas":fechas,"peliculas":peliculas,"califs":califs,"num":numpeliculas,"paginas":paginas,"pag_actual":pag_actual,"pagante":pagante,"sigpag":sigpag})



def registro(request):
    carross=Carro(request)
    cantp=len(carross.carro)
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        direc=request.POST["direccion"]
        tel=request.POST["telefono"]
        usuar=request.POST["username"]
        usuari=str(usuar)
        if form.is_valid():
            guardar=profile(telelefono=tel,direccion=direc,usuario=usuari)
            guardar.save()
            form.save()

            username=form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('login')
    else:
        form=UserRegisterForm()
    context={'form':form}
    return render(request,'registro.html',context)


def perfil(request,num=0):
    current_user=request.user
    usua=current_user
    usua=str(usua)
    pedi=Pedidos.objects.all()
    numpedi=len(pedi)
    lista=[]
    
   
    for ped in pedi:
        if ped.user ==usua :
            lista.append(int(ped.id))
    suspedidos=Pedidos.objects.filter(id__in=lista)[:10]
    if len(suspedidos) == 0:
        suspedidos=""
   


    
    return render(request,'perfil.html',{"suspedidos":suspedidos,"num":num})


def agregar(request):
    d=26 #capacidad de memoria 32gb 

    if request.method=="POST":
        agregarrespuesta=agregarform(request.POST,request.FILES)
        
        
        if agregarrespuesta.is_valid():
            infform=agregarrespuesta.cleaned_data
            titulo1=infform['titulo1']
            titulo2=infform['titulo2']
            titulo3=infform['titulo3']
            titulo4=infform['titulo4']
            tipo=infform['tipo']
            peso=infform['peso']
            cali=infform['calificacion']
            

            con1=1
            basep=servicio.objects.all()
            nump=len(basep)

            class limpiar():
                def __init__(self,valor):
                    valor=valor.lower()
                    valor=valor.replace(".","")
                    valor=valor.replace("á","")
                    valor=valor.replace("é","")
                    valor=valor.replace("í","")
                    valor=valor.replace("ó","")
                    valor=valor.replace("ú","")
                    valor=valor.replace(",","")
                    valor=valor.replace("/","")
                    valor=valor.replace("*","")
                    valor=valor.replace(":","")
                    valor=valor.replace(";","")
                    valor=valor.replace("!","")
                    valor=valor.replace("%","")
                    valor=valor.replace("(","")
                    valor=valor.replace(")","")
                    valor=valor.replace("-","")
                    valor=valor.replace("_","")
                    valor=valor.replace("[","")
                    valor=valor.replace("]","")
                    valor=valor.replace(" ","")

                    self.t1=valor
                   
            tt1=limpiar(titulo1)
            t1=tt1.t1
            
            t2=''
            if titulo2 !=None:
                tt2=limpiar(titulo2)
                t2=tt2.t1
                con1=con1+1
                
            t3=''
            if titulo3 !=None:
                tt3=limpiar(titulo3)
                t3=tt3.t1
                con1=con1+1
                
            
            t4=''
            if titulo4 !=None:
                tt4=limpiar(titulo4)
                t4=tt4.t1
                con1=con1+1
            con2=1
            buscador=0
            while con2<=con1:
                if con2==1:
                    for base in basep:
                        if t1==base.tlim1:
                            buscador=1
                        if t1==base.tlim2:
                            buscador=1
                        if t1==base.tlim3:
                            buscador=1
                        if t1==base.tlim4:
                            buscador=1
                if con2==2:
                    for base in basep:
                        if t2==base.tlim1:
                            buscador=1
                        if t2==base.tlim2:
                            buscador=1
                        if t2==base.tlim3:
                            buscador=1
                        if t2==base.tlim4:
                            buscador=1
                if con2==3:
                    for base in basep:
                        if t3==base.tlim1:
                            buscador=1
                        if t3==base.tlim2:
                            buscador=1
                        if t3==base.tlim3:
                            buscador=1
                        if t1==base.tlim4:
                            buscador=1
                if con2==4:
                    for base in basep:
                        if t4==base.tlim1:
                            buscador=1
                        if t4==base.tlim2:
                            buscador=1
                        if t4==base.tlim3:
                            buscador=1
                        if t4==base.tlim4:
                            buscador=1
                con2=con2+1
            
            tipo=str(tipo)
            
            if tipo=="serie":
                
                
                

                can=peso/d

                k=int(can)
                if can>k:
                    k=k+1
                preci=(k*130)+100
                
                    
            else:
                
                preci=20
                
            if buscador==0:
                
                a=servicio(tlim1=t1,tlim2=t2,tlim3=t3,tlim4=t4,precio=preci,calif=cali)
                form=agregarform(request.POST,request.FILES,instance=a)
                form.save()
                mensaje='GUARDADO SATISFACTORIAMENTE'
                return render(request,"respuesta.html",{'mensaje':mensaje}) 
            else:
                mensaje="Ya esta guardado esa pelicula"
                return render(request,"respuesta.html",{'mensaje':mensaje})

            
            
    else:
        agregarrespuesta=agregarform()

    return render(request,"agregar.html",{"form":agregarrespuesta})
ung=0
unf=0
unc=0
def resfiltro(request):
    global unc,ung,unf
    carross=Carro(request)
    cantp=len(carross.carro)
    
    
    cla=unc
    gen=ung
    fec=unf
    
    generos=genero.objects.all()
    califs=calificacion.objects.all()
    fechas=fecha.objects.all()
    numpeliculas=len(servicio.objects.all())
    
    mensaje="Seleccione por lo menos un filtro"
    if request.method=="POST":
        gen=request.POST["gene"]
        cla=request.POST["clasif"]
        fec=request.POST["fec"]

        ung=gen
        unc=cla
        unf=fec
    
    if cla=='0'and gen=='0' and fec=='0':
        
        peliculasL=servicio.objects.all()
        mensaje="Mostrando todas las peliculas disponibles"
        
    elif cla!='0'and gen=='0' and fec=='0':
        peliculasL=servicio.objects.filter(calif=cla)
        
        mensaje="Mostrando por calificación"
    elif cla=='0'and gen!='0' and fec=='0':
        
        peliculasL=servicio.objects.filter(genero=gen)
        
        mensaje="Mostrando por género"
    elif cla=='0'and gen=='0' and fec!='0':
        
        peliculasL=servicio.objects.filter(fecha=fec)
        
        mensaje="Mostrando por fecha"
    elif cla!='0'and gen!='0' and fec=='0':
        
        peliculasL=servicio.objects.filter(calif=cla,genero=gen)
        
        mensaje="Mostrando con filtro de calificación y genero"
    elif cla!='0'and gen=='0' and fec!='0':
        
        peliculasL=servicio.objects.filter(calif=cla,fecha=fec)
        
        mensaje="Mostrando con filtro de calificación y año"
    elif cla=='0'and gen!='0' and fec!='0':
        
        peliculasL=servicio.objects.filter(genero=gen,fecha=fec)
        
        mensaje="Mostrando con filtro de genero y año"
    elif cla!='0'and gen!='0' and fec!='0':
        
        peliculasL=servicio.objects.filter(genero=gen,fecha=fec,calif=cla)
        
        mensaje="Mostrando con filtro de calificación,genero y año"
    else:
        peliculasL=servicio.objects.all()


    paginator=Paginator(peliculasL,16)
    pagina=request.GET.get("page") or 1
    peliculas=paginator.get_page(pagina)
    pag_actual=int(pagina)
    pagante=pag_actual-1
    sigpag=pag_actual+1
    
   

    paginas=range(1,peliculas.paginator.num_pages + 1)
    ini=1
    

    return render(request,"resfiltro.html",{"ini":ini,"cantp":cantp,"generos":generos,"fechas":fechas,"mensaje":mensaje,"peliculas":peliculas,"califs":califs,"num":numpeliculas,"paginas":paginas,"pag_actual":pag_actual,"pagante":pagante,"sigpag":sigpag})

def buscarp(request):
    carross=Carro(request)
    cantp=len(carross.carro)
    pag_actual=1
    buscando=request.POST["buscarpr"]
    if buscando !='':
        limpio=buscando
        class limpie():
            
            def __init__(self,valor):
                valor=valor.lower()
                valor=valor.replace(".","")
                valor=valor.replace("á","")
                valor=valor.replace("é","")
                valor=valor.replace("í","")
                valor=valor.replace("ó","")
                valor=valor.replace("ú","")
                valor=valor.replace(",","")
                valor=valor.replace("/","")
                valor=valor.replace("*","")
                valor=valor.replace(":","")
                valor=valor.replace(";","")
                valor=valor.replace("!","")
                valor=valor.replace("%","")
                valor=valor.replace("(","")
                valor=valor.replace(")","")
                valor=valor.replace("-","")
                valor=valor.replace("_","")
                valor=valor.replace("[","")
                valor=valor.replace("]","")
                valor=valor.replace(" ","")

                self.t1=valor
                        
        lim=limpie(limpio)
        limpio=lim.t1
        buscando=limpio
        lista=[]
    

        # PARA GUARDAR var.guardarpe(basep) CON UN CLICLO 
        basepe=servicio.objects.filter(tlim1__icontains=limpio)
        for basep in basepe:
            lista.append(int(basep.id))
            
        
            

        basepe2=servicio.objects.filter(tlim2__icontains=limpio)
        listanumero=len(lista)
        listapro=lista
        for basep2 in basepe2:
            c1=0
            c2=0
            while c1<listanumero:
                if basep2.id == listapro[c1]:
                    c2=1
                    
                c1=c1+1
            if c2==0:
                lista.append(int(basep2.id))
                 
        basepe3=servicio.objects.filter(tlim3__icontains=limpio)
        listanumero=len(lista)
        listapro=lista
        for basep3 in basepe3:
            c1=0
            c2=0
            while c1<listanumero:
                if basep3.id == listapro[c1]:
                    c2=1
                    
                c1=c1+1
            if c2==0:
                lista.append(int(basep3.id))
        basepe4=servicio.objects.filter(tlim4__icontains=limpio)
        listanumero=len(lista)
        listapro=lista
        for basep4 in basepe4:
            c1=0
            c2=0
            while c1<listanumero:
                if basep4.id == listapro[c1]:
                    c2=1
                    
                c1=c1+1
            if c2==0:
                lista.append(int(basep4.id))
        basecompleta=servicio.objects.all()
        listanumero=len(lista)
        
    
        basepe=servicio.objects.filter(id__in=lista)
        
    
        buscando=""
        if len(basepe) == 0:
            buscando="Pelicula no encontrada, puede agregarla al confirmar su compra"
        
        
    else:
        buscando="Favor de ingresar la pelicula a buscar"
        basepe=""
    ini=0


    return render(request,"buscarp.html",{"ini":ini,"cantp":cantp,"buscando":buscando,"resultados":basepe,"pag_actual":pag_actual})

 
def agregar_producto(request,producto_id,pag_actual,ini):
    
    
    carro=Carro(request)
    producto=servicio.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    if ini==0:
        return redirect("/?page=%d"%pag_actual)
    elif ini==2:
        return redirect("/series")
    else:
        return redirect("/resfiltro/?page=%d"%pag_actual)


   # return redirect('/resfiltro/')
def eliminar_producto(request,producto_id,pag_actual,ini):
    
    carro=Carro(request)
    producto=servicio.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    if ini==0:
        return redirect("/?page=%d"%pag_actual)
    elif ini==2:
        return redirect("/series")
    else:
        return redirect("/resfiltro/?page=%d"%pag_actual)


def limpiar_carro(request):
    carro=Carro(request)
    
    carro.limpiar_carro()
    return redirect("resfiltro")

def historial(request,total_carro):
    
    total_carro=float(total_carro) # FLOAT PARA TOTAL
    carro=Carro(request)   # COSAS DEL CARRO
    mensaje=len(carro.carro)  # Cantidad de peliculas
    
    cars=carro.carro  # CONVIRTIENDO EN TIPO TUPLA COMO ESTO 17': {'producto_id': 17, 'nombre': '8....
    
    listap=[]
    
    for car in cars:
        val=car
        listap.append(int(val))   # OBTENIENDO SOLO LAS ID EN ENTERO Y EN UNA LISTA
    
    pedido=servicio.objects.filter(id__in=listap)
    prec=0
    for pedid in pedido:
        
        prec=prec+pedid.precio
        
    
    
    verif3=0
    
    if prec>199:
        verif3=1
    memoria=0
    if verif3==0:
        prec=prec+150
        memoria=1
    
    
    total_carro=prec




    return render(request,"historial.html",{"cantp":mensaje,"pedido":pedido,"total":total_carro,"memoria":memoria})
def confirmacion(request):
    if request.method=="POST":
        comentari=request.POST["conficomp"]
        carro=Carro(request)
        cars=carro.carro
        listap=[]
        
        pedido=""
        current_user=request.user
        usua=current_user
        coma=", "
        palabras=""
        costo=0
        conta=0
        for car in cars:
            val=car
            listap.append(int(val))
        pedido=servicio.objects.filter(id__in=listap)
        for pedi in pedido:
            pal=pedi.titulo1
            pal=str(pal)
            if conta==0:
                palabras=palabras+pal
                conta=2
            else:
                palabras=palabras+coma+pal
            costo=costo+pedi.precio

        if costo<200:
            costo=costo+150  
        costo=str(costo) 
        usualita=[] 
        usualita.append(usua)
        perfiles=profile.objects.filter(usuario__in=usualita)
        info="direccion: "
        
        for perfil in perfiles:
            
            info=info+str(perfil.direccion)+",telefono"+str(perfil.telelefono) 

        form=Pedidos(content=palabras,comentarios=comentari,user=usua,masinfo=costo,memorias=info)
        form.save()
        
    carro.limpiar_carro()

    
    return redirect('/perfil/1')

def vpel1053(request):
    entregar=Pedidos.objects.all()
    lista=[]
    
    
    for entrega in entregar:
        if entrega.entregado is False:
            lista.append(int(entrega.id))
            

    pedi=Pedidos.objects.filter(id__in=lista)
    if request.method=="POST":
        fechass=request.POST["fecha"]
        guardarfecha=fecha(fecha=fechass)
        guardarfecha.save()
    
    
    return render(request,'vpel1053.html',{"suspedidos":pedi})
def listop(request,suspedido_id):
    pedi=int(suspedido_id)
    lista=[]
    lista.append(suspedido_id)
    cambiar=Pedidos.objects.get(id=suspedido_id)
    cambiar.entregado=1
    cambiar.save()
    return redirect("/vpel1053/")
def serie(request):
    otralista=['serie']
    tip=tipo.objects.filter(tipo__in=otralista)
    
    lista=[]
    for ti in tip:
        if ti.tipo == "serie":
            lista.append(ti.id)
    
    todas=servicio.objects.filter(tipo__in=lista)
    ini=2
    return render(request,"series.html",{"resultados":todas,"ini":ini,})
def gastos(request):
    model=Cuentas
    if request.method=="POST":
        cantidad=request.POST["canti"]
        concepto=request.POST["conce"]
        if 'ganper' in request.POST:
            ganancia = request.POST['ganper']

        else:
            ganancia = 0
    
        
        
        if ganancia == '1':
            a=Cuentas(canti=cantidad,ganper=1,conce=concepto,importa=0,entraporcen=0)
            form=encuesta(request.POST,instance=a)
            form.save()
            return redirect("/miperfil/")

        else:
            if 'importa' in request.POST:
                importante = request.POST['importa']
                
            else:
                importante = 0
            
            if importante == '1':
                
                a=Cuentas(canti=cantidad,ganper=0,conce=concepto,importa=1,entraporcen=1)
                form=encuesta(request.POST,instance=a)
                form.save()
                return redirect("/miperfil/")


            else:
                a=Cuentas(canti=cantidad,ganper=0,conce=concepto,importa=0,entraporcen=1)
                form=encuesta(request.POST,instance=a)
                form.save()
                return redirect("/miperfil/")
    else:
        forma=encuesta()

    return render(request,"gastos.html",{"forma":forma})
def miperfil(request,num=54):
    
    sema=datetime.now()
    sema=sema.strftime("%W")
    if num>=0 and num<54:
        semactual=str(num)
    else:
        semactual=datetime.now()
        
        semactual=semactual.strftime("%W")
    

    totalaldia=0
    positisdia=0
    negatidia=0
    positis=0
    cuentas=Cuentas.objects.filter(entraporcen__in='1')
    cuentapositivas=Cuentas.objects.filter(entraporcen__in='0')
    for cuentapositiva in cuentapositivas:
        fechaposi=cuentapositiva.create
        
        fechaposi=fechaposi.strftime("%W")
        positisdia=positisdia+cuentapositiva.canti #CON ESTO OBTENEMOS LA GANANCIA DE TOD EL A;O
        if fechaposi==semactual:
            positis=positis+cuentapositiva.canti #CON ESTO LA GANANCIA DE LA SEMANA

    admisemana=0
    for cuenta in cuentas:
        fechacuenta=cuenta.create
        fechacuenta=fechacuenta.strftime("%W")
        negatidia=negatidia+cuenta.canti #CON ESTO OBTENEMOS LOS GASTOS DEL A;O
        if fechacuenta==semactual:
            admisemana=admisemana+cuenta.canti #CON ESTO GASTOS TOTALES POR SEMANA
    total=positis-admisemana #TOTAL POR SEMANA
    totalaldia=positisdia-negatidia #TOTAL POR A;O
    columna=[]
    data=[]
    gastosmayores=[]
    for cuenta in cuentas:
        fechacuenta=cuenta.create
        
        
        fechacuenta=fechacuenta.strftime("%W")
        
        if fechacuenta==semactual:
            porce=(cuenta.canti/positis)*100
            porce=round(porce,2)
            porcegas=(cuenta.canti/admisemana)*100
            porcegas=round(porcegas,2)
            
            
            fila=[]
            data.append(
                {
                    'name': cuenta.conce,
                    'y':porcegas,
                    'cant':cuenta.canti

                })
            fila.append(porce)
            fila.append(cuenta.conce)
            fila.append(cuenta.canti)
            if porce >80:
                
                gastosmayores.append(fila)
            else:
                
                columna.append(fila) #LISTA CON PORCENTAJES Y CONCEPTOS DE GASTO
    x=len(columna)
    
   
    
    return render(request,"miperfil.html",{"total":totalaldia,"totalsemana":total,"matrizsem":columna,"gastosmayores":gastosmayores,"n":x,"data":data,"gastos":admisemana,"semana":semactual,"range":range(54),"sema":sema,"ganados":positis})
def deuda(request):
    
    model=Gastos
    if request.method=="POST":
        cantidad=request.POST["cantidad"]
        concepto=request.POST["concep"]
        if 'importancia' in request.POST:
            importante = request.POST['importancia']#ES 1 CUANDO ES ABONO 
        else:
            importante = 0  #ES 0 CUANDO ES DINERO GASTADO
    
        
        
        if importante == '1':     #seria pago JOSE
            a=Gastos(cantidad=cantidad,ganoper=1,concep=concepto,importancia=1)
            form=deudarocio(request.POST,instance=a)
            form.save()
            return redirect("/deuda/")

        else:
            if 'ganoper' in request.POST:
                ganoper = request.POST['ganoper'] #a mi favor
                
            else:
                ganoper = 0 #a favor de rocio
            
            if ganoper == '1':
                
                a=Gastos(cantidad=cantidad,ganoper=1,concep=concepto,importancia=0)
                form=deudarocio(request.POST,instance=a)
                form.save()
                return redirect("/deuda/")


            else:
                a=Gastos(cantidad=cantidad,ganoper=0,concep=concepto,importancia=0)
                form=deudarocio(request.POST,instance=a)
                form.save()
                return redirect("/deuda/")
    else:
        forma=deudarocio()
        cuent=Gastos.objects.filter(importancia__in='0')
        abon=Gastos.objects.filter(importancia__in='1')
        
        total=0
        listar=[]
        listaj=[]
        for i in cuent:
            if i.ganoper == 0:
                
                deuda=i.cantidad/2
                total=total+deuda
                fila=[]
                fila.append(i.concep)
                fila.append(i.cantidad)
                fila.append(i.created)
                listar.append(fila)
                
            else:
                deuda=i.cantidad/2
                total=total-deuda
                fila=[]
                fila.append(i.concep)
                fila.append(i.cantidad)
                fila.append(i.created)
                listaj.append(fila)
        for i in abon:

            total=total-i.cantidad
            fila=[]
            fila.append(i.concep)
            fila.append(i.cantidad)
            fila.append(i.created)
            listaj.append(fila)





        

    return render(request,"deuda.html",{"forma":forma,"total":total,"listaj":listaj,"listar":listar,})
def ayuda(request):
    
    return render(request,"ayuda.html")

    
    #now=datetime.now()
    #dia=now.strftime("%A")
    #fecha=pedid.created
    #formato=fecha.strftime("%W")
    #print(formato)
    #print (dia)
    
    
    #return render(request,'gastos.html',{"suspedidos":pedi})




# def error404(request,exception):
    # se agrego unas informacion en url VPEL y el html

   #  return render(request,'404.html')


