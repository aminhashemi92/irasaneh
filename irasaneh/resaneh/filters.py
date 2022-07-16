import django_filters
from django import forms
from .models import *
from account.models import Company
from django.db.models import Q
from cities.models import *

class ResanehFilter(django_filters.FilterSet):

    PRICE_CHOICE =(
        ('گران‌ترین','گران‌ترین'),
        ('ارزان‌ترین','ارزان‌ترین'),
    )

    CREATED_CHOICE=(
        ('قدیمی‌ترین','قدیمی‌ترین'),
        ('جدید‌ترین','جدید‌ترین'),
    )

    VIEWED_CHOICE=(
        ('پربازدیدترین','min'),
        ('max','max'),
    )

    price_g = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_l = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    company = django_filters.ModelMultipleChoiceFilter(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    industry = django_filters.ModelMultipleChoiceFilter(queryset=Industry.objects.all(), widget=forms.CheckboxSelectMultiple)
    showtype = django_filters.ModelMultipleChoiceFilter(queryset=ShowType.objects.all(), widget=forms.CheckboxSelectMultiple)
    structuretype = django_filters.ModelMultipleChoiceFilter(queryset=StructureType.objects.all(), widget=forms.CheckboxSelectMultiple)
    place = django_filters.ModelMultipleChoiceFilter(queryset=Place.objects.all(), widget=forms.CheckboxSelectMultiple)
    gender = django_filters.ModelMultipleChoiceFilter(queryset=Gender.objects.all(), widget=forms.CheckboxSelectMultiple)
    ages = django_filters.ModelMultipleChoiceFilter(queryset=Ages.objects.all(), widget=forms.CheckboxSelectMultiple)
    incometithe = django_filters.ModelMultipleChoiceFilter(queryset=IncomeTithe.objects.all(), widget=forms.CheckboxSelectMultiple)

    q = django_filters.CharFilter(method='my_search',label="Search", widget=forms.TextInput(attrs={'class': 'form-control text-center' , 'placeholder':'جستجو ...'}))


    price = django_filters.ChoiceFilter(choices=PRICE_CHOICE, method='price_sort')
    created = django_filters.ChoiceFilter(choices=CREATED_CHOICE, method='created_sort')
    viewed = django_filters.ChoiceFilter(choices=VIEWED_CHOICE, method='viewed_sort')


    # country = django_filters.ModelMultipleChoiceFilter(queryset=Country.objects.all(), widget=forms.CheckboxSelectMultiple)
    # state = django_filters.ModelMultipleChoiceFilter(queryset=State.objects.all(), widget=forms.CheckboxSelectMultiple)
    # city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(), widget=forms.CheckboxSelectMultiple)
    # zone = django_filters.ModelMultipleChoiceFilter(queryset=Zone.objects.all(), widget=forms.CheckboxSelectMultiple)



    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all(), widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3'}))

    state = django_filters.ModelChoiceFilter(queryset=State.objects.all(), widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3'}))

    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-select form-select-sm mb-3'}))

    zone = django_filters.ModelMultipleChoiceFilter(queryset=Zone.objects.all(), widget=forms.CheckboxSelectMultiple)



    class Meta:
        model = Resaneh
        fields = ['q']



    def my_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(address__icontains=value) | Q(detail__icontains=value)
        )

    def price_sort(self, queryset, name, value):
        data = 'price' if value == 'ارزان‌ترین' else '-price'
        return queryset.order_by(data)

    def created_sort(self, queryset, name, value):
        data = 'created' if value == 'قدیمی‌ترین' else '-created'
        return queryset.order_by(data)

    def viewed_sort(self, queryset, name, value):
        data = 'viewed' if value == 'پربازدیدترین' else '-viewed'
        return queryset.order_by(data)




class ResanehSearchFilter(django_filters.FilterSet):

    q = django_filters.CharFilter(method='my_search',label="Search", widget=forms.TextInput(attrs={'class': 'form-control text-center' , 'placeholder':'جستجو ...'}))

    class Meta:
        model = Resaneh
        fields = ['q']

    def my_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(address__icontains=value) | Q(detail__icontains=value)
        )
