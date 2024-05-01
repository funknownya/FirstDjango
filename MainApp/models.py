from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self) -> str:
        return f"Color({self.name})"


class Item(models.Model):
    name  = models.CharField(max_length=100, verbose_name='Имя')
    brand = models.CharField(max_length=100, verbose_name='Бренд')
    count = models.PositiveIntegerField(verbose_name="Количество") 
    description = models.TextField(max_length=200, default="Базовое описание товара")
    colors = models.ManyToManyField(to=Color)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.brand}, {self.count})"
    
    def display_colors(self):
        return ", ".join(color.name for color in self.colors.all())
    
    display_colors.short_description = "Цвета"