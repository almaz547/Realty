from django.core.management.base import BaseCommand
from realtyapp.models import Category, Apartment
from django.conf import settings

import json
import os


class Command(BaseCommand):

    def handle(self, *args, **options):

        apartments = Apartment.objects.all()
        print(f'14  len(apartments)  {len(apartments)}')
        list_url_base = []
        if apartments:
            for element in apartments:
                url = element.url_object
                list_url_base.append(url)

        try:
            path = 'C:\\Users\\User\PycharmProjects\Homework-5\homework_14_parser_html_\dict_sale_apartments.json'
            path_2 = os.path.join(settings.BASE_DIR, path)
            with open(path_2, 'r', encoding='utf-8') as f:
                dict_sale_apartments = json.load(f)
                print(f'1 Словарь sale получен')
        except FileNotFoundError:
            dict_sale_apartments = ''
            print(f'2 Ошибка в получении словаря')
        if dict_sale_apartments:
            print(f'len(dict_sale_apartments)  {len(dict_sale_apartments)}')
            for key, value in dict_sale_apartments.items():
                if key in list_url_base:
                    print(f'Совпадение объектов')
                    continue
                else:
                    url_object = key
                    metro_name = value.get('metro_name', '')
                    metro_distance = value.get('metro_distance', '')
                    metro_distance_number = value.get('metro_distance_number', '')
                    total_square = value.get('total_square', '')
                    living_square = value.get('living_square', '')
                    floor_number = value.get('floor_number', '')
                    floor_total = value.get('floor_total', '')
                    count_room = value.get('count_room', '')
                    material = value.get('material', '')
                    balcony_type = value.get('balcony_type', '')
                    is_home_appliances = value.get('is_home_appliances', '')
                    is_furniture = value.get('is_furniture', '')
                    year_public = value.get('year_public', '')
                    month_public = value.get('month_public', '')
                    day_public = value.get('day_public', '')
                    time_public = value.get('time_public', '')
                    cost = value.get('cost', '')
                    currency = value.get('currency', '')
                    street = value.get('street', '')
                    house_number = value.get('house_number', '')
                    city = value.get('city', '')
                    area_city = value.get('area_city', '')
                    advertising_object = value.get('advertising_object', '')

                    categ = Category.objects.get(name='sale')

                    apartment = Apartment.objects.create(url_object= url_object, metro_name= metro_name, metro_distance= metro_distance,
                                                 metro_distance_number= metro_distance_number, total_square= total_square,
                                                 living_square= living_square, floor_number= floor_number, cost= cost,
                                                 floor_total= floor_total, count_room= count_room, material= material,
                                                 balcony_type= balcony_type, is_home_appliances= is_home_appliances,
                                                 is_furniture= is_furniture, year_public= year_public, area_city= area_city,
                                                 month_public= month_public, day_public= day_public, time_public= time_public,
                                                 currency= currency, street= street, house_number= house_number,
                                                 city= city, advertising_object= advertising_object)

                    apartment.category.add(categ)
                    apartment.save()
                    # print(apartment.category.all())

        else:
            print(f'4  Словарь пуст')

