# Diagnóstico del proyecto heredado

Ejecutamos `app.py` tal como venía y lo probamos con distintos datos. Estos son los problemas encontrados:

| # | Problema | Cómo se reproduce | Causa | Corrección |
|---|---|---|---|---|
| 1 | Solo funciona desde su propia carpeta | Ejecutar `python proyecto_heredado/app.py` desde la carpeta superior → `FileNotFoundError: 'ventas.csv'` | La ruta `'ventas.csv'` es relativa a la carpeta desde la que se ejecuta, no al proyecto | Ruta configurable con `ARCHIVO_VENTAS` y, por defecto, calculada desde la raíz del proyecto (`config.py`) |
| 2 | Se rompe con un archivo sin datos | CSV solo con la cabecera `ventas` → `ZeroDivisionError: division by zero` | `estimar()` divide entre `len(valores)` sin comprobar que haya valores | `estimar_demanda()` lanza `ValueError("No hay ventas…")` con un mensaje claro |
| 3 | Acepta ventas negativas | CSV con `-10` y `-20` → `Demanda prevista: -16.5` | No hay ninguna validación de los datos | Se rechazan valores negativos con `ValueError` |
| 4 | Se rompe con un valor no numérico | CSV con `abc` → `ValueError: could not convert string to float` sin indicar dónde | `float()` sin control de errores | `leer_ventas()` indica la fila con el problema: `Valor no numérico en la fila 3: 'abc'` |
| 5 | Configuración mezclada con la lógica | El factor `1.1` y el nombre del archivo están escritos dentro del código | No hay configuración externa | Variables de entorno `FACTOR_DEMANDA` y `ARCHIVO_VENTAS`, con validación del factor |
| 6 | Lectura, cálculo y salida en la misma función | `ejecutar()` abre el archivo, calcula e imprime | Código monolítico, imposible de probar por partes | Módulos separados: `datos.py`, `calculo.py`, `config.py`, `main.py` |
| 7 | Avisos de calidad | `ruff check app.py` → `F401 'os' imported but unused` e imports desordenados | Import sin usar | Ruff sin errores en todo el proyecto |
| 8 | No es reproducible | No hay `requirements.txt`, `.gitignore`, README, entorno virtual ni pruebas | Proyecto pensado solo para el equipo del autor | `.venv` + `requirements.txt` con versiones fijas + `pyproject.toml` + README + 12 pruebas con pytest |
