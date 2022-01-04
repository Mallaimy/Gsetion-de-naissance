from django.contrib import admin
from .models import Fonctionnaire, Pere, Mere, Enfant


@admin.register(Fonctionnaire)
class FonctionAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "genre", "telephone", "poste")
    ordering = ("nom",)
    search_fields = ("nom",)


@admin.register(Pere)
class PereAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "genre",)
    ordering = ("nom",)
    search_fields = ("nom",)

@admin.register(Mere)
class MereAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "genre",)
    ordering = ("nom",)
    search_fields = ("nom",)



@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "genre",)
    ordering = ("nom",)
    search_fields = ("nom",)


