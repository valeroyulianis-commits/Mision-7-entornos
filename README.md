# Misión 7 · Estimador de demanda 📈

Helloo 👋 Este proyecto estima la demanda de un producto a partir de sus ventas recientes: saca la media de las ventas y le aplica un factor de crecimiento (1.1 por defecto).

Partimos de un proyecto heredado que solo funcionaba en el ordenador de su autor. Lo reorganizamos para que se pueda instalar desde cero, configurar sin tocar el código y comprobar con pruebas automáticas. Los problemas que encontramos están en `diagnostico.md`.

## Requisitos
- Python 3.10 o superior (lo probamos con 3.12).
- Git.

## Instalación desde cero

**1. Clona el repo y entra en la carpeta:**
```bash
git clone https://github.com/valeroyulianis-commits/mision-7-entornos.git
cd mision-7-entornos
```

**2. Crea y activa el entorno virtual:**
```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```
Sabrás que está activo porque la terminal empieza con `(.venv)`.

> Si PowerShell no te deja activarlo (error de *execution policy*), ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a intentarlo.

**3. Instala las herramientas y el proyecto:**
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```
El primero instala pytest y Ruff con versiones fijas; el segundo instala nuestro paquete `demanda` en modo editable.

**4. Ejecuta:**
```bash
demanda
```
Respuesta esperada:
```
Archivo: ...\mision-7-entornos\data\ventas.csv
Registros: 3 · Factor: 1.1
Demanda prevista: 22.0
```

## Configuración (sin tocar el código)

| Variable | Para qué sirve | Por defecto |
|---|---|---|
| `FACTOR_DEMANDA` | Factor de crecimiento (debe ser mayor que 0) | `1.1` |
| `ARCHIVO_VENTAS` | Ruta al CSV con una columna `ventas` | `data/ventas.csv` |

```powershell
# Windows (PowerShell)
$env:FACTOR_DEMANDA = "1.5"
demanda
```
```bash
# macOS / Linux
FACTOR_DEMANDA=1.5 demanda
```

## Comprobaciones de calidad
```bash
python -m pytest -q      # 12 pruebas
ruff check .             # revisión del código
ruff format --check .    # formato
```

## Estructura
```
mision-7-entornos/
├── src/demanda/
│   ├── calculo.py    # lógica de negocio: estimar_demanda()
│   ├── datos.py      # entrada: leer y validar el CSV
│   ├── config.py     # variables de entorno
│   └── main.py       # une todo y muestra el resultado
├── tests/            # pruebas con pytest
├── data/ventas.csv   # datos de ejemplo
├── pyproject.toml    # paquete + configuración de pytest y Ruff
├── requirements.txt  # herramientas con versión fija
├── diagnostico.md    # problemas del proyecto heredado
└── evidencias.md
```

## Si algo no sale a la primera

| Lo que ves | Qué hacer |
|---|---|
| `demanda` no se reconoce | Activa el `.venv` (paso 2) y repite `python -m pip install -e .` |
| `Error: FACTOR_DEMANDA debe ser…` | Revisa el valor de la variable; para quitarla en PowerShell: `Remove-Item Env:FACTOR_DEMANDA` |
| `Error: No se encuentra el archivo…` | Revisa `ARCHIVO_VENTAS` o quítala para usar el archivo por defecto |
| VS Code no reconoce los imports | `Ctrl+Shift+P` → **Python: Select Interpreter** → el de `.venv` |

*Yulianis Valero y Yuleimis Valero*
