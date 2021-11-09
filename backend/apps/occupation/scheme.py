import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from apps.occupation.models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = "__all__"


class UpdateOccupation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        company_name = graphene.String()
        position_name = graphene.String()
        hire_date = graphene.Date()
        fire_date = graphene.Date(required=False)
        salary = graphene.Int()
        fraction = graphene.Int()
        base = graphene.Int()
        advance = graphene.Int()
        by_hours = graphene.Boolean()

    occupation = graphene.Field(OccupationType)

    def mutate(self, info, id, name, company_name, position_name, hire_date, salary, fraction, base, advance,
               by_hours, fire_date=None):
        element = Occupation.objects.get(id=id)
        element.name = name
        element.company_name = company_name
        element.position_name = position_name
        element.hire_date = hire_date
        element.fire_date = fire_date if fire_date else None
        element.salary = salary
        element.fraction = fraction
        element.base = base
        element.advance = advance
        element.by_hours = by_hours
        element.save()
        return UpdateOccupation(occupation=element)


class CreateOccupation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        company_name = graphene.String()
        position_name = graphene.String()
        hire_date = graphene.Date()
        fire_date = graphene.Date()
        salary = graphene.Int()
        fraction = graphene.Int()
        base = graphene.Int()
        advance = graphene.Int()
        by_hours = graphene.Boolean()

    occupation = graphene.Field(OccupationType)

    def mutate(self, info, name, company_name, position_name, hire_date, fire_date, salary, fraction, base, advance,
               by_hours):
        new_object = Occupation(
            name=name,
            company_name=company_name,
            position_name=position_name,
            hire_date=hire_date,
            fire_date=fire_date,
            salary=salary,
            fraction=fraction,
            base=base,
            advance=advance,
            by_hours=by_hours
        )
        new_object.save()
        return CreateOccupation(occupation=new_object)


class Query(graphene.ObjectType):
    get_occupations = graphene.List(OccupationType)
    get_occupation = graphene.Field(OccupationType, id=graphene.ID())

    def resolve_get_occupations(self, info, **kwargs):
        return Occupation.objects.all()

    def resolve_get_occupation(self, info, id):
        return Occupation.objects.get(id=id)


class Mutation(graphene.ObjectType):
    add_occupation = CreateOccupation.Field()
    update_occupation = UpdateOccupation.Field()


scheme = graphene.Schema(query=Query, mutation=Mutation)
