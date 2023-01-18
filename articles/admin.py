from django.contrib import admin

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:

            if form.cleaned_data['is_main'] == True:
                counter += 1
        if counter == 0:
            raise ValidationError('Выберите основной раздел')
        elif counter > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()

class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInLineFormset
    extra = 0
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]
    list_display = ['id', 'title', 'text']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']