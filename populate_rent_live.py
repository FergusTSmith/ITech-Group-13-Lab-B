import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentlive.settings')

import django
django.setup()
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment

def populate():

    letting_agents = [
        {'name': 'Dave Smith',
        'description': 'Landlord operating out of Glasgow',
        'phone': '0712345678',
        'email': 'DaveSmith@gmail.com',
        'category': 'landlord',
        'city': 'GLA'},
        {'name': 'John Davidson',
        'description': 'Letting Agent operating out of Edinburgh',
        'phone': '078889992',
        'email': 'JohnDavidsonh@gmail.com',
        'category': 'agent',
        'city': 'EDI'},
        {'name': 'Mary Fergusson',
        'description': 'Letting agent operating out of Glasgow',
        'phone': '0798765432',
        'email': 'MaryF@gmail.com',
        'category': 'landlord',
        'city': 'GLA'},
    ]

    categories = [
        {'name': 'landlord',
        'description': 'Private person looking to rent a small amount of privately owned properties'},
        {'name': 'agent',
        'description': 'Person working for a letting agency'},
        {'name': 'agency',
        'description': 'Company created to manage and let rentals'},
    ]

    cities = [
        {'name': 'Glasgow',
        'uniqueName': 'GLA',
        'description': 'Scotlands largest city',
        'categories': {'landlord', 'agency', 'agent'}
        },
        {'name': 'Edinburgh',
        'uniqueName': 'EDI',
        'description': 'Scotlands capital city',
        'categories': {'landlord', 'agency', 'agent'}
        },{'name': 'Dundee',
        'uniqueName': 'DND',
        'description': 'A city',
        'categories': {'landlord', 'agency', 'agent'}
        },
    ]

    rentals = [
        {'name': '123 Fake St',
        'address': '123 Fake St, Glasgow, G11 1A1',
        'description': '1 bedroom flat in Southside',
        'city': 'GLA',
        'lettingAgent': 'Mary Fergusson',
        'price': 400,
        'size': 2,
        'followers': 254,
        'state': True},
        {'name': '321 Fake Av',
        'address': '321 Fake Av, Edinburgh, EH12 1H1',
        'description': '1 bedroom flat in Morningside',
        'city': 'EDI',
        'lettingAgent': 'John Davidson',
        'price': 200,
        'size': 4,
        'followers': 1243,
        'state': True},
        {'name': '445 Unreal St',
        'address': '445 Unreal St, Glasgow, G22 3J2',
        'description': '1 bedroom flat in West End',
        'city': 'GLA',
        'lettingAgent': 'Dave Smith',
        'price': 800,
        'size': 6,
        'followers': 112,
        'state': True},
    ]
    for l in letting_agents:
        add_agent(l['name'], l['description'], l['phone'], l['email'], l['category'], l['city'])
        
    for cat in categories:
        add_category(cat['name'], cat['description'])

    for c in cities:
        add_city(c['name'], c['uniqueName'], c['description'], c['categories'])

    for r in rentals:
        add_rental(r['name'], r['address'], r['description'], r['city'], r['lettingAgent'], r['price'], r['size'], r['followers'], r['state'])



    def add_category(name, description):
        c = Category.objects.get_or_create(name=name)[0]
        c.description = description
        c.save()
        return c

    def add_agent(name, description, phone, email, category, city):
        l = LettingAgent.objects.get_or_create(name=name)
        l.description = description
        l.phone = phone
        l.email = email
        l.category = category
        l.city = city
        l.save()
        return l

    def add_city(name, uniqueName, description, categories):
        c = City.objects.get_or_create(uniqueName=uniqueName)
        c.name = name
        c.description = description
        c.categories = categories
        c.save()
        return c

    def add_rental(name, address, description, city, lettingAgent, price, size, followers, state):
        r = Rental_Property.objects.get_or_create(address=address)
        r.name = name
        r.description = description
        r.city = city
        r.lettingAgent = lettingAgent
        r.price = price
        r.size = size
        r.followers = followers
        r.state = state
        r.save()
        return r



if __name__ == '__main__':
    print("Starting the RentLive Population Script...")
    populate()