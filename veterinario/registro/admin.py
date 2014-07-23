from django.contrib import admin
from .models import Animal
from .models import Vacina
from .models import Doutor

admin.site.register(Animal)
admin.site.register(Vacina)
admin.site.register(Doutor)
