# ETL de Aerolíneas de Brasil
Este repositorio contiene un proyecto de ETL (Extract, Transform, Load) para procesar y analizar datos públicos de aerolíneas en Brasil. El objetivo es extraer datos de diversas fuentes públicas, transformarlos para obtener información útil y cargarlos en una base de datos para su posterior análisis.

# Tabla de Contenidos
Descripción
Características
Requisitos
Instalación
Uso
Estructura del Proyecto
Contribuciones
Licencia

# Descripción
Este proyecto de ETL se centra en la recopilación de datos públicos de aerolíneas en Brasil, incluyendo información sobre vuelos, aeropuertos, y estadísticas de rendimiento. Los datos se extraen de diversas fuentes, se transforman para limpiar y normalizar la información, y se cargan en una base de datos relacional para facilitar su análisis y visualización.

# Características
Extracción de Datos: Recopilación de datos de múltiples fuentes públicas.
Transformación de Datos: Limpieza, normalización y enriquecimiento de los datos.
Carga de Datos: Almacenamiento de los datos transformados en una base de datos relacional.
Análisis y Visualización: Scripts y notebooks para el análisis y visualización de los datos.

# Requisitos
Python 3.8+
Pandas
SQLAlchemy
Requests
Jupyter Notebook (opcional, para análisis y visualización)
PostgreSQL (o cualquier otra base de datos relacional)

# Instalación
Clona el repositorio:

bash
Edit
Copy code
git clone https://github.com/tu_usuario/etl-aerolineas-brasil.git
cd etl-aerolineas-brasil
Crea un entorno virtual e instala las dependencias:

bash
Edit
Copy code
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
Configura la base de datos en config.py:

python
Edit
Copy code
DATABASE_URI = 'postgresql://usuario:contraseña@localhost:5432/nombre_base_datos'
Uso
Ejecuta el script de extracción de datos:

bash
Edit
Copy code
python extract.py
Ejecuta el script de transformación de datos:

bash
Edit
Copy code
python transform.py
Ejecuta el script de carga de datos:

bash
Edit
Copy code
python load.py
(Opcional) Abre los notebooks de Jupyter para análisis y visualización:

bash
Edit
Copy code
jupyter notebook

# Estructura del Proyecto
Edit
Copy code
etl-aerolineas-brasil/
│
├── data/                   # Datos crudos y transformados
├── notebooks/              # Notebooks de Jupyter para análisis y visualización
├── scripts/                # Scripts de ETL
│   ├── extract.py          # Script de extracción de datos
│   ├── transform.py        # Script de transformación de datos
│   └── load.py             # Script de carga de datos
├── config.py               # Configuración del proyecto
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Este archivo

# Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría hacer.

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.