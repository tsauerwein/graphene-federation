import graphene
from graphene import ObjectType
from graphene_directives.schema import Schema

from graphene_federation import LATEST_VERSION, build_schema


def test_build_schema_default_schema_cls():
    class Query(ObjectType):
        hello = graphene.String()

    schema = build_schema(query=Query, federation_version=LATEST_VERSION)

    assert isinstance(schema, Schema)
    assert type(schema) is Schema


def test_build_schema_custom_schema_cls():
    custom_schema_cls_used = []

    class CustomSchema(Schema):
        pass

    class Query(ObjectType):
        hello = graphene.String()

    schema = build_schema(
        query=Query,
        federation_version=LATEST_VERSION,
        schema_cls=CustomSchema,
    )

    assert isinstance(schema, CustomSchema)
    assert type(schema) is CustomSchema
