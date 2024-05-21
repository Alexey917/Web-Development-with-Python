from django import forms


class UserForm(forms.Form):
    login = forms.CharField(min_length=2, max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)


class NumbersForm(forms.Form):
    CHOICES = [
        ('min_n', 'Минимум из трёх'),
        ('max_n',  'Максимум из трёх'),
        ('mid', 'Среднеарифметическое из трёх')
    ]
    first = forms.IntegerField()
    second = forms.IntegerField()
    third = forms.IntegerField()
    action = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


class Registration(forms.Form):
    GENDER = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]

    name = forms.CharField(min_length=2, max_length=60, label='Имя')
    surname = forms.CharField(min_length=2, max_length=60, label='Фамилия')
    age = forms.IntegerField(min_value=0, label='Возраст')
    email = forms.EmailField(min_length=7, max_length=60, label='Почта')
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER, label='Пол')
    address = forms.CharField(label='Адрес для доставки товара')


class DateProgrammer(forms.Form):
    year = forms.CharField(min_length=2, max_length=60, label='Год')
