from django.forms import ModelForm
from .models import Project,Message,Skill,Endorsement,Comment,Coffee,Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','thumbnail','body']

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Title...'}
        )

        self.fields['thumbnail'].widget.attrs.update(
            {'class' : 'form-control'}
        )

        self.fields['title'].widget.attrs.update(
            {'class' : 'form-control'}
        )

        self.fields['body'].widget.attrs.update(
            {'class' : 'form-control'}
        )   

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Name...'}
        )

        self.fields['email'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Email...'}
        )

        self.fields['subject'].widget.attrs.update(
            {'class' : 'form-control'}
        )

        self.fields['body'].widget.attrs.update(
            {'class' : 'form-control'}
        )   

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Title...'}
        )

        self.fields['body'].widget.attrs.update(
            {'class' : 'form-control'}
        )

class EndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
        fields = '__all__'
        exclude = ['featured','approved']

    def __init__(self,*args,**kwargs):
        super(EndorsementForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Name...'}
        )

        self.fields['body'].widget.attrs.update(
            {'class' : 'form-control'}
        )

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['project']

    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Enter Name...'}
        )

        self.fields['body'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Add Comment...'}
        )

class OrderForm(ModelForm):
    class Meta:
        model = Coffee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit', 'Buy', css_class='button white btn-block btn-success mt-2')
        )

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super(QuestionForm,self).__init__(*args,**kwargs)

        self.fields['answer'].widget.attrs.update(
            {'class' : 'form-control','placeholder' : 'Add Comment...'}
        )


