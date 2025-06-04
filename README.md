# Proyecto de Automatización de Pruebas - Automation Exercise

Este proyecto implementa una suite de pruebas de automatización de extremo a extremo para el sitio web **Automation Exercise**. El objetivo principal es validar el flujo de usuario a través de funcionalidades clave como:

- Registro  
- Navegación de productos  
- Búsqueda y filtrado  
- Adición al carrito  
- Proceso de compra

La arquitectura se basa en el **Patrón Screenplay**, buscando un equilibrio entre legibilidad, mantenibilidad y eficiencia.

---

## Tabla de Contenidos

- [🚀 Requisitos Previos](#-requisitos-previos)  
- [📦 Instalación del Proyecto](#-instalación-del-proyecto)  
- [⚙️ Configuración](#️-configuración)  
- [▶️ Cómo Ejecutar las Pruebas](#️-cómo-ejecutar-las-pruebas)  
- [📊 Cómo Ver los Reportes de Allure](#-cómo-ver-los-reportes-de-allure)  
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)  
- [💡 Consideraciones Adicionales](#-consideraciones-adicionales)  
- [✅ Estado del Proyecto](#-estado-del-proyecto)  
- [📄 Licencia](#-licencia)

---

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

- **Python 3.8+**
- **pip** (ya viene con Python)
- **venv** (también viene con Python)
- **Allure Commandline** → [Instrucciones oficiales](https://docs.qameta.io/allure/)
- **Navegador web:** Google Chrome (última versión)

---

## Instalación del Proyecto

### Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd tu_nombre_del_proyecto
```

### Crear y activar un entorno virtual

```bash
python -m venv .venv
```

#### En Windows:

```bash
.venv\Scripts\activate
```

#### En macOS/Linux:

```bash
source .venv/bin/activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

El proyecto utiliza variables de entorno para configurar la URL base del sitio.

Crea un archivo `.env` en la raíz del proyecto:

```env
BASE_URL=https://www.automationexercise.com/
# Otras credenciales o configuraciones sensibles aquí
```

> ⚠Asegúrate de agregar `.env` a tu archivo `.gitignore` para evitar subirlo al repositorio.

---

## Cómo Ejecutar las Pruebas

Desde la raíz del proyecto (con el entorno virtual activado):

```bash
behave features/flujoCompleto.feature --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results
```

**Detalles del comando:**

- `behave features/flujoCompleto.feature`: Ejecuta ese archivo `.feature`.
- `--no-capture`: Muestra los `print()` de depuración.
- `-f allure_behave.formatter:AllureFormatter -o allure-results`: Usa Allure para generar resultados.

---

## Cómo Ver los Reportes de Allure

### Generar el reporte HTML:

```bash
allure generate allure-results --clean -o allure-report
```

### Abrir el reporte:

```bash
allure open allure-report
```

Esto abrirá el reporte en tu navegador predeterminado.

---

## Estructura del Proyecto

```
your_project/
├── features/
│   ├── steps/                # Definiciones de pasos Gherkin
│   └── *.feature             # Escenarios de prueba
├── actors/                   # Definición del 'Actor'
├── abilities/                # Capacidades del actor (ej: BrowseTheWeb)
├── tasks/                    # Qué hace el actor
├── interactions/             # Cómo lo hace
├── questions/                # Verificaciones
├── ui/                       # Localizadores de elementos
├── exceptions/               # Excepciones personalizadas
├── utils/                    # Utilidades generales
├── .gitignore                # Archivos a ignorar por Git
├── requirements.txt          # Dependencias
└── README.md                 # Este archivo
```
