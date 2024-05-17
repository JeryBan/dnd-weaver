"""
Serializers for handling
Scenario, Npc and Monster
data
"""
from rest_framework import serializers
from scenario.models import Scenario, Npc, Monster


class ScenarioListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('story_mode'):
            self.Meta.fields += ['story_mode']
        else:
            self.Meta.fields += ['combat_mode']

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'order', 'lvl_requirement']


class ScenarioDetailSerializer(ScenarioListSerializer):

    class Meta(ScenarioListSerializer.Meta):
        fields = ScenarioListSerializer.Meta.fields + ['description', 'map', 'soundtrack', 'npcs', 'monsters', 'campaign']


class NpcListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Npc
        fields = ['image']


class NpcDetailSerializer(NpcListSerializer):

    class Meta(NpcListSerializer.Meta):
        fields = '__all__'


class MonsterListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monster
        fields = ['image']


class MonsterDetailSerializer(MonsterListSerializer):

    class Meta(MonsterListSerializer.Meta):
        fields = '__all__'

