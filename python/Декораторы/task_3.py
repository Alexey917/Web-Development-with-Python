def decorator(func):
    def wrapper(name, year, balance, organization):
        print(f'--------------------{organization}--------------------')
        func(name, year, balance, organization)
        print(f'--------------------{organization}--------------------')
    return wrapper


@decorator
def my_company(name, year, balance, organization):
    financial_report = {
        'Название организации: ': name,
        'Год: ': year,
        'Баланс: ': balance,
    }
    for key, value in financial_report.items():
        print(key, value)
    return financial_report


def organization_1():
    format_report = 'PDF'
    return format_report


def organization_2():
    format_report = 'Excel'
    return format_report


def organization_3():
    format_report = 'doc'
    return format_report


my_company('Папортник', 2024, 1500000, organization_1())
my_company('Папортник', 2023, 1000000, organization_2())
my_company('Папортник', 2022, 700000, organization_3())
