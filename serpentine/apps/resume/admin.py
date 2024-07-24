from django.contrib import admin

from .models import ContactInfo, Resume, Section, SectionItem, Skill

admin.site.register([ContactInfo, Skill, SectionItem, Section, Resume])
