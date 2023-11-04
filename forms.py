from django import forms
from .models import PersonalinfoModel
from .models import ShiftAvailability
from .models import SurveyCalendar

class PersonalinfoModelForm(forms.ModelForm):
    class Meta:
        model = PersonalinfoModel
        fields = ["item1", "item2", "item3", "item4","item5","item6","item7","item8"]

        from django import forms

class ShiftAvailabilityForm(forms.ModelForm):
    class Meta:
        model = ShiftAvailability
        fields = [
            'date',
            'on_call_available',
            'on_call_comments',
            'on_call_external_hospital',
            'on_call_external_hospital_comments',
        ]

class SurveyCalendarForm(forms.ModelForm):
    class Meta:
        model = SurveyCalendar
        fields = ["date", "item1", "item2", "item3", "item4","item5","item6","item7","item8"]

        from django import forms

