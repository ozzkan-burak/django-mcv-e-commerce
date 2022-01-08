from django.db import models
from django.db.models import fields
from ckeditor_uploader.fields import RichTextUploadingField

from django.forms import ModelForm, Textarea, TextInput
class Setting(models.Model):
  STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
  )
  title = models.CharField(max_length=30)
  keywords = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  company = models.CharField(blank=True,max_length=50)
  adress = models.CharField(blank=True,max_length=150)
  phone = models.CharField(blank=True,max_length=15)
  fax = models.CharField(blank=True,max_length=15)
  email = models.CharField(max_length=30)
  smtpserver = models.CharField(max_length=20)
  smtpmail = models.CharField(max_length=20)
  smtppassword = models.CharField(max_length=10)
  smtpport = models.CharField(blank=True,max_length=5)
  icon = models.ImageField(blank=True, upload_to='images/')
  facebook = models.CharField(blank=True,max_length=50)
  instagram = models.CharField(blank=True,max_length=50)
  twitter = models.CharField(blank=True,max_length=50)
  aboutus = RichTextUploadingField(blank=True)
  contact = RichTextUploadingField(blank=True)
  references = RichTextUploadingField(blank=True)
  status = models.CharField(max_length=10, choices=STATUS)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.title
  
class ContactFormMessage(models.Model):
  STATUS = (
    ('New', 'Yeni'),
    ('Read', 'Okundu'),
    ('Closed', 'Kapandı'),
  )
  name = models.CharField(blank=True,max_length=20)
  email = models.CharField(blank=True,max_length=50)
  subject = models.CharField(blank=True,max_length=50)
  message = models.CharField(blank=True,max_length=255)
  status = models.CharField(max_length=10, choices=STATUS, default='New')
  ip = models.CharField(blank=True,max_length=20)
  note = models.CharField(blank=True,max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
  
class ContactForm(ModelForm):
  class Meta:
    model = ContactFormMessage
    fields = ['name', 'subject', 'email', 'message']
    widgets = {
      'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız Soyadınız'}),
      'subject': TextInput(attrs={'class': 'form-control', 'placeholder': 'Konu'}),
      'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'E-posta'}),
      'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesajınız'}),
    }
  
  def __str__(self):
    return self.title