from django import forms

from Car_Collection_App.web.models import Profile, Car, CarChoices


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['first_name', 'last_name', 'profile_picture']

    username = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        widget=forms.EmailInput,
        required=True
    )

    age = forms.IntegerField(
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True
    )


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    type = forms.ChoiceField(
        choices=CarChoices.choices(),
        required=True
    )

    model = forms.CharField(
        required=True
    )

    year = forms.IntegerField(
        required=True
    )

    image_url = forms.URLField(
        required=True
    )

    price = forms.FloatField(
        required=True
    )

