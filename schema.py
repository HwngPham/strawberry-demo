from strawberry import Schema

from resolvers import BookQuery


schema = Schema(query=BookQuery)
