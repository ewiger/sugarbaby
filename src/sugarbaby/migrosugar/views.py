from django.http import HttpResponse
from django.shortcuts import render
from django import forms
import json
from functools import partial
from sugarbaby.migrosugar.models import DiaryRecord


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())


def get_view_context():
    # Instantiate form for each instance to pass to template.
    #vm_instances_formset = VmInstancesFormSet()
    # Make list of column headers for the template.
    columns = list()
    # if vm_instances_formset.total_form_count() > 0:
    #     columns = [field.label_tag for field
    #                in vm_instances_formset.forms[0].visible_fields()]
    return {
    #    'formset': vm_instances_formset,
        'columns': columns,
    }


# Entry page
def home(request):
    return render(request, 'dashboard/count.html', get_view_context())


def count(request):
    return render(request, 'dashboard/count.html', get_view_context())


def diary(request):
    # if request.method == "POST":
    #     f = DateRangeForm(request.POST)
    #     if f.is_valid():
    #         c = f.save(commit=False)
    #         c.end_date = timezone.now()
    #         c.save()
    # else:

    f = DateRangeForm()
    args = {}
    args.update(request)
    args['form'] = f

    return render(request, 'dashboard/diary.html', {
        'form': f
    })
    #return render(request, 'dashboard/diary.html', get_view_context())


def list_products(request):
    response_data = [
        {'id': '7610200243430', 'name': 'M-Budget Vollmilch'},
        {'id': '7610200243430', 'name': '7610200243430'},
    ]
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")


def get_sugar_values(request, selected_date):
    response_data = DiaryRecord.get_daily_values(selected_date)
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
