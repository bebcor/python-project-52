from django import forms
from .models import Task
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label 

User = get_user_model()

class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Выберите статус'
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.none(),
        required=False,
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Не назначен'
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label='Метки'
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        self.fields['executor'].queryset = User.objects.all()
        self.fields['labels'].queryset = Label.objects.all()
        
        if self.instance.pk is None:
            self.instance.author = self.user
