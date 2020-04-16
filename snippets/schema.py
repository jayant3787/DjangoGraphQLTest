import graphene
from graphene_django.types import DjangoObjectType
from .models import Snippet
from datetime import datetime

class SnippetType(DjangoObjectType):
    class Meta:
        model = Snippet

class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)

    def resolve_all_snippets(self, info, **kwargs):
        return [
            Snippet(name ='Jayant', stream ='Mca',login_time= datetime.now()),
            Snippet(name ='Sehal', stream ='Mca',login_time= datetime.now()),
            Snippet(name ='Meghal', stream ='Mca',login_time= datetime.now()),
            Snippet(name ='Shashank', stream ='Mca',login_time= datetime.now()),
            Snippet(name ='Rakesh', stream ='Mca',login_time= datetime.now()),
        ]