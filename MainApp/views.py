from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity": 5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity": 12},
   {"id": 7, "name": "Картофель фри" ,"quantity": 0},
   {"id": 8, "name": "Кепка" ,"quantity": 124}
]


def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    result = f"""
    Имя: {author['Имя']}<br>
    Отчество: {author['Отчество']}<br>
    Фамилия: {author['Фамилия']}<br>
    телефон: {author['телефон']}<br>
    email: {author['email']}<br>
    """
    return HttpResponse(result)

def get_items(request, item_number):
    for item in items:
        if item["id"] == item_number:
            response = f"""
            <h2>Название: {item['name']}</h2>
            <p>Количество: {item['quantity']}</p>
            <p><a href="/items"> Назад к списку товаров </a></p>
            """
            return HttpResponse(response)
    return HttpResponseNotFound(f'Товар с id={item_id} не найден')
    
# <ol>
#    <li> ... </li>
#    <li> ... </li>
#    <li> ... </li>
# </ol>
def items_list(request):
    response = "<h1> Список товаров </h1><ol>"
    for item in items:
        response += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    response += "</ol>"
    return HttpResponse(response)