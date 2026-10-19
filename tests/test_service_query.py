import graphene
from graphene import ObjectType

from graphene_federation import LATEST_VERSION, build_schema


def test_build_schema_add_service_query_default():
    class Query(ObjectType):
        hello = graphene.String()

    schema = build_schema(query=Query, federation_version=LATEST_VERSION)

    assert "_service" in schema.graphql_schema.type_map["Query"].fields


def test_build_schema_add_service_query_false():
    class Query(ObjectType):
        hello = graphene.String()

    schema = build_schema(
        query=Query,
        federation_version=LATEST_VERSION,
        add_service_query=False,
    )

    assert "_service" not in schema.graphql_schema.type_map["Query"].fields



def test_build_schema_mutation_only_no_service_query():
    """Schemas without queries are still valid."""

    class Mutation(ObjectType):
        x = graphene.String()

    schema = build_schema(
        mutation=Mutation,
        federation_version=LATEST_VERSION,
        add_service_query=False,
    )
    assert schema.graphql_schema is not None
