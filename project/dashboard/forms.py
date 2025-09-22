
from django import forms
from users.models import User
from serviceCategory.models import ServiceCategory
 
class WorkerExtraDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['serviceCategory', 'skills', 'rate', 'experience', 'city']

        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your skills'}),
            'rate': forms.NumberInput(attrs={'placeholder': 'Hourly rate'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Years of experience'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
                    }

        # Custom validation: required only for workers
        def clean(self):
            cleaned_data = super().clean()
            role = self.instance.role  # or cleaned_data.get('role') if included in form
            city = cleaned_data.get('city')
            skills = cleaned_data.get('skills')
            rate = cleaned_data.get('rate')
            experience = cleaned_data.get('experience')

            if role == User.Role.WORKER:
                if not city:
                    self.add_error('city', "City is required for workers.")
                if not skills:
                    self.add_error('skills', "Skills are required for workers.")
                if not rate:
                    self.add_error('rate', "Rate is required for workers.")
                if not experience:
                    self.add_error('experience', "Experience is required for workers.")
            
            return cleaned_data
        


SORT_CHOICES = [
    ('asc', 'Price Low to High'),
    ('desc', 'Price High to Low'), 
]

class workerSearchForm(forms.Form):
    searchInput = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search workers...'}))
    category = forms.ModelChoiceField(
        queryset=ServiceCategory.objects.all(),  # Admin-defined categories
        required=False,
        empty_label="All Categories"
    )
    city = forms.CharField(required=False, label="City" , widget=forms.TextInput(attrs={'placeholder': 'Your city...'}))
    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False
    )



