from django.contrib import admin

# Register your models here.
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'fornecedor', 'preco', 'descricao', 'imagem')
    list_filter = ('fornecedor',)
    search_fields = ('nome',)