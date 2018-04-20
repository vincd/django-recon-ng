Django Recon-ng
===============

Display Recon-ng data on the Django Admin interface.

## Quick start

Install Django Recon-ng:
```
pip install django-recon-ng
```

Edit your Django settings file:
```python

INSTALLED_APPS = [
    '...',
    'django_recon_ng'
]

# add the sqlite recon-ng database named 'recon_db'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'recon_db': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '~\.recon-ng\workspaces\default\data.db'),
    }
}

# add a database router to handle read/write operations
DATABASE_ROUTERS = ('django_recon_ng.dbrouters.ReconNGDBRouter', )

# say to our module the name of the database
RECON_NG_DATABASE_NAME = 'recon_db'
```
