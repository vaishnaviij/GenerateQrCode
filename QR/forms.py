from django import forms



class QRCodeForm(forms.Form):
    restraunt_name=forms.CharField(
        max_length=50,
        label="Name",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Name ',
            
        })
        )
    url = forms.URLField(max_length=200,
                         label="URL/Link",
                        widget=forms.URLInput(attrs={
                            'class':'form-control',
                            
                            'placeholder':'Enter the link ',
                            
                        })
    )
