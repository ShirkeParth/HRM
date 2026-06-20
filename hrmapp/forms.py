from django import forms
from .models import PerformanceReview

class PerformanceReviewForm(forms.ModelForm):

    class Meta:
        model = PerformanceReview

        fields = [
            'review_title',
            'review_date',
            'employee',
            'review_period',
            'rating',
            'comments'
        ]

        widgets = {
            'review_date': forms.DateInput(attrs={
                'type': 'date'
            }),

            'comments': forms.Textarea(attrs={
                'rows': 4
            })
        }