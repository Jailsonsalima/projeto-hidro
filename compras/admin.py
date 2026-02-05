from django.contrib import admin

# Register your models here.

from .models import ListaCompra, ItemListaCompra, LogAlteracaoLista

@admin.register(ListaCompra)
class ListaCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'empresa', 'status', 'criado_por', 'data_criacao')
    list_filter = ('status', 'empresa')
    search_fields = ('numero',)

@admin.register(ItemListaCompra)
class ItemListaCompraAdmin(admin.ModelAdmin):
    list_display = ('id','lista', 'produto', 'quantidade_desejada', 'preco_unitario')
    list_filter = ('lista', 'produto')

@admin.register(LogAlteracaoLista)
class LogAlteracaoListaAdmin(admin.ModelAdmin):
    list_display = ('id','lista', 'produto', 'alterado_por', 'quantidade_antiga', 'quantidade_nova', 'data_hora')
    list_filter = ('lista', 'alterado_por')