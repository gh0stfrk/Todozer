from django import forms


class AddTodo(forms.Form):
    title = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                                      'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))
    
    description = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter todo description', 'rows': 3}))
    
    