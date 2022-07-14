from strawberry import type, field
from typing import List

from models import Book


def resolve_books():
    return [
        Book(title='Book foo', author='by foo'),
        Book(title='Book bar', author='by bar')
    ]


@type
class BookQuery:
    books: List[Book] = field(resolver=resolve_books)
