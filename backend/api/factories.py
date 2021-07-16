from factory import Factory, Faker
import factory
from .models import Author, Book


class AuthorF(factory.Factory):
    id = factory.Sequence(lambda x: x)
    first_name = Faker('first_name')
    last_name = Faker('last_name')

    class Meta:
        model = Author


class BookF(factory.Factory):
    id = factory.Sequence(lambda x: x)
    title = Faker('sentence', nb_words=7)
    year = Faker('year')
    author = factory.SubFactory(AuthorF)

    class Meta:
        model = Book
