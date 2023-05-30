from django.forms.widgets import TextInput, DateInput, Select, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomPasswordInput(PasswordInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'border-2 border-black'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'gender', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'border-2 border-black'}),
            'first_name': TextInput(attrs={'class': 'border-2 border-black'}),
            'last_name': TextInput(attrs={'class': 'border-2 border-black'}),
            'email': TextInput(attrs={'class': 'border-2 border-black'}),
            'date_of_birth': DateInput(attrs={'class': 'datepicker border-2 border-black'}),
            'phone_number': TextInput(attrs={'class': 'border-2 border-black'}),
            'gender': Select(attrs={'class': 'border-2 border-black'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = CustomPasswordInput()
        self.fields['password2'].widget = CustomPasswordInput()
        self.fields['username'].required = False