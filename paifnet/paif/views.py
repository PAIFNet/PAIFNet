from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import firestore

db = firestore.client()

# Direcionar o usuário para tela de login
def login(request):
    return render(request, 'login/login.html')

# Direcionar o usuário para tela de Recuperação de Senha 
def recuperar(request):
    return render(request, 'recuperar/recuperar-senha.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

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

def dashboard(request):
    nome = request.COOKIES.get('nome')
    if nome:
        return render(request, 'dashboard/dashboard.html', {'nome': nome})
    else:
        return redirect('/login/')