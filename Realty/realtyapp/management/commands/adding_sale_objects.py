from django.core.management.base import BaseCommand
from realtyapp.models import Category, Apartment, Material, Metro, Room_count, Area_city
from realtyapp.models import Currency, Balcony, Sity, Street, Images
from django.conf import settings

import json
import os

def check_object_in_base(model, name):
    if name:
        name_base = model.objects.filter(name=name)
        if name_base:
            for elem in name_base:
                name_base = elem
        if not name_base:
            name_base = model.objects.create(name=name)
    else:
        name_base = None
    return name_base

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
            path = os.path.join(settings.BASE_DIR, 'realtyapp\data\dict_sale_apartments.json')
            with open(path, 'r', encoding='utf-8') as f:
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
                    metro_base = check_object_in_base(model=Metro, name=metro_name)
                    metro_distance = value.get('metro_distance', '')
                    metro_distance_number = value.get('metro_distance_number', '')
                    total_square = value.get('total_square', '')
                    living_square = value.get('living_square', '')
                    floor_number = value.get('floor_number', '')
                    floor_total = value.get('floor_total', '')
                    count_room = value.get('count_room', '')
                    room_base = check_object_in_base(model=Room_count, name=count_room)
                    material = value.get('material', '')
                    material_base = check_object_in_base(model=Material, name=material)
                    balcony_type = value.get('balcony_type', '')
                    balcony_base = check_object_in_base(model=Balcony, name=balcony_type)
                    is_home_appliances = value.get('is_home_appliances', '')
                    is_furniture = value.get('is_furniture', '')
                    year_public = value.get('year_public', '')
                    month_public = value.get('month_public', '')
                    day_public = value.get('day_public', '')
                    time_public = value.get('time_public', '')
                    cost = value.get('cost', '')
                    currency = value.get('currency', '')
                    currency_base = check_object_in_base(model=Currency, name=currency)
                    street = value.get('street', '')
                    street_base = check_object_in_base(model=Street, name=street)
                    house_number = value.get('house_number', '')
                    city = value.get('city', '')
                    city_base = check_object_in_base(model=Sity, name=city)

                    description = value.get('description', '')

                    area_city = value.get('area_city', '')
                    area_city_base = check_object_in_base(model=Area_city, name=area_city)

                    list_url_images = value.get('images', [])
                    advertising_object = value.get('advertising_object', '')

                    categ = Category.objects.get(name='sale')

                    apartment = Apartment.objects.create(url_object=url_object, metro_name=metro_base,
                                                         metro_distance=metro_distance,
                                                         metro_distance_number=metro_distance_number,
                                                         total_square=total_square,
                                                         living_square=living_square, floor_number=floor_number,
                                                         cost=cost,
                                                         floor_total=floor_total, count_room=room_base,
                                                         material=material_base,
                                                         balcony_type=balcony_base,
                                                         is_home_appliances=is_home_appliances,
                                                         is_furniture=is_furniture, year_public=year_public,
                                                         area_city=area_city_base,
                                                         month_public=month_public, day_public=day_public,
                                                         time_public=time_public,
                                                         currency=currency_base, street=street_base,
                                                         house_number=house_number,
                                                         city=city_base, advertising_object=advertising_object,
                                                         description=description)

                    apartment.category.add(categ)
                    apartment.save()
                    for url_image in list_url_images:
                        image_base = Images.objects.create(url_image=url_image, apartment=apartment)

        else:
            print(f'4  Словарь пуст')

