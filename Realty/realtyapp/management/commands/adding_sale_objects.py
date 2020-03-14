from django.core.management.base import BaseCommand
from realtyapp.models import Category, Estate_object
from django.conf import settings

import json
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        # estate_objects = Estate_object.objects.first().url_object
        # categ = Category.objects.filter(name='sale')
        estate_objects = Estate_object.objects.all()
        print(f'estate_objects  {estate_objects}')
        x = 0
        for elem in estate_objects:
            print(elem.category)
            x += 1
            if x > 5:
                break
        # categ = Category.objects.filter(name='sale')
        # estate_objects_category = estate_objects.category.first().filter(name= 'sale')
        # print(f'estate_objects_category  {estate_objects_category}')

        # categ = Category.objects.filter(name='sale').all()
        # print(f'categ  {categ}  {type(categ)}')
        # estate_objec = categ.estate_objects.all()
        # print(f'estate_objec  {estate_objec}')
        #
        # estate_objects = Estate_object.categ.all()
        # print(f'14  estate_object  {estate_objects}')
        # list_url_base = []
        # if estate_objects:
        #     for element in estate_objects:
        #         url = element.url_object
        #         list_url_base.append(url)
        # try:
        #     path = 'C:\\Users\\User\PycharmProjects\Homework-5\homework_14_parser_html_\dict_sale_apartments.json'
        #     path_2 = os.path.join(settings.BASE_DIR, path)
        #     with open(path_2, 'r', encoding='utf-8') as f:
        #         dict_sale_apartments = json.load(f)
        #         print(f'1 Словарь rent получен')
        # except FileNotFoundError:
        #     dict_sale_apartments = ''
        #     print(f'2 Ошибка в получении словаря')
        # if dict_sale_apartments:
        #     print(f'len(dict_sale_apartments)  {len(dict_sale_apartments)}')
        #     x = 0
        #     for key, value in dict_sale_apartments.items():
        #         print(f'30  key  {key}')
        #         print(f'31  value  {value}')
        #         x += 1
        #         if x > 4:
        #             break
        #         if key in list_url_base:
        #             continue
                # else:
                #
                #     url_object = key
                #     if 'metro_name' in value:
                #         metro_name = value['metro_name']
                #     else:
                #         metro_name = ''
                #     if 'metro_distance' in value:
                #         metro_distance = value['metro_distance']
                #     else:
                #         metro_distance = ''
                #     if 'metro_distance_number' in value:
                #         metro_distance_number = value['metro_distance_number']
                #     else:
                #         metro_distance_number = ''
                #     if 'total_square' in value:
                #         total_square = value['total_square']
                #     else:
                #         total_square = ''
                #     if 'living_square' in value:
                #         living_square = value['living_square']
                #     else:
                #         living_square = ''
                #     if 'floor_number' in value:
                #         floor_number = value['floor_number']
                #     else:
                #         floor_number = ''
                #     if 'floor_total' in value:
                #         floor_total = value['floor_total']
                #     else:
                #         floor_total = ''
                #     if 'count_room' in value:
                #         count_room = value['count_room']
                #     else:
                #         count_room = ''
                #     if 'material' in value:
                #         material = value['material']
                #     else:
                #         material = ''
                #     if 'balcony_type' in value:
                #         balcony_type = value['balcony_type']
                #     else:
                #         balcony_type = ''
                #     if 'is_home_appliances' in value:
                #         is_home_appliances = value['is_home_appliances']
                #     else:
                #         is_home_appliances = ''
                #     if 'is_furniture' in value:
                #         is_furniture = value['is_furniture']
                #     else:
                #         is_furniture = ''
                #     if 'year_public' in value:
                #         year_public = value['year_public']
                #     else:
                #         year_public = ''
                #     if 'month_public' in value:
                #         month_public = value['month_public']
                #     else:
                #         month_public = ''
                #     if 'day_public' in value:
                #         day_public = value['day_public']
                #     else:
                #         day_public = ''
                #     if 'time_public' in value:
                #         time_public = value['time_public']
                #     else:
                #         time_public = ''
                #     if 'cost' in value:
                #         cost = value['cost']
                #     else:
                #         cost = ''
                #     if 'currency' in value:
                #         currency = value['currency']
                #     else:
                #         currency = ''
                #     if 'street' in value:
                #         street = value['street']
                #     else:
                #         street = ''
                #     if 'house_number' in value:
                #         house_number = value['house_number']
                #     else:
                #         house_number = ''
                #     if 'city' in value:
                #         city = value['city']
                #     else:
                #         city = ''
                #     if 'area_city' in value:
                #         area_city = value['area_city']
                #     else:
                #         area_city = ''
                #     if 'advertising_object' in value:
                #         advertising_object = value['advertising_object']
                #     else:
                #         advertising_object = ''
                #     categ = Category.objects.get(name='sale')
                #     estate_object = Estate_object.objects.create(url_object= url_object, metro_name= metro_name, metro_distance= metro_distance,
                #                                  metro_distance_number= metro_distance_number, total_square= total_square,
                #                                  living_square= living_square, floor_number= floor_number, cost= cost,
                #                                  floor_total= floor_total, count_room= count_room, material= material,
                #                                  balcony_type= balcony_type, is_home_appliances= is_home_appliances,
                #                                  is_furniture= is_furniture, year_public= year_public, area_city= area_city,
                #                                  month_public= month_public, day_public= day_public, time_public= time_public,
                #                                  currency= currency, street= street, house_number= house_number,
                #                                  city= city, advertising_object= advertising_object)
                #     estate_object.save()
                #     estate_object.category.add(categ)
                #     estate_object.save()

        # else:
        #     print(f'4  Словарь пуст')

