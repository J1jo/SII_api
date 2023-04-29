
# SII_api

SII_api consiste en una API en Python que permite a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica.




## Como Funciona:

- La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.
- El formato fecha es dd:mm:yyyy
- La respuesta de la API es en formato JSON.
- La API devuelve el valor de la Unidad de Fomento correspondiente a la fecha consultada.



## Prerrequisitos

- Clonar el repositorio

## Como ejecutar el proyecto?

### 1.- Debes clonar el proyecto

```bash
  git clone https://github.com/J1jo/SII_api.git
```

### 2.- Crear ambiente virtual

```bash
  python -m venv env
  env\Scripts\activate
```

### 3.- Casos de prueba

En la raíz se encuentra una carpeta llamada `tests` dentro de ella un archivo llamado `test_api.py`, desde el cual se hacen pruebas unitarias. Para probar diferentes casos es necesario modificar este archivo.
## Ejecutar pruebas

*Para poder ejecutar las pruebas deberá ejecutar el siguiente comando*

```bash
  python -m unittest discover -s tests/
```
