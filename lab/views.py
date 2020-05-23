from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from lab.forms import EmpForm, DeptForm
from lab.models import Emp, Dept
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class EmpCreateView(generic.CreateView):
    form_class = EmpForm
    success_url = '/'
    template_name = 'labs/create.html'


class DeptCreateView(generic.CreateView):
    form_class = DeptForm
    success_url = '/'
    template_name = 'labs/create.html'


class EmpListView(LoginRequiredMixin, ListView):
    queryset = Emp.objects.all()
    template_name = 'labs/emp_list.html'
    context_object_name = 'emp_list'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('pagesize') or self.paginate_by


class DeptListView(LoginRequiredMixin, ListView):
    queryset = Dept.objects.all()
    template_name = 'labs/dept_list.html'
    context_object_name = 'dept_list'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('pagesize') or self.paginate_by
