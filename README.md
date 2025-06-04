Proyecto de Automatización de Pruebas - Automation Exercise
Este proyecto implementa una suite de pruebas de automatización de extremo a extremo para el sitio web "Automation Exercise". El objetivo principal es validar el flujo de usuario a través de funcionalidades clave como el registro, la navegación de productos, la búsqueda, el filtrado, la adición al carrito y el proceso de compra.

La arquitectura se basa en el Patrón Screenplay, buscando un equilibrio entre legibilidad, mantenibilidad, escalabilidad y eficiencia de recursos, especialmente considerando las limitaciones de almacenamiento en disco.

🚀 Requisitos Previos
Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

Python 3.8+: Se recomienda la última versión estable de Python.

pip: El gestor de paquetes de Python (generalmente viene con Python).

venv: Módulo para crear entornos virtuales (generalmente viene con Python).

Allure Commandline: Herramienta para generar y servir los reportes de Allure.

Puedes encontrar las instrucciones de instalación en la documentación oficial de Allure.

Navegador Web: Chrome (se recomienda tener la última versión).

📦 Instalación del Proyecto
Sigue estos pasos para configurar el proyecto localmente:

Clonar el Repositorio:

git clone <URL_DE_TU_REPOSITORIO>
cd tu_nombre_del_proyecto

Crear y Activar un Entorno Virtual:
Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto.

python -m venv .venv

En Windows:

.venv\Scripts\activate

En macOS/Linux:

source .venv/bin/activate

Instalar Dependencias:
Con el entorno virtual activado, instala todas las librerías necesarias:

pip install -r requirements.txt

⚙️ Configuración
Este proyecto utiliza variables de entorno para la URL base del sitio.

BASE_URL: La URL principal del sitio web bajo prueba (por defecto: https://www.automationexercise.com/).

Puedes configurar estas variables creando un archivo .env en la raíz del proyecto.

Ejemplo de .env:

BASE_URL=https://www.automationexercise.com/
# Otras credenciales o configuraciones sensibles aquí (NO SUBIR A GIT)

Nota: Asegúrate de que tu archivo .gitignore contenga .env para evitar subir información sensible al repositorio.

▶️ Cómo Ejecutar las Pruebas
Para ejecutar el flujo completo de pruebas y generar los resultados para Allure Reports, utiliza el siguiente comando desde la raíz del proyecto (con el entorno virtual activado):

behave features/flujoCompleto.feature --no-capture -f allure_behave.formatter:AllureFormatter -o allure-results

behave features/flujoCompleto.feature: Ejecuta el archivo de característica flujoCompleto.feature. Si has separado tus características en múltiples archivos (ej. features/registro_usuario.feature, features/busqueda_de_productos.feature), puedes ejecutar todas las pruebas usando behave features/.

--no-capture: Evita que Behave capture la salida estándar, permitiendo ver los print() de depuración en la consola.

-f allure_behave.formatter:AllureFormatter -o allure-results: Configura Behave para usar el formateador de Allure y guardar los resultados brutos en la carpeta allure-results.

📊 Cómo Ver los Reportes de Allure
Después de ejecutar las pruebas, puedes generar y abrir el reporte HTML interactivo de Allure:

Generar el Reporte HTML:

allure generate allure-results --clean -o allure-report

allure-results: La carpeta donde se guardaron los resultados brutos.

--clean: Limpia cualquier reporte anterior antes de generar uno nuevo.

-o allure-report: Especifica la carpeta de salida para el reporte HTML generado.

Abrir el Reporte en el Navegador:

allure open allure-report

Esto lanzará un servidor web local y abrirá el reporte en tu navegador predeterminado.

📂 Estructura del Proyecto
El proyecto sigue el Patrón Screenplay para una organización modular y mantenible:

your_project/
├── features/
│   ├── steps/                # Definiciones de los pasos de Gherkin (ej. busquedaSteps.py)
│   └── *.feature             # Archivos Gherkin que describen los escenarios de prueba
├── actors/                   # Define la entidad 'Actor' que interactúa con el sistema
├── abilities/                # Define las capacidades del Actor (ej. BrowseTheWeb para Selenium)
├── tasks/                    # Acciones de alto nivel que el Actor realiza (el 'qué')
├── interactions/             # Acciones de bajo nivel que componen las tareas (el 'cómo')
├── questions/                # Preguntas que el Actor hace para verificar el estado del sistema
├── ui/                       # Repositorio de localizadores de elementos de la interfaz de usuario
├── exceptions/               # Excepciones personalizadas para un manejo de errores claro
├── utils/                    # Utilidades generales (ej. DriverFactory para el WebDriver)
├── .gitignore                # Archivo para Git que ignora carpetas y archivos no deseados
├── requirements.txt          # Lista de dependencias de Python del proyecto
└── README.md                 # Este archivo

💡 Consideraciones Adicionales
WebDriver Manager: La librería webdriver_manager se utiliza para gestionar automáticamente los drivers del navegador. Esto significa que no necesitas descargar chromedriver.exe manualmente; la librería lo hará por ti, simplificando la configuración inicial y el mantenimiento.

Optimización de Espacio en Disco: La elección de Python y Behave, junto con el uso de entornos virtuales y la configuración adecuada de .gitignore, minimiza la huella de almacenamiento del proyecto en comparación con frameworks basados en Java (como Cucumber/Serenity BDD) que a menudo requieren una JVM y descargan grandes cantidades de dependencias.

Manejo de Anuncios: Se han implementado estrategias para manejar anuncios intrusivos (ej. configuración de opciones del navegador, posibles scrolls o reintentos en las interacciones) para mejorar la estabilidad de las pruebas en diferentes resoluciones de pantalla. Se recomienda, si es posible, deshabilitar la carga de anuncios en entornos de prueba para una mayor fiabilidad.

¡Esperamos que este README.md sea una guía útil para el uso y la comprensión del proyecto!
