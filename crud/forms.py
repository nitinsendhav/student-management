from django import forms
from app.models import studentModel

class StudentForm(forms.ModelForm):
    grade_choice = [
        ("", "-- Select Grade --"),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),

    ]
    grade = forms.ChoiceField(choices=grade_choice, label="grade", widget=forms.Select(attrs={
                'class': 'form-control',
            }))
    
    result_choice = [
        ("", "-- Select Result --"),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    ]
    result = forms.ChoiceField(choices=result_choice, label="result", widget=forms.Select(attrs={
                'class': 'form-control',
            }))
    subject_choice = [
        ("", "-- Select Subject --"),
        ('BA', 'BA'),
        ('BCA', 'BCA'),
        ('BCOM', 'BCOM'),
        ('BSC', 'BSC'),
        ('BMLT', 'BMLT'),
        ('Science', 'Science'),
        ('Psychology', 'Psychology'),
        ('Mathematics', 'Mathematics'),
        ('Chemistry', 'Chemistry'),
        ('Physics', 'Physics'),
        ('Economics', 'Economics'),
        ('Engineering', 'Engineering'),
        ('Computer Sciences', 'Computer Sciences'),
        ('Computer Basics', 'Computer Basics'),
        ('Philosophy', 'Philosophy'),

    ]
    subject = forms.ChoiceField(choices=subject_choice, label="subject", widget=forms.Select(attrs={
                'class': 'form-control',
            }))


    class Meta:
        model = studentModel
        fields = ['name', 'subject', 'roll', 'marks', 'grade', 'result', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            
            'roll': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your roll'
            }),

            'marks': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Marks'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
        }

    
