from faker import Faker

from hexlet_django_blog.articles.models import Article

SEED = 4321
fake = Faker()
Faker.seed(4321)


def article_factory():
    return Article.objects.create(
            title = fake.sentence(nb_words=5), 
            content = fake.text(max_nb_chars=200)) 
        

