from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('Email', 'mobile', 'Students', 'Father_name', 'Father_occ', 'Address', 'College')
        labels = {
            'Email': 'Email Address',
            'Students': "Student's Name",
            'Father_name': "Father's Name",
            'Father_occ': "Father's Occupation"

        }

    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.fields['College'].empty_label = "Select"
        self.fields['Father_occ'].required = False
