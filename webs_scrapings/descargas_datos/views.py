# pylint: disable=no-member
from django.shortcuts import render
from .forms import LinkForm
from .scripts.scraper import scraper_data


def index(request):
    if request.method == 'GET':
        form = LinkForm()
        context = {
            'form': form
        }
        return render(request, 'descargas_datos/index.html', context)
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            # Almacenar los datos en un diccionario
            scrape_parametros = {
                'url_inicial': form.cleaned_data['url_inicial'],
                'url_base': form.cleaned_data['url_base'],
                'selector_enlace': form.cleaned_data['selector_enlace'],
                'selector_articulo': form.cleaned_data['selector_articulo'],
                'selector_titulo': form.cleaned_data['selector_titulo']
            }

            scraper_data(scrape_parametros)

            context = {
            }
            return render(request, 'descargas_datos/success.html', context)
