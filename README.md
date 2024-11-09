# ExamenAPI
## Configuración del Entorno y Ejecucion del Proyecto
# Prerrequisitos
Asegúrate de tener instalados los siguientes requisitos en tu máquina:

-Python 3.x
-pip (la herramienta de instalación de paquetes de Python)
-virtualenv (para crear entornos virtuales)

## Para crear y activar el entorno Virtual con git bash  e instalar las dependencias del requirements.txt 

virtualenv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python app.py

## Resolución de la parte Teorica del Examen

# 1. Para qué se puede usar Python en lo que respecta a datos. Dar 5 casos y explicar brevemente

-Análisis de Datos con Pandas:
Python, a través de pandas, permite realizar análisis de datos potentes y flexibles, lectura y manipulación de datos, limpieza de datos, transformación de datos y análisis estadístico

-Visualización de Datos
A través de bibliotecas como: matplotlib, seaborn, plotly, etc permiten crear desde simples gráficos de barras hasta visualizaciones interactivas.

-Machine Learning con Scikit-learn
Python es fundamental en machine learning: Modelos de clasificación y regresión, Clustering y reducción de dimensionalidad, Validación cruzada y evaluación de modelos, Procesamiento de características.

-Procesamiento Numérico con NumPy
Esto es crucial para: Procesamiento de imágenes, Cálculos científicos, Operaciones matriciales.

-Automatización de Análisis
Python permite automatizar tareas repetitivas: Scraping web para recolección de datos, Generación automática de reportes, Actualización periódica de dashboards, Procesamiento batch de datos.

# 2. ¿Cómo se diferencian Flask de Django? Argumentar. 

Flask y Django son dos frameworks de Python para desarrollo web con características distintivas: Flask es un microframework ligero y minimalista que ofrece alta flexibilidad y control sobre los componentes, con una curva de aprendizaje inicial más accesible, siendo ideal para proyectos pequeños, APIs y microservicios; mientras que Django es un framework completo y robusto que incluye numerosas funcionalidades integradas, proporciona una estructura de proyecto predefinida y ofrece herramientas como admin panel y autenticación incorporada, lo que lo hace más adecuado para aplicaciones grandes y complejas.

# 3.  ¿Qué es un API? Explicar en sus propias palabras 

Un API es un conjunto de reglas que permite que diferentes aplicaciones se comuniquen entre sí, como un traductor universal que ayuda a que diferentes sistemas informáticos puedan entenderse y compartir información de manera ordenada y segura.

# 4. ¿Cuál es la principal diferencia entre REST y WebSockets? 

La principal diferencia entre REST y WebSockets radica en su modelo de comunicación y manejo de conexiones: REST es un estilo de arquitectura que utiliza HTTP para realizar operaciones CRUD mediante un modelo de petición-respuesta donde cada interacción es independiente y stateless (sin estado), utilizando métodos HTTP estándar como GET, POST, PUT y DELETE, siendo ideal para operaciones discretas y aplicaciones donde la latencia no es crítica.

Mientras WebSockets establece una conexión bidireccional persistente (stateful) entre cliente y servidor, permitiendo que ambas partes envíen mensajes en cualquier momento sin necesidad de establecer nuevas conexiones, lo que lo hace especialmente eficiente para aplicaciones en tiempo real como chats, juegos en línea o actualizaciones en vivo, reduciendo la latencia y la sobrecarga de comunicación al mantener una única conexión abierta.

# Describir un ejemplo de API comercial y como funciona – usar otros ejemplos no vistos en el curso.

Ejemplo de API Comercial: Twilio

La API de Twilio es una plataforma de comunicación en la nube que permite a las aplicaciones enviar y recibir mensajes de texto, realizar y recibir llamadas telefónicas, y gestionar otros servicios de comunicación. Es ampliamente utilizada por empresas para integrar capacidades de comunicación en sus aplicaciones y servicios.

Funcionamiento de la API de Twilio

Envío de Mensajes de Texto

Realización de Llamadas Telefónicas

Recepción de Mensajes y Llamadas

Verificación de Usuarios

Integración con Aplicaciones
