from django.views.generic. base import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ThemeForm
from .models import Theme
from django.utils import timezone 


class MainpageView(TemplateView):
    template_name = 'theme/main.html'

# Create your views here.

def themeform(request, theme =None):
    if request.method == 'POST':
        form = ThemeForm(request.POST, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.pub_date = timezone.now()
            theme.save()
            return redirect('home')
    else:
        form = ThemeForm(instance = theme)
        return render(request,'theme/new.html' , {'form':form})

def edit(request, pk):
    theme = get_object_or_404(Theme, pk=pk)
    return themeform(request,theme)

def remove(request, pk):
    theme = get_object_or_404(Theme, pk=pk)
    theme.delete()
    return redirect('home')

def main(request):
    return render(request, 'theme/main.html')

def home(request):
    themes = Theme.objects
    return render(request, 'theme/home.html', {'theme':themes})

def new(request):
    return render(request, 'theme/new.html')

def create(request):
    theme= Theme()
    theme.title = request.GET['title']
    theme.body = request.GET['body']
    theme.pub_date = timezone.datetime.now()
    theme.save()
    return redirect('/theme/home/')