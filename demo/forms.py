from demo.models import Report, Content

from django import forms


class ReportForm(forms.ModelForm):

    contents = forms.ModelMultipleChoiceField(
                to_field_name='name',
                queryset=Content.objects.all())

    class Meta:
        model = Report
        fields = ('name', 'contents')


class DefaultReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('name', 'contents')
