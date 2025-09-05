from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ..models.article import Article
from ..serializers.article import ArticleSerializer

class ArticleView(APIView):
    """
        Some basic API view that users send requests to for
        searching for articles
    """
    def post(self, request: Request, format=None):
        print(f"--- ArticleView POST received ---")
        try:
            articles = Article.objects.filter(**request.data)
            print(f"Queryset count: {articles.count()}")
            serializer = ArticleSerializer(articles, many=True)
        except Exception as e:
            print(e)
            return Response([])
        return Response(serializer.data)
