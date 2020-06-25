from django import forms

class CommentForm (forms.Form):
    visitor_name_text = forms.CharField (max_length = 200, widget=forms.TextInput(attrs={'class' : 'vTextField'}))
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'class' : 'vLargeTextField'}))
