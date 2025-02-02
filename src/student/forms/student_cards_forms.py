from django import forms
from student.models.student_cards_model import StudentCardsModel


class StudentCardForm(forms.ModelForm):

    class Meta:
        model = StudentCardsModel
        fields = ['student', 'reference', 'issue_date', 'expiration_date']

        widgets ={
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'})
        }

        labels ={
            'student': "Nom de l'élève"
        }