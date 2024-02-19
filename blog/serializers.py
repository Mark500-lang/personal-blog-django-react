from rest_framework import serializers
from .models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='order.username')
    
    class Meta:
        model = Articles
        fields = ['id', 'title', 'summary', 'content', 'category', 'author', 'views', 'created_at']