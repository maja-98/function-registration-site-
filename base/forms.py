from .models import *
from django.forms import ModelForm

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class FamilyForm(ModelForm):
    class Meta:
        model = Family
        fields = '__all__'