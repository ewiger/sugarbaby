from django.http import HttpResponse
from django.shortcuts import render
import json


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
    return render(request, 'dashboard/diary.html', get_view_context())


def list_products(request):
    response_data = [
        {'id': '7610200243430', 'name': 'M-Budget Vollmilch'},
    ]
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")
