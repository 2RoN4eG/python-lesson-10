import shop_utils as su


def show_menu():
    print("""
1 - Вывести товары, срок годности которых истекает в ближайшие `days` дней.
2 - Вывести товары, у которых срок годности уже истёк.
3 - Создать отчёт по продажам: название товара, количество проданных единиц, общая выручка.
4 - Сгруппировать товары по категориям: количество товаров и средняя цена.
    """)


def main():
    while True:
        show_menu()
        choise = input("Выберете пункт меню: ")
        match(choise):
            case "0":
                break
            case "1":
                days = int(input("Введите кол-во дней: "))
                json_data = su.read_json_file(r"./Task 2/products.json")
                su.export_expiring_products(json_data,
                                            r"./Task 2/expiring_products.csv",
                                            days)
            case "2":
                json_data = su.read_json_file(r"./Task 2/products.json")
                su.export_expired_products(json_data,
                                           r"./Task 2/expired_products.csv")
            case "3":
                json_data = su.read_merged_json_data(r"./Task 2/products.json",
                                                     r"./Task 2/sales.json")
                su.export_sales_report(json_data,
                                       r"./Task 2/sales_report.csv")
            case "4":
                json_data = su.read_json_file(r"./Task 2/products.json")
                su.export_category_summary(json_data,
                                           r"./Task 2/category_summary.csv")


if __name__ == "__main__":
    main()
