from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render (request, 'index.html')


def sobre(request):
    return render (request, 'sobre.html')


def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        data = {
            'nome': nome,
            'email': email,
            'assunto': assunto,
            'mensagem': mensagem
        }
        mensagem = """
        Nova mensagem: {}
        de: {}
        """.format(data['mensagem'], data['email'])
        send_mail(data['assunto'], mensagem,'' ,['tgsoftwaresjc@gmail.com'])
        print('Mensagem enviada!')
    return render (request, 'contato.html')


def projetos(request):
    return render (request, 'projetos.html')

def infatec(request):
    return render (request, 'infatec.html')

def uol(request):
    return render (request, 'uol.html')

def appOracle(request):
    return render (request, 'appOracle.html')

def kitsune(request):
    return render (request, 'kitsune.html')

def tecsus(request):
    return render (request, 'tecsus.html')

def ionic(request):
    return render (request, 'ionic.html')

def habilidades(request):
    return render (request, 'habilidades.html')

