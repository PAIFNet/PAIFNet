from django.shortcuts import redirect

def verificar_cookie(view_func):
    def wrapper(request, *args, **kwargs):
        nome = request.COOKIES.get('nome')
        usuario = request.COOKIES.get('usuario')
        if nome and usuario:
            request.nome = nome
            request.usuario = usuario
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper