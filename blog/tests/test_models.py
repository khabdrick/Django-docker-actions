import pytest
from blog.models import Article


@pytest.mark.django_db

def test_article_create():  
   article = Article.objects.create(  
   author_name="Muhammed Ali",  
   title="Simple article",  
   content="The article's content",  
   )  
   assert article.author_name=="Muhammed Al" # this will make sure the test fails  
   assert article.title=="Simple article"  
   assert article.content=="The article's content" 