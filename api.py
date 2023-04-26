import requests
from bs4 import BeautifulSoup
import calendar
import locale

# Establecer la configuración regional para español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def get_uf_value(date):
    day, month, year = map(int, date.split('-'))
    # Verificar que la fecha sea válida
    if year < 2013 or month < 1 or month > 12 or day < 1 or day > 31:
        return {'error': 'Fecha no válida.'}

    # Obtener el nombre del mes
    month_name = calendar.month_name[month]

    # Obtener la tabla de valores de la UF para el año especificado
    url = f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm'
    response = requests.get(url)

    if response.status_code != 200:
        return {'error': 'No se pudo descargar la página.'}

    soup = BeautifulSoup(response.text, 'html.parser')
    # Buscar la fila correspondiente al día del mes especificado
    table = soup.find("div", class_="meses", id="mes_"+month_name)
    rows = table.find_all('tr')
    for row in rows:
        # Buscar la etiqueta "th" que contenga el día especificado
        day_th = row.find('th', text=str(day))
        if day_th:
            # Si se encontró el día, buscar la etiqueta "td" correspondiente al valor de la UF
            uf_td = day_th.find_next_sibling('td')
            return {'valor_uf': uf_td.text.strip()}
    # Si no se encontró la fila correspondiente al día del mes, devolver un error
    return {'error': 'No se encontró el valor de la UF correspondiente a la fecha ingresada.'}