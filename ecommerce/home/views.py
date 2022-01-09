from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Setting, ContactForm,ContactFormMessage
from product.models import Product


# Create your views here.
def index(request):
  setting= Setting.objects.get(pk=1)
  sliderData = Product.objects.all()[:4];
  context = {'setting': setting, 'page': 'home', 'sliderData': sliderData}
  return render(request, 'index.html', context)

def about(request):
  setting= Setting.objects.get(pk=1)
  context = {'setting': setting}
  return render(request, 'about.html', context)

def references(request):
  setting= Setting.objects.get(pk=1)
  context = {'setting': setting}
  return render(request, 'references.html', context)

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    
    if form.is_valid():
      data = ContactFormMessage()
      data.name = form.cleaned_data['name']
      data.email = form.cleaned_data['email']
      data.subjecrt = form.cleaned_data['subject']
      data.message = form.cleaned_data['message']
      data.ip = request.META.get('REMOTE_ADDR')
      data.save()
      # messages.success(request, 'Mesaıjınız başarı ile gönderilmiştir. Teşekkür ederiz.')
      return HttpResponseRedirect('/contact')
      
    
  setting= Setting.objects.get(pk=1)
  form = ContactForm()
  context = {'setting': setting, 'form': form}
  return render(request, 'contact.html', context)
