from core.models import Task
import random


def populate():
    actions = [
        'Купить',
        'Продать',
        'Принести',
        'Отдать',
        'Забрать',
        'Сделать',
    ]
    goods = [
        'молоко',
        'хлеб',
        'телефон',
        'шкаф',
        'рюкзак',
        'ключ',
    ]
    todolist = []
    items_qty = random.randint(3, 6)
    count = 0
    while (count < items_qty):
        todo_item = ' '.join([random.choice(actions), random.choice(goods)])
        if todo_item not in todolist:
            todolist.append(todo_item)
            count += 1
    for item in todolist:
        Task(title=item).save()
