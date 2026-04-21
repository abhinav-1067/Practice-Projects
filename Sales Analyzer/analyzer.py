import numpy as np

def total_revenue(data):
    price = data['f5']
    quantitiy = data['f4']
    revenue = price*quantitiy
    return np.sum(revenue)

def best_selling_product(data):
    products = data['f3']
    quantitiy = data['f4']
    
    unique_products = np.unique(products)
    total_sales = []
    
    for product in unique_products:
        total = np.sum(quantitiy[product==products])
        total_sales.append(total)
        
    max_index = np.argmax(total_sales)    
    return unique_products[max_index], total_sales[max_index]

def high_sales(data,threshold=3):
    quantity = data['f4']
    return data[quantity >= threshold]

def month_sale(data):
    dates = data['f1']
    price = data['f5']
    qunatity = data['f4']
    
    months = np.array([d[:7] for d in dates])
    unique_months = np.unique(months)
    
    result = {}
    
    for month in unique_months:
        mask = month == months
        revenue = np.sum(qunatity[mask]*price[mask])
        result[month] = revenue
    
    return result
