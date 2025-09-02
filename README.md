# Catálogo de Cursos Online — CRUD (Django)

![Django CI]
Proyecto CRUD con Django aplicando Scrum, XP, GitHub y CI (GitHub Actions).

## Cómo ejecutar localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Estructura
- `catalogo/` … app Django (models, views, urls, templates)
- `.github/workflows/django.yml` … pipeline de CI
- `tests/` … pruebas (pytest / Django tests)

## CI (GitHub Actions)
El workflow corre en cada **push** y **pull request**.
- Si existe `manage.py` ⇒ corre `migrate` y `python manage.py test`
- Si NO existe `manage.py` ⇒ corre `pytest` con pruebas mínimas

> Reemplaza **USUARIO** y **REPO** en el badge de arriba una vez creado el repositorio.

## Colaboración
1. Crea rama por feature (`feature/nombre`)
2. Commits pequeños y descriptivos
3. Pull Request a `main`, con revisión de un compañero
4. Merge solo si el CI pasa ✅

## Integrantes y Roles
- Scrum Master: (Frabricio)
- Dev Backend (Django): (nick camana)
- GitHub & CI/CD (tú): (luis soca)

## Evidencias sugeridas (para el video)
- PRs revisados
- Historial de commits por integrante
- Ejecuciones de CI (pestaña Actions) pasando/fallando
- README con badge verde

## Cambios de prueba para Pull Request
