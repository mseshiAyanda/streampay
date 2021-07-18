from .models import *
import django_filters


class ContentFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = ['name', 'type_of_content', 'description']