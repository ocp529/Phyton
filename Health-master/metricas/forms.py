from django import forms
from metricas.models import Metrics


class MetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields = "__all__"
