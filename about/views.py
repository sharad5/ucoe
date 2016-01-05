from django.shortcuts import render
from django.utils import timezone
from .models import About_home
from .models import Dept_history
from .models import Infrastructure
from .models import Labs
from .models import Hostel

def about(request):
    posts = About_home.objects.order_by('published_date')
    return render(request, 'about/about.html', {})