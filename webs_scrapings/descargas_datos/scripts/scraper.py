# pylint: disable=relative-beyond-top-level, unused-import
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .iniciar_webdriver_uc import iniciar_webdriver
from ..models import Scraper
import io
import sys


def scraper_data(scrape_parametros):

    start_time = time.time()
    driver = iniciar_webdriver(headless=True, pos="izquierda")
    wait = WebDriverWait(driver, 10)

    url_inicial = scrape_parametros['url_inicial']
    url_base = scrape_parametros['url_base']
    selector_enlace = scrape_parametros['selector_enlace']
    selector_articulo = scrape_parametros['selector_articulo']
    selector_titulo = scrape_parametros['selector_titulo']

    dic_links = {}

    driver.get(url_inicial)
    comprobar_si_langgarph(url_inicial, wait, dic_links,
                           url_base, selector_enlace)
    print("INICIANDO CICLO DE LECTURA DE LINKS")

    while any(not dic_links[k]["visited"] for k in dic_links.keys()):
        for s, k in enumerate(list(dic_links.keys())):
            if not dic_links[k]["visited"]:
                print(
                    f"YA EXISTE EN EL DICCIONARIO PERO VAMOS A COMPROBAR SI HAY ALGO DENTRO QUE NOS SIRVA {s}")
                visitar_y_filtrar(k, dic_links, url_base, driver,
                                  wait, selector_enlace, selector_articulo, selector_titulo)

    driver.quit()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"El tiempo total de ejecución es: {elapsed_time} segundos")
    print(len(dic_links))


def comprobar_si_langgarph(url_inicial, wait, dic_links, url_base, selector_enlace):
    if url_base in url_inicial:
        filtrar_a(url_base, dic_links, wait, selector_enlace)


def filtrar_a(url_base, dic_links, wait, selector_enlace):
    try:
        links_menus = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector_enlace)))
        for i in links_menus:
            link = i.get_attribute('href')
            if link:
                base_link = link.split('?')[0]
                if '.' in base_link[-6:] and not base_link.endswith('.ipynb'):
                    continue
                if base_link.startswith(url_base) and '#' not in link:
                    if link.endswith('.ipynb'):
                        base_link = link[:link.rfind('/')]
                    if base_link not in dic_links:
                        print(f"Añadiendo link al diccionario: {base_link}")
                        dic_links[base_link] = {"visited": False}
    except Exception as e:
        print(f"Error filtrando enlaces: {e}")


def visitar_y_filtrar(url_inicial, dic_links, url_base, driver, wait, selector_enlace, selector_articulo="article", selector_titulo="article h1"):
    driver.get(url_inicial)
    comprobar_si_langgarph(url_inicial, wait, dic_links,
                           url_base, selector_enlace)

    try:
        title_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector_titulo)))
        title = title_element.text if title_element else "No title"
    except Exception as e:
        print(f"Error obteniendo el título en {url_inicial}")
        title = "No title"

    try:
        content_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector_articulo)))
        content = content_element.text if content_element else "No content"
    except Exception as e:
        print(f"Error obteniendo el contenido en {url_inicial}")
        content = "No content"

    # Limpiar los datos para eliminar los bytes NUL
    title = title.replace('\0', '')
    content = content.replace('\0', '')

    dic_links[url_inicial] = {
        "visited": True,
        "title": title,
        "content": content
    }

    # Impresiones de depuración
    print(
        f"Guardando en DB: {url_inicial}, Título: {title}, Artículo: {content[:100]}")

    try:
        scraper_instance, created = Scraper.objects.get_or_create(
            url=url_inicial,
            defaults={
                'titulo': title[:255],
                'articulo': content,
                'visitado': True
            }
        )
        if created:
            print(f"Nuevo registro creado para {url_inicial}")
        else:
            print(f"Registro existente actualizado para {url_inicial}")
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")
