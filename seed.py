import os
import sys
import django

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market.settings')
django.setup()

from django.contrib.auth import get_user_model
from catalog.models import Category, Product

User = get_user_model()

categories = {
    'fruits-vegetables': {
        'name': 'Fruits & Vegetables',
        'slug': 'fruits-vegetables',
        'description': 'Fresh fruits and vegetables sourced daily.',
        'products': [
            ('Dole Bananas', 65.00, 100, 'products/fruits/banana.png'),
            ('Washington Red Apples', 90.00, 80, 'products/fruits/washington red apple.jpg'),
            ('Baguio Carrots', 55.00, 60, 'products/fruits/baguio_carrots.webp'),
            ('Fresh Tomatoes', 45.00, 75, 'products/fruits/tomatoes.webp'),
        ],
    },
    'dairy-products': {
        'name': 'Dairy Products',
        'slug': 'dairy-products',
        'description': 'Fresh dairy and chilled essentials.',
        'products': [
            ('Alaska Fresh Milk', 85.00, 50, 'products/dairy/fresh_milk.webp'),
            ('Eden Cheese', 120.00, 40, 'products/dairy/eden_cheese.webp'),
            ('Magnolia Butter', 95.00, 35, 'products/dairy/magnolia_butter.jpg'),
            ('Nestlé Yogurt', 70.00, 45, 'products/dairy/nestle_yogurt.jpg'),
        ],
    },
    'snacks': {
        'name': 'Snacks',
        'slug': 'snacks',
        'description': 'Crunchy snacks and crackers for every craving.',
        'products': [
            ('Piattos Cheese', 45.00, 90, 'products/snacks/piattos.webp'),
            ('Nova Multigrain Snacks', 50.00, 85, 'products/snacks/nova.webp'),
            ('SkyFlakes Crackers', 35.00, 120, 'products/snacks/skyflakes.webp'),
            ('Rebisco Chocolate Crackers', 40.00, 100, 'products/snacks/rebisco.png'),
        ],
    },
    'beverages': {
        'name': 'Beverages',
        'slug': 'beverages',
        'description': 'Refreshing drinks to quench your thirst.',
        'products': [
            ('Coca-Cola Mismo', 55.00, 70, 'products/beverage/coke.webp'),
            ('Wilkins Pure Bottled Water', 25.00, 150, 'products/beverage/wilkins.jpg'),
            ('C2 Green Tea', 35.00, 100, 'products/beverage/c2_red.jpg'),
            ('Zest-O Orange Juice', 40.00, 80, 'products/beverage/zest_o.webp'),
        ],
    },
    'household-essentials': {
        'name': 'Household Essentials',
        'slug': 'household-essentials',
        'description': 'Cleaning and personal care products.',
        'products': [
            ('Surf Powder Detergent', 95.00, 60, 'products/household/surf.jpg'),
            ('Joy Dishwashing Liquid', 75.00, 55, 'products/household/joy.jpg'),
            ('Safeguard Soap', 40.00, 90, 'products/household/safeguard.webp'),
            ('Palmolive Shampoo', 85.00, 65, 'products/household/palmolive.webp'),
        ],
    },
}

for cat_data in categories.values():
    cat, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={'name': cat_data['name'], 'description': cat_data['description']},
    )
    if created:
        print(f'  Created category: {cat.name}')
    else:
        print(f'  Found category: {cat.name}')

    for name, price, stock, image_name in cat_data['products']:
        product, created = Product.objects.update_or_create(
            name=name,
            defaults={
                'category': cat,
                'price': price,
                'stock': stock,
                'image': image_name,
                'description': f'Fresh {name.lower()} — available at 7-Evelyn.',
            },
        )
        if created:
            print(f'    Created product: {product.name} (₱{product.price})')
        else:
            print(f'    Updated product: {product.name}')

admin_created = False
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@7evelyn.com', 'admin123')
    admin_created = True
    print('  Created superuser: admin / admin123')

if not User.objects.filter(username='customer').exists():
    User.objects.create_user('customer', 'customer@7evelyn.com', 'customer123')
    print('  Created test user: customer / customer123')

print('\nSeed complete!')
print(f'  Admin login:   admin / admin123')
print(f'  Customer login: customer / customer123')
