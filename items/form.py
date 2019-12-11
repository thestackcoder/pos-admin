import io
from django import forms

from items.models import Item

import csv

class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        # for item in reader:
        #     Item.objects.create_item(item['name'], )