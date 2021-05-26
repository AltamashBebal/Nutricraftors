
from django import forms
from .models import HomeImage
from Plans.models import MealBox, TransformationPlan

# creating a form



class HomeImageForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = HomeImage

        # specify fields to be used
        fields = [ "image"]


class TransFormationForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = TransformationPlan

        # specify fields to be used
        fields = [ "image"]


class MealBoxForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = MealBox

        # specify fields to be used
        fields = ["image"]

    def save(self,commit=True):
        mealbox=self.instance
        # mealbox.name=self.name
        mealbox.image=self.cleaned_data['image']

        if self.cleaned_data['image']:
            mealbox.image=self.cleaned_data['image']

        if commit:
            mealbox.save()    
        return mealbox    