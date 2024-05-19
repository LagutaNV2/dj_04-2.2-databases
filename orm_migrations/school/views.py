from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # students = Student.objects.order_by('group').all()
    students = Student.objects.order_by('group').prefetch_related('teachers')
    context = {'object_list': students}
    print(f'{students=}')
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = 'group'

    return render(request, template, context)