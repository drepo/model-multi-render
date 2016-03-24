from demo.models import Report
from demo.forms import ReportForm, DefaultReportForm

from django.views.generic.edit import UpdateView


class ReportUpdate(UpdateView):
    form_class = ReportForm
    model = Report
    template_name = 'report_form.html'
    object_pk = 1


class WorkingReportUpdate(UpdateView):
    form_class = DefaultReportForm
    model = Report
    template_name = 'report_form.html'
    object_pk = 1
