from django.forms.widgets import TextInput, DateInput, Select, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomPasswordInput(PasswordInput):
    """class for setting up custom password field"""
    def __init__(self, attrs=None):
        """Adding styling to the passworld field"""
        default_attrs = {'class': 'border-2 border-black text-black'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class SignUpForm(UserCreationForm):
    """class that handles the creation of the sign up page"""
    class Meta(UserCreationForm.Meta):
        """Defining custom fields for the signup form"""
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'gender', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'border-2 border-black text-black'}),
            'first_name': TextInput(attrs={'class': 'border-2 border-black text-black'}),
            'last_name': TextInput(attrs={'class': 'border-2 border-black text-black'}),
            'email': TextInput(attrs={'class': 'border-2 border-black text-black'}),
            'date_of_birth': DateInput(attrs={'class': 'datepicker border-2 border-black text-black'}),
            'phone_number': TextInput(attrs={'class': 'border-2 border-black text-black'}),
            'gender': Select(attrs={'class': 'border-2 border-black text-black'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = CustomPasswordInput()
        self.fields['password2'].widget = CustomPasswordInput()
        self.fields['username'].required = False
