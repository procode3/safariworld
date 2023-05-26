from django.shortcuts import render, redirect
from django.http import HttpResponse


adv_list = [
        {
        'id': 1,
        'place_id': 1001,
        'name': 'Item 1',
        'created_at': '2023-05-23 10:00:00',
        'updated_at': '2023-05-23 12:30:00',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'departure_date': '2023-06-01',
        'return_date': '2023-06-10',
        'no_of_days': 10,
        'no_of_nights': 9,
        'price': 1999.99,
        'reviews_count': 15,
        'no_of_slots': 20,
        'age_restriction': 18,
        'activities': 'Hiking, Sightseeing, Swimming'
     },
    {
        'id': 2,
        'place_id': 1002,
        'name': 'Item 2',
        'created_at': '2023-05-24 09:30:00',
        'updated_at': '2023-05-24 14:45:00',
        'description': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem.',
        'departure_date': '2023-07-05',
        'return_date': '2023-07-12',
        'no_of_days': 8,
        'no_of_nights': 7,
        'price': 1499.99,
        'reviews_count': 8,
        'no_of_slots': 15,
        'age_restriction': 21,
        'activities': 'Camping, Cycling, Bonfire'
    },
    {
        'id': 3,
        'place_id': 1003,
        'name': 'Item 3',
        'created_at': '2023-05-25 14:15:00',
        'updated_at': '2023-05-26 09:20:00',
        'description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.',
        'departure_date': '2023-08-15',
        'return_date': '2023-08-20',
        'no_of_days': 6,
        'no_of_nights': 5,
        'price': 899.99,
        'reviews_count': 5,
        'no_of_slots': 16,
        'age_restriction': 16,
        'activities': 'Canoeing, Fishing, Bird Watching'
    }]

def index(request):
    return render(request, 'booking/index.html')

def adventures(request):
   
    return render(request, 'booking/all_adventures.html')

def adv_details(request, id):
    adv_item = adv_list[id-1]
    template = f"""
        <h1>{adv_item['name']}</h1>
        <p>{adv_item['description']}</p>
        <p>{adv_item['activities']}</p>
    """
    return HttpResponse(template)

def book_adv(request, id):
    authenticated = True

    if authenticated:
        return redirect(f'/{id}/order')
    else:
        return redirect('/login')

def order_page(request, id):
    return HttpResponse('ordering') 

def login(request):
    return HttpResponse('Thank you')       