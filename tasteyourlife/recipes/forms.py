from django import forms

from tasteyourlife.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'category', 'subcategory', 'cooking_method', 'ingredients', 'instructions', 'servings',
                  'preparation_time', 'cooking_time', 'photo', 'difficulty')

        labels = {
            'name': "Recipe Name:",
            'category': 'Category:',
            'subcategory': 'Subcategory:',
            'cooking_method': 'Cooking Method:',
            'ingredients': 'Ingredients:',
            'instructions': 'Instructions:',
            'servings': 'Servings:',
            'preparation_time': 'Preparation Time /minutes/:',
            'cooking_time': 'Cooking Time /minutes/:',
            'photo': 'Upload a photo of the recipe:',
            'difficulty': 'Difficulty level:'
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter recipe name"
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'subcategory': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'cooking_method': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
            'ingredients': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter one ingredient on each new line. For example:\nPotatoes - 600 g "
                                   "\nSalt - 1 tbsp"
                }
            ),
            'instructions': forms.Textarea(
                attrs={
                    'class': "form-control",
                    'placeholder': 'Enter detailed instruction for preparing the recipe'
                }
            ),
            'servings': forms.NumberInput(
                attrs={
                    'class': "form-control",
                }
            ),
            'preparation_time': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'cooking_time': forms.NumberInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'photo': forms.FileInput(
                attrs={
                    'class': "form-control"
                }
            ),
            'difficulty': forms.Select(
                attrs={
                    'class': "form-control"
                }
            ),
        }

