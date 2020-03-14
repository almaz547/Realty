from django.core.management.base import BaseCommand
from realtyapp.models import Category, Apartment
from django.conf import settings

import json
import os


class Command(BaseCommand):

    def handle(self, *args, **options):

        apartment = Apartment.objects.all()
        print(f'14  len(apartment)  {len(apartment)}')
        list_url_base = []
        if apartment:
            for element in apartment:
                url = element.url_object
                list_url_base.append(url)
        try:
            path = 'C:\\Users\\User\PycharmProjects\Homework-5\homework_14_parser_html_\dict_rent_apartments.json'
            path_2 = os.path.join(settings.BASE_DIR, path)
            with open(path_2, 'r', encoding='utf-8') as f:
                dict_rent_apartments = json.load(f)
                print(f'1 Словарь rent получен')
        except FileNotFoundError:
            dict_rent_apartments = ''
            print(f'2 Ошибка в получении словаря')
        if dict_rent_apartments:
            x = 0
            for key, value in dict_rent_apartments.items():
                # print(f'30  key  {key}')
                # # print(f'31  value  {value}')
                # x += 1
                # if x > 4:
                #     break
                if key in list_url_base:
                    print(f'Совпадение объектов')
                    continue
                else:

                    url_object = key
                    if 'metro_name' in value:
                        metro_name = value['metro_name']
                    else:
                        metro_name = ''
                    # print(f'metro_name  {metro_name} {type(metro_name)}')
                    if 'metro_distance' in value:
                        metro_distance = value['metro_distance']
                    else:
                        metro_distance = ''
                    # print(f'metro_distance  {metro_distance}')
                    if 'metro_distance_number' in value:
                        metro_distance_number = value['metro_distance_number']
                    else:
                        metro_distance_number = 0
                    # print(f'metro_distance_number  {metro_distance_number}  {type(metro_distance_number)}')
                    if 'total_square' in value:
                        total_square = value['total_square']
                    else:
                        total_square = 0
                    # print(f'total_square  {total_square}  {type(total_square)}')
                    if 'living_square' in value:
                        living_square = value['living_square']
                    else:
                        living_square = 0
                    # print(f'living_square  {living_square}')
                    if 'floor_number' in value:
                        floor_number = value['floor_number']
                    else:
                        floor_number = 0
                    # print(f'floor_number  {floor_number}')
                    if 'floor_total' in value:
                        floor_total = value['floor_total']
                    else:
                        floor_total = 0
                    # print(f'floor_total  {floor_total}')
                    if 'count_room' in value:
                        count_room = value['count_room']
                    else:
                        count_room = 0
                    # print(f'count_room  {count_room}')
                    if 'material' in value:
                        material = value['material']
                    else:
                        material = ''
                    # print(f'material  {material}')
                    if 'balcony_type' in value:
                        balcony_type = value['balcony_type']
                    else:
                        balcony_type = ''
                    # print(f'balcony_type  {balcony_type}')
                    if 'is_home_appliances' in value:
                        is_home_appliances = value['is_home_appliances']
                    else:
                        is_home_appliances = ''
                    # print(f'is_home_appliances  {is_home_appliances}')
                    if 'is_furniture' in value:
                        is_furniture = value['is_furniture']
                    else:
                        is_furniture = ''
                    # print(f'is_furniture  {is_furniture}')
                    if 'year_public' in value:
                        year_public = value['year_public']
                    else:
                        year_public = 0
                    # print(f'year_public  {year_public}')
                    if 'month_public' in value:
                        month_public = value['month_public']
                    else:
                        month_public = 0
                    # print(f'month_public  {month_public}')
                    if 'day_public' in value:
                        day_public = value['day_public']
                    else:
                        day_public = 0
                    # print(f'day_public  {day_public}')
                    if 'time_public' in value:
                        time_public = value['time_public']
                    else:
                        time_public = 0
                    # print(f'time_public  {time_public}')
                    if 'cost' in value:
                        cost = value['cost']
                    else:
                        cost = 0
                    # print(f'cost  {cost}')
                    if 'currency' in value:
                        currency = value['currency']
                    else:
                        currency = ''
                    # print(f'currency  {currency}')
                    if 'street' in value:
                        street = value['street']
                    else:
                        street = ''
                    # print(f'street  {street}')
                    if 'house_number' in value:
                        house_number = value['house_number']
                    else:
                        house_number = 0
                    # print(f'house_number  {house_number}')
                    if 'city' in value:
                        city = value['city']
                    else:
                        city = ''
                    # print(f'city  {city}')
                    if 'area_city' in value:
                        area_city = value['area_city']
                    else:
                        area_city = ''
                    # print(f'area_city  {area_city}')
                    if 'advertising_object' in value:
                        advertising_object = value['advertising_object']
                    else:
                        advertising_object = ''


                    categ = Category.objects.get(name='rent')
                    # print(f'categ  {categ}')
                    # for element in categ:
                    #     categoryes = element
                    #     print(f'categoryes  {categoryes}')
                    #     print(f'type(categoryes)  {type(categoryes)}')

                    apartment = Apartment.objects.create(url_object= url_object, metro_name= metro_name, metro_distance= metro_distance,
                                                 metro_distance_number= metro_distance_number, total_square= total_square,
                                                 living_square= living_square, floor_number= floor_number, cost= cost,
                                                 floor_total= floor_total, count_room= count_room, material= material,
                                                 balcony_type= balcony_type, is_home_appliances= is_home_appliances,
                                                 is_furniture= is_furniture, year_public= year_public, area_city= area_city,
                                                 month_public= month_public, day_public= day_public, time_public= time_public,
                                                 currency= currency, street= street, house_number= house_number,
                                                 city= city, advertising_object= advertising_object)
                    apartment.save()
                    apartment.category.add(categ)
                    apartment.save()
                    print(apartment.category.all())






        else:
            print(f'4  Словарь пуст')

# categoryes  rent
# type(categoryes)  <class 'realtyapp.models.Category'>
