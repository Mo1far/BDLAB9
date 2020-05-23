from django.forms import ModelForm

from lab.models import Emp, Dept


class EmpForm(ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'


class DeptForm(ModelForm):
    class Meta:
        model = Dept
        fields = '__all__'
