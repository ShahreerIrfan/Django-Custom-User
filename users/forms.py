from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import UserProfile, UserAddress
from .constant import GENDER, BLOOD_GROUP
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, Submit, Field

class UserProfileForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    bloodGroup = forms.ChoiceField(choices=BLOOD_GROUP)
    birthDate = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    streetAddress = forms.CharField(max_length=40)
    postalCode = forms.IntegerField()
    country = forms.CharField(max_length=40)
    image = forms.ImageField()  # New field for user image

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'gender', 'postalCode', 'birthDate', 'streetAddress', 'country', 'bloodGroup', 'image'] 

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign Up'))  # Add the submit button

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            gender = self.cleaned_data.get('gender')
            postalCode = self.cleaned_data.get('postalCode')
            streetAddress = self.cleaned_data.get('streetAddress')
            country = self.cleaned_data.get('country')
            birthDate = self.cleaned_data.get('birthDate')
            bloodGroup = self.cleaned_data.get('bloodGroup')
            image = self.cleaned_data.get('image')

            UserAddress.objects.create(
                user=user,
                streetAddress=streetAddress,
                postalCode=postalCode,
                country=country,
            )
            UserProfile.objects.create(
                user=user,
                bloodGroup=bloodGroup,
                birthDate=birthDate,
                gender=gender,
                image=image,
            )
        return user
