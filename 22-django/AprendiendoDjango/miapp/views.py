from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (metodos)
# MVT = Modelo Template Vista -> Acciones (metodos)

layout = """
<h1>Sitio web con Django | Cristhian Mayuri</h1>
<hr/>
<ul>
    <li>
        <a href='/inicio'>Inicio</a>
    </li>
    <li>
        <a href='/hola-mundo'>Hola Mundo</a>
    </li>
    <li>
        <a href='/pagina-pruebas'>Página de pruebas</a>
    </li>
    <li>
        <a href='/contacto'>Contacto</a>
    </li>
</ul>
<hr/>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""
    year = 2025
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"

        year += 1

    html += "</ul>"
    """
    year = 2021
    hasta = range(year, 2051)

    nombre = "Cristhian Mayuri"
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
        })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Cristhian", apellidos="Mayuri")

    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno', 'dos', 'tres']
    })

def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"

    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")

def save_article(request):
    if request.method == 'GET':
        titulo = request.GET['titulo']

        if len(titulo) <= 5:
            return HttpResponse("El título es muy pequeño")

        contenido = request.GET['contenido']
        publicado = request.GET['publicado']

        articulo = Article(
            title = titulo,
            content = contenido,
            public = publicado
        )

        articulo.save()
        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

def create_article(request):
    return render(request, 'create_article.html')

def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id, title, content, public):
    articulo = Article.objects.get(pk=id)

    articulo.title = title
    articulo.content = content
    articulo.public = public
    articulo.save()

    return HttpResponse(f"Articulo editado: <strong>{articulo.title}</strong> - {articulo.content}")

def articulos(request):
    articulos = Article.objects.all()

    # articulos = Article.objects.filter(id__lte=7, title__contains="article")

    # articulos = Article.objects.filter(Q(title__contains="Segundo") | Q(public=True))

    # articulos = Article.objects.filter(title__contains="Articulo").exclude(public=False)

    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Primer articulo' AND public = 0 ")

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')