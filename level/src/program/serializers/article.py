from rest_framework import serializers
from ..models.article import Article

class ArticleSerializer(serializers.ModelSerializer):
    """
        How objects of the Article model are serialized into other data types (e.g. JSON)
    """
    class Meta:
        model = Article
        fields = ('title', 'body')
