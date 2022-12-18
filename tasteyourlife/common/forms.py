from django import forms

from tasteyourlife.common.models import Article


class ArticleBaseForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'content')

        labels = {
            'name': "Article name:",
            'content': 'Article content:',}

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Enter name for the article'
                }

            ),
            'content': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter the article's content"
                }
            ),
        }