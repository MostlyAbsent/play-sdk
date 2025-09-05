from django.urls import path
from .views import main
from .views.article import ArticleView

urlpatterns = [
    # /program/
    path('', main.index, name='index'),
    # /program/1
    path('article/', ArticleView.as_view(), name='article')
]
