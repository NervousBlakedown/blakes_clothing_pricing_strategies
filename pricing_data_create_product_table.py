"""Create Pricing Database: Product Table."""

# Imports
import pandas as pd
import random
import string
import sqlite3

# Generate random strings for Description and SKU
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Generate random decimal values for Cost
# TODO: Adjust prices to reflect real situation
def generate_random_cost():
    return f'${int(round(random.uniform(1, 3000), 0)):,.0f}.00'

# Define product name and description mapping
product_descriptions = {
    'Aristocrat Suit': 'Elegant and sophisticated suit for formal occasions',
    'Regal Blazer': 'Stylish blazer with a touch of luxury',
    'Sovereign Tuxedo': 'Classic tuxedo for special events',
    'Noble Cashmere Overcoat': 'Warm and luxurious overcoat made with cashmere',
    'Elite Silk Shirt': 'High-quality silk shirt for a refined look',
    'Monarch Velvet Jacket': 'Opulent velvet jacket with a regal touch',
    'Opulent Wool Trousers': 'Luxurious wool trousers for a polished appearance',
    'Grandeur Double-Breasted Vest': 'Elegant double-breasted vest for formal attire',
    'Prestige Dress Shoes': 'Premium dress shoes for a distinguished look',
    'Majesty Silk Robe': 'Sumptuous silk robe for ultimate comfort and style',
    'Eminent Leather Briefcase': 'Stylish and practical leather briefcase for professionals',
    'Royal Ascot Bow Tie': 'Sophisticated bow tie for formal occasions',
    'Majestic Cufflinks': 'Exquisite cufflinks to elevate any outfit',
    'Imperial Cashmere Sweater': 'Luxuriously soft cashmere sweater for cold days',
    'Exquisite Pocket Square': 'Handcrafted pocket square for a refined finishing touch',
    'Premier Tailored Shirt': 'Tailored shirt with exceptional fit and quality',
    'Lavish Velvet Smoking Jacket': 'Opulent velvet smoking jacket for elegant evenings',
    'Deluxe Suede Loafers': 'Comfortable and stylish suede loafers for any occasion',
    'Supreme Silk Tie': 'Premium silk tie for a sophisticated look',
    'Prestigious Leather Belt': 'High-quality leather belt to complete your outfit',
    'Elite Embroidered Dress Shirt': 'Elegant dress shirt with intricate embroidery',
    'Refined Wool Peacoat': 'Classic peacoat made with fine wool',
    'Grandiose Silk Scarf': 'Luxurious silk scarf to add flair to your outfit',
    'Polished Leather Monk Straps': 'Stylish and refined leather monk strap shoes'
}

# Define the number of rows to generate (index value = product)
num_rows = 24  # 100_000; one row for each product

# Define a list of 24 product names
product_names = [
    'Aristocrat Suit', 'Regal Blazer', 'Sovereign Tuxedo', 'Noble Cashmere Overcoat',
    'Elite Silk Shirt', 'Monarch Velvet Jacket', 'Opulent Wool Trousers', 'Grandeur Double-Breasted Vest',
    'Prestige Dress Shoes', 'Majesty Silk Robe', 'Eminent Leather Briefcase', 'Royal Ascot Bow Tie',
    'Majestic Cufflinks', 'Imperial Cashmere Sweater', 'Exquisite Pocket Square', 'Premier Tailored Shirt',
    'Lavish Velvet Smoking Jacket', 'Deluxe Suede Loafers', 'Supreme Silk Tie', 'Prestigious Leather Belt',
    'Elite Embroidered Dress Shirt', 'Refined Wool Peacoat', 'Grandiose Silk Scarf',
    'Polished Leather Monk Straps'
]

# Define an empty dictionary to store the generated data
data = {
    'ProductID': [],
    'ProductName': [],
    'Description': [],
    'SKU': [],
    'Cost': [],
    'CreatedDate': []
}

# Generate random data for each column
for product_id in range(1, num_rows + 1):
    product_name = random.choice(product_names)
    data['ProductID'].append(f"{product_id:02d}")
    data['ProductName'].append(product_name)
    data['Description'].append(product_descriptions[product_name])
    data['SKU'].append(generate_random_string(8))
    data['Cost'].append(generate_random_cost())
    data['CreatedDate'].append(generate_random_datetime())

# Create the dataframe
df = pd.DataFrame(data)

# set the data types of the columns
df = df.astype({
    'ProductID': str,
    'ProductName': str,
    'Description': str,
    'SKU': str,
    'Cost': str,
    'CreatedDate': 'datetime64[ns]'
})



"""Part II: add to Sqlite3 database"""

# Connect to the SQLite database or create a new one if it doesn't exist
conn = sqlite3.connect('blake_clothing_brand.db')

# Load the dataframe into a SQLite table
df.to_sql('products', conn, if_exists='replace', index=False)

# Commit the changes
conn.commit()

# Get a cursor
cursor = conn.cursor()

# add SQL query
cursor = conn.execute("SELECT * FROM Products;")

rows = cursor.fetchall()

for row in rows:
    print(row)


# close the connection
conn.close()
