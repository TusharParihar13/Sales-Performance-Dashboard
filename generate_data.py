import pandas as pd
import random
from datetime import datetime, timedelta

# 1. Setup Data for Columns
regions = ['East', 'West', 'Central', 'South']
segments = ['Consumer', 'Corporate', 'Home Office']
states = ['California', 'Texas', 'New York', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']

# Map Categories to Sub-Categories for realism
products_map = {
    'Furniture': ['Bookcases', 'Chairs', 'Tables', 'Furnishings'],
    'Office Supplies': ['Labels', 'Storage', 'Art', 'Binders', 'Appliances', 'Paper', 'Fasteners', 'Envelopes'],
    'Technology': ['Phones', 'Accessories', 'Machines', 'Copiers']
}

# Helper function to generate random dates
def random_date(start_year=2022, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# 2. Generate 7000 Rows
data = []

for i in range(7000):
    # IDs
    order_id = f"CA-2023-{random.randint(100000, 999999)}"
    cust_id = f"{random.choice(['AB', 'CD', 'EF', 'GH'])}-{random.randint(10000, 99999)}"
    
    # Dates (Ship date is 2-7 days after Order date)
    o_date = random_date()
    s_date = o_date + timedelta(days=random.randint(2, 7))
    
    # Categorical
    region = random.choice(regions)
    state = random.choice(states)
    segment = random.choice(segments)
    
    # Product Hierarchy
    category = random.choice(list(products_map.keys()))
    sub_category = random.choice(products_map[category])
    prod_name = f"{sub_category} Product {random.randint(1, 50)}" # Generic name
    
    # Numerical
    quantity = random.randint(1, 15)
    base_price = random.uniform(10, 500)
    sales = round(base_price * quantity, 2)
    discount = random.choice([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
    
    # Profit Calculation (Sales - Cost, simplified logic)
    # Profit can be negative if discount is high
    cost = sales * 0.6 # Assuming 60% cost
    profit = round((sales * (1 - discount)) - cost, 2)
    
    # Append row
    data.append([
        order_id, 
        o_date.strftime('%Y-%m-%d'), 
        s_date.strftime('%Y-%m-%d'), 
        cust_id, 
        segment, 
        region, 
        state, 
        category, 
        sub_category, 
        prod_name, 
        sales, 
        quantity, 
        discount, 
        profit
    ])

# 3. Create DataFrame and Save
columns = ['Order_ID', 'Order_Date', 'Ship_Date', 'Customer_ID', 'Customer_Segment', 
           'Region', 'State', 'Product_Category', 'Sub_Category', 'Product_Name', 
           'Sales', 'Quantity', 'Discount', 'Profit']

df = pd.DataFrame(data, columns=columns)

# Save to CSV
file_name = 'sales_data_7000.csv'
df.to_csv(file_name, index=False)

print(f"Success! '{file_name}' with 7000 rows has been created.")
print(df.head())