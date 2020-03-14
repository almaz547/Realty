from django.core.management.base import BaseCommand
from realtyapp.models import Category, Apartment

class Command(BaseCommand):

    def handle(self, *args, **options):
        category = Category.objects.create(name='rent')
        category.save()
        category = Category.objects.create(name='sale')
        category.save()


        # Проверка после загрузки
        # apartment = Apartment.objects.all()
        # print(f'14  len(apartment)  {len(apartment)}')
        # x = 0
        # for el in apartment:
        #     print(f'el.url_object  {el.url_object}')
        #     print(f'el.category  {el.category}')
        #     x += 1
        #     if x >5:
        #         break


        # categ = Category.objects.get(name='rent')
        # print(f'categ  {categ}')
        # print(f'type(categ)  {type(categ)}')