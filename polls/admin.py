from django.contrib import admin
from . import models

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['publish_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
