from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        labels = {
            'group': 'Группа',
            'text': 'Текст'
        }
        fields = '__all__'
