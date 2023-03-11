from django import forms

#una clase se extienda con una caracteristica para que luego se comberta en un formulario html

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.
    TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'input'}))


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo del projecto", max_length=200, widget=forms.Textarea(attrs={'class': 'input'}))
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'input'}))