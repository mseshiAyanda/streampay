from .models import *
import django_filters


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Posts
        fields = ['name', 'type_of_content', 'description']