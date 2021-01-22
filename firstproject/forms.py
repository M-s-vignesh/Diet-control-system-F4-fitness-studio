from django import forms

class food(forms.Form):
	apple=forms.FloatField(label="how many apples you had in grams?")
	orange=forms.FloatField(label="how many orange you had in grams?")
	banana=forms.FloatField(label="how many banana you had in grams?")
	onion=forms.FloatField(label="how many onion you had in grams?")
	carrot=forms.FloatField(label="how many carrot you had in grams?")
	rice=forms.FloatField(label="how much rice you had in grams?")
	fish=forms.FloatField(label="how much fish you had in grams?")
	stretching=forms.FloatField(label="how many stretches u have done?")
	pushups=forms.FloatField(label="how many pushups u have done?")
	lifting=forms.FloatField(label="how many lifting u have done?")
	walking=forms.FloatField(label="how many steps u have walked?")
	running=forms.FloatField(label="how many minutes u had ran?")
