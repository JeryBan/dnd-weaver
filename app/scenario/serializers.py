"""
Serializers for handling
Scenario, Npc and Monster
data
"""
from rest_framework import serializers
from scenario.models import Scenario, Npc, Monster
from core.validators import FileExtensionValidator


class ScenarioSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    order = serializers.IntegerField(required=True)
    lvl_requirement = serializers.IntegerField(required=False)
    map = serializers.FileField(validators=[FileExtensionValidator], required=False)
    soundtrack = serializers.FileField(required=False)

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'order', 'lvl_requirement', 'description', 'map', 'soundtrack']


class NpcListSerializer(serializers.ModelSerializer):
    image = serializers.FileField(validators=[FileExtensionValidator])

    class Meta:
        model = Npc
        fields = ['image']


class NpcDetailSerializer(NpcListSerializer):

    class Meta(NpcListSerializer.Meta):
        fields = '__all__'


class MonsterListSerializer(serializers.ModelSerializer):
    image = serializers.FileField(validators=[FileExtensionValidator])

    class Meta:
        model = Monster
        fields = ['image']


class MonsterDetailSerializer(MonsterListSerializer):

    class Meta(MonsterListSerializer.Meta):
        fields = '__all__'

