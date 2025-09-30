# 📝 Blog API con FastAPI

Este proyecto implementa una API de **usuarios, posts y comentarios** utilizando **FastAPI** y **SQLAlchemy**.  
Está pensado para aprender y practicar buenas prácticas en desarrollo backend con Python.

---

## ⚙️ Instalación

Clonar repositorio  
```bash
git clone https://github.com/tuusuario/blog-api.git
cd blog-api
```
Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instalar dependencias
```bash
pip install -r requirements.txt
```

Variables de entorno (.env)
```bash
DATABASE_URL=sqlite:///./blog.db
```

Ejecutar servidor
```bash
uvicorn app.main:app --reload
```


