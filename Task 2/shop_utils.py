from datetime import datetime
from itertools import groupby
import csv
import json


def read_json_file(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)


# ## Функции модуля

# ### 1. `export_expiring_products(json_data, filename, days)`
# Вывести товары, срок годности которых истекает в ближайшие `days` дней.

# **CSV‑выход:**  
# `id, name, category, expires, days_left`

def export_expiring_products(json_data, filename, days):
    date_now = datetime.today()
    expired_products = []
    for product in json_data["products"]:
        expires = datetime.strptime(product["expires"], "%Y-%m-%d")
        days_left = (expires - date_now).days
        if days_left < days:
            expired_product = {}
            expired_product["id"] = product["id"]
            expired_product["name"] = product["name"]
            expired_product["category"] = product["category"]
            expired_product["expires"] = product["expires"]
            expired_product["days_left"] = days_left

            expired_products.append(expired_product)

    with open(filename, "w", newline="") as csv_file:
        fieldnames = ["id", "name", "category", "expires", "days_left"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expired_products)


# ### 2. `export_expired_products(json_data, filename)`
# Вывести товары, у которых срок годности уже истёк.

# **CSV‑выход:**
# `id, name, category, expires, expired_days_ago`

def export_expired_products(json_data, filename):
    date_now = datetime.now()
    expired_products = []
    for product in json_data["products"]:
        expires = datetime.strptime(product["expires"], "%Y-%m-%d")
        expired_days_ago = (expires - date_now)
        if expired_days_ago.days < 0:
            expired_product = {}
            expired_product["id"] = product["id"]
            expired_product["name"] = product["name"]
            expired_product["category"] = product["category"]
            expired_product["expires"] = product["expires"]
            expired_product["expired_days_ago"] = expired_days_ago

            expired_products.append(expired_product)

    with open(filename, "w", newline="") as csv_file:
        fieldnames = ["id", "name", "category", "expires", "expired_days_ago"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expired_products)


# ### 3\*. `export_sales_report(json_data, filename)`
# Создать отчёт по продажам: название товара, количество проданных единиц, общая выручка.

# **CSV‑выход:**  
# `product_name, quantity_sold, total_revenue`

def get_product_value(products_json_data, id, key):
    for product in products_json_data["products"]:
        if product["id"] == id:
            return product.get(key, "0")


def get_sale_value(sales_json_data, product_id, key):
    for sale in sales_json_data["sales"]:
        if sale["product_id"] == product_id:
            return sale.get(key, "0")
    else:
        return "0"


def read_merged_json_data(products_filename, sales_filename):
    products_json_data = read_json_file(products_filename)
    sales_json_data = read_json_file(sales_filename)

    merged_products = []
    for product in products_json_data["products"]:
        quantity = int(get_sale_value(sales_json_data,
                                      product["id"],
                                      "quantity"))
        merged_product = {}
        merged_product["product_name"] = product["name"]
        merged_product["quantity_sold"] = quantity
        merged_product["total_revenue"] = quantity * float(get_product_value(
            products_json_data, product["id"], "price"))
        merged_products.append(merged_product)

    return merged_products


def export_sales_report(json_data, filename):
    with open(filename, "w", newline="") as csv_file:
        fieldnames = ["product_name", "quantity_sold", "total_revenue"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_data)


# ### 4\*. `export_category_summary(json_data, filename)`
# Сгруппировать товары по категориям: количество товаров и средняя цена.

# **CSV‑выход:**  
# `category, products_count, average_price`

def export_category_summary(json_data, filename):
    products = json_data["products"].copy()

    def category_predicate(item):
        return item.get("category", "")

    products.sort(key=category_predicate)

    grouped_items = []
    for group, group_items in groupby(products, key=category_predicate):
        average_price = 0
        group_items = list(group_items)
        for item in group_items:
            average_price += item["price"]
        average_price /= len(group_items)

        group_item = {}
        group_item["category"] = group
        group_item["products_count"] = len(group_items)
        group_item["average_price"] = average_price

        grouped_items.append(group_item)

    with open(filename, "w", newline="") as csv_file:
        fieldnames = ["category", "products_count", "average_price"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(grouped_items)
