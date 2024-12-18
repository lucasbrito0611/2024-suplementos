import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from loja.models import Cartao, Cliente


@login_required
def list_carteira_view(request):
    return render(request, template_name='Perfil/carteira.html', status=200) 

@login_required
def adicionar_cartao_view(request):
    user = request.user
    cliente = Cliente.objects.get(user=user)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        nometitular = request.POST.get('nometitular')
        numero = request.POST.get('numero')
        tipo = request.POST.get('tipo')

        cartoes_cliente = Cartao.objects.filter(cliente=user.cliente)
        cartao_existe = cartoes_cliente.filter(numero=numero).exists()

        if nome and nometitular and numero and tipo:
            numero_bin = numero[:6] 
            url = f"https://api.pagar.me/bin/v1/{numero_bin}"

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    dados = response.json()
                    bandeira = dados.get('brandName', 'Desconhecido')

                    if cartao_existe:
                        messages.error(request, 'Você já possui esse cartão.', extra_tags='novo-cartao')
                        return redirect(reverse('minha-carteira'))
                    else:
                        if tipo == 'debito':
                            Cartao.objects.create(cliente=cliente, nome=nome, nometitular=nometitular, numero=numero, bandeira=bandeira, tipo='debito')

                            messages.success(request, 'Cartão adicionado com sucesso!', extra_tags='novo-cartao')
                            return redirect(reverse('minha-carteira'))
                        elif tipo == 'credito':
                            Cartao.objects.create(cliente=cliente, nome=nome, nometitular=nometitular, numero=numero, bandeira=bandeira, tipo='credito')

                            messages.success(request, 'Cartão adicionado com sucesso!', extra_tags='novo-cartao')
                            return redirect(reverse('minha-carteira'))
                else:
                    messages.error(request, 'Cartão não encontrado.', extra_tags='novo-cartao')

            except Exception as e:
                context = {'success': False, 'error': f'Erro ao consultar a API: {e}'}
        else:
            messages.error(request, 'Preencha os campos obrigatórios. (*)', extra_tags='novo-cartao')

    return render(request, template_name='Perfil/carteira.html', status=200) 