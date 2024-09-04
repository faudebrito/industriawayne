from django.contrib import admin
from .models import Inimigos  
from .models import Equipamentos
from .models import Metas


admin.site.register(Inimigos)

admin.site.register(Equipamentos)

admin.site.register(Metas)

