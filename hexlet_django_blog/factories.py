import factory
import factory.random

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.comments.models import Comment

SEED = 4321

factory.random.reseed_random(SEED)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker("sentence", nb_words=5)
    content = factory.Faker("paragraph", nb_sentences=5, variable_nb_sentences=True)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author = factory.Faker("name")
    text = factory.Faker("sentence", nb_words=4)
    article = factory.SubFactory(ArticleFactory)
