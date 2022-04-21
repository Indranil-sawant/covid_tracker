from datetime import date
from django.contrib import admin

from . import models


admin.site.register(models.Data)