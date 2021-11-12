from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return HttpResponse("<strong>FGV</strong>")

def redireciona(request):
    url_direcionamento = reverse("dinamica-str", args=['leao'])
    return HttpResponseRedirect(url_direcionamento)

def retorna_html(request):
    return render(request, 'fgv/fgv.html')

def view_dinamic_int(request, param):
    if param == 0:
        return HttpResponse('<strong>Parâmetro 0</strong>')
    elif param == 1:
        return HttpResponse('<strong>Parâmetro 1</strong>')
    elif param == 2:    
        return HttpResponse('<strong>Parâmetro 2</strong>')
    else:
        raise Http404()
        #return HttpResponseNotFound('Página não existe')

def view_dinamic_str(request, param):
    if param == 'leao':
        return HttpResponse('<strong>Você se acha</strong>')
    else:
        return HttpResponseNotFound('Página não existe')

def special_dtl(request):
    lista_de_cursos = ["ciência de dados", "matemática aplicada"]
    lista_de_signos = ['Áries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio',
    'Sagittarius', 'Capicorn', 'Aquarius', 'Pisces']
    context = {
        "nome": "Tio",
        "nome_familia": "Rafa",
        "cursos": lista_de_cursos,
        "signos": lista_de_signos
    }       
    return render(request, 'fgv/fgv-dtl.html', context) 