from django import forms
from django.db.models import QuerySet
from .models import Visit
from core.models import City, Airport

class SearchForm(forms.Form):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Search...'}))


class AddVisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["continent", "country", "city", "airport"]

    def __init__(self, *args, **kwargs):
        initial_country = kwargs.pop("initial_country", None)
        initial_continent = kwargs.pop("initial_continent", None)
        initial_city = kwargs.pop("initial_city", None)
        initial_airport = kwargs.pop("initial_airport", None)
        
        super(AddVisitForm, self).__init__(*args, **kwargs)

        if initial_country:
            self.initial["country"] = initial_country
            self.fields["country"].disabled = True
            self.initial["continent"] = initial_continent
            self.fields["continent"].disabled = True
            
            if initial_city:
                self.initial["city"] = initial_city
                self.fields["city"].disabled = True
                if initial_airport:
                    self.initial["airport"] = initial_airport
                    self.fields["airport"].disabled = True
                else:
                    airports = Airport.objects.filter(city=initial_city)
                    self.fields["airport"].queryset = airports
            else:
                cities = City.objects.filter(country=initial_country)
                self.fields["city"].queryset = cities
                airports = Airport.objects.none()
                for city in cities:
                    airports |= Airport.objects.filter(city=city)
                self.fields["airport"].queryset = airports

