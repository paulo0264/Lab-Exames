from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if not senha == confirmar_senha:
            return redirect('/usuarios/cadastro')
        if len(senha) < 6:
            return redirect('/usuarios/cadastro')
        try:
            # Username deve ser único!
            user = User.objects.create_user(
            first_name=primeiro_nome,
            last_name=ultimo_nome,
            username=username,
            email=email,
            password=senha,
        )
        except:
            return redirect('/usuarios/cadastro')
        return redirect('/usuarios/cadastro')
