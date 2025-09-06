# PathWise — Plataforma de planificación de carrera impulsada por IA

**Resumen**  
PathWise es un proyecto en Python que proporciona funcionalidades para evaluación inicial (surveys), gestión de usuarios y páginas web estáticas/plantillas orientadas a planificación de carrera y matching laboral. Repositorio: `chainchair/PathWise`. [Fuente](https://github.com/chainchair/PathWise/tree/main)

---

## Tabla de contenidos
- [Características](#características)  
- [Tecnologías](#tecnologías)  
- [Requisitos](#requisitos)  
- [Instalación rápida](#instalación-rápida)  
- [creacion del archivo de entorno](#creacion-del-archivo-de-entorno)  
- [API key](#api-key)  
- [ejecucion](#ejecucion)  



---

## Características
- Formularios/encuestas iniciales para perfilado profesional.  
- Interfaz web con templates y assets estáticos.  
- Gestión de usuarios (carpeta `users`).  
- Páginas de inicio y roadmap incluidos.  

> Estas características se infieren de la estructura del repo y archivos presentes en la rama `main`.

---

## Tecnologías
- Python (aplicación backend).  
- HTML + templates (carpeta `templates`).  
- CSS en `static/css`.  
- Archivo de entrada `manage.py`.  

> (Lenguajes principales en el repositorio: Python, HTML, CSS).

---

## Requisitos
- Python 3.10+ (recomendado).  
- `pip` para instalar dependencias.  
- Base de datos compatible (SQLite por defecto).

---

## Instalación rápida
```bash
# clonar repo
git clone https://github.com/chainchair/PathWise.git
cd PathWise

# crear entorno virtual
python -m venv venv
# Windows
# venv\Scripts\activate
# Unix / macOS
source venv/bin/activate

# instalar dependencias
pip install -r requirements.txt
```

## creacion del archivo de entorno
defina un archivo .env con lo siguiente en la raiz de su proyecto
OPENAI_API_KEY=sk-proj-apikey
DEBUG=True

###API key 
para crear la api key entre a este enlace
https://platform.openai.com/api-keys

## ejecucion
### migraciones
```bash
python manage.py migrate
```

### crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### ejecutar servidor de desarrollo
```bash
python manage.py runserver
```
