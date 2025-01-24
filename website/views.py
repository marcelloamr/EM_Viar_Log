import os
from django.conf import settings
from django.shortcuts import render
import csv
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cities(request):
    return render(request, 'cities.html')

def cubagem(request):
    return render(request, 'cubagem.html')


def cities_view(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'cidades.csv')
    cities = []

    try:
        # Leia o arquivo CSV com codificação adequada
        with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                cidade = row.get('cidade') or row.get('Cidade')
                atendimento = row.get('atendimento') or row.get('Atendimento')
                if cidade and atendimento:
                    cities.append((cidade, atendimento))
    except FileNotFoundError:
        print("Erro: Arquivo cidades.csv não encontrado.")
    except UnicodeDecodeError as e:
        print(f"Erro de decodificação: {e}")
    except KeyError as e:
        print(f"Erro: Chave {e} não encontrada no CSV.")

    # Filtrar as cidades com base na busca
    query = request.GET.get('q', '').lower()
    filtered_cities = [(cidade, atendimento) for cidade, atendimento in cities if query in cidade.lower()] if query else cities

    # Se for uma requisição AJAX, retorne JSON
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'cidades': filtered_cities[:20]})

    context = {
        'cidades': cities[:-1],  # Mostrar apenas 5 cidades inicialmente
    }
    return render(request, 'cities.html', context)