## Test Unitarios

Para correr los test ejecutar `python -m unittest`

## Test e2e

### Instalar dependencias

1. Crear y Activar virtual env
```bash
python -m venv .venv
```
2. Activar virtual env
```bash
cd .venv/Scripts
. activate
cd ../..
``` 
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Instalar browsers
```bash 
playwright install
```

### Correr los test

1. Si el virtual env no esta activado, activarlo
2. Correr los test 

    a. Modo headless
    ```bash
    pytest --browser webkit
    ```
    b. Modo headed
    ```bash
    pytest --browser chromium --headed
    ```
    c. Modo lento
    ```bash
    pytest --browser chromium --headed --slowmo 400
    ```