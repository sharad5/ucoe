from django.contrib import admin
from .models import About_home
from .models import Dept_history
from .models import Infrastructure
from .models import Labs
from .models import Hostel

admin.site.register(About_home)
admin.site.register(Dept_history)
admin.site.register(Infrastructure)
admin.site.register(Labs)
admin.site.register(Hostel)