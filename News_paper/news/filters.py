from django_filters import FilterSet
from .models import Post,Category


class PostFilter(FilterSet):
    class Meta:
        model=Post
        fields={
            'title':['icontains'],
            'data_time':['gt'],
                }
        
class CategoryFilter(FilterSet):
    class Meta:
        model=Category
        fields={
            'name':['icontains']
                }