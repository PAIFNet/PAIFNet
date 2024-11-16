from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import firestore
from paifnet.utils.decorators import verificar_cookie
import firebase_admin
from firebase_admin import credentials

db = firestore.client()

def login(request):
    return render(request, 'login/login.html')

def recuperar(request):
    return render(request, 'recuperar/recuperar-senha.html')

@verificar_cookie
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def participantes(request):
    return render(request, 'participantes/participantes.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def grupos(request):
    return render(request, 'grupos/grupos.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def frequencia(request):
    return render(request, 'frequencia/frequencia.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def lista_de_espera(request):
    return render(request, 'lista_espera/lista_de_espera.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def suporte(request):
    return render(request, 'suporte/suporte.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def form_suporte(request):
    return render(request, 'form_suporte/form_suporte.html', {'nome': request.nome, 'usuario': request.usuario})

@verificar_cookie
def form_suporte(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        problema = request.POST.get('problema')

        try:
            # Salvar no Firestore na coleção "suporte"
            db.collection("suporte").add({
                'id': "testeid",
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'problema': problema,
            })

            # Após salvar, redireciona para uma página de confirmação ou sucesso
            return render(request, 'form_suporte/sucesso.html', {'nome': nome})
        except Exception as e:
            print(f"Erro ao salvar no Firestore: {e}")
            return render(request, 'form_suporte/form_suporte.html', {'erro': "Erro ao salvar o relato, tente novamente."})

    # Se o método não for POST, renderiza o formulário normalmente
    return render(request, 'form_suporte/form_suporte.html', {'nome': request.nome, 'usuario': request.usuario})

# Verificar login dos usuários
@csrf_exempt
def verificar_login(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        try:
            usuarios_ref = db.collection("usuarios")
            query = usuarios_ref.where("usuario", "==", usuario).where("senha", "==", senha).get()

            if query:  # Verifica se o query retornou documentos
                usuario_doc = query[0].to_dict()
                nome = usuario_doc.get('nome')

                response = redirect('/dashboard/')
                response.set_cookie('usuario', usuario, max_age=3600)  # Definindo o cookie para o usuário
                response.set_cookie('nome', nome, max_age=3600)
                return response
            else:
                # Caso não haja correspondência, retorna a página de login com uma mensagem de erro
                return render(request, 'login.html', {'erro': "Usuário ou senha inválido."})

        except Exception as e:
            print(f"Erro ao acessar o Firestore: {e}")
            return redirect('/')  # Redireciona para a página inicial em caso de erro ao acessar o banco de dados
    else:
        # Caso o método não seja POST, renderiza a página de login normalmente
        return render(request, 'login.html')

def logout(request):
    response = redirect('/')
    response.delete_cookie('usuario')
    response.delete_cookie('nome')
    return response