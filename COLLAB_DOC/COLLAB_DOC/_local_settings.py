from COLLAB_DOC.settings import *

# template to create local_settings.py in order to not share secret configs
# override only local changes such as databases
# run with makefile

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "collab_doc",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
