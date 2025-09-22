import factory
import factory.random

from simple_blog.articles.models import Article

SEED = 4321

factory.random.reseed_random(SEED)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker("sentence", nb_words=5)
    content = factory.Faker("paragraph", nb_sentences=5, variable_nb_sentences=False)
