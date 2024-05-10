"""
Serializers for handling
Scenario, Npc and Monster
data
"""
from rest_framework import serializers
from scenario.models import Scenario, Npc, Monster


class ScenarioSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('story_mode'):
            self.Meta.fields += ['story_mode']
        else:
            self.Meta.fields += ['combat_mode']

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'order', 'lvl_requirement']


class ScenarioDetailSerializer(ScenarioSerializer):

    class Meta(ScenarioSerializer.Meta):
        fields = ScenarioSerializer.Meta.fields + ['description', 'map', 'soundtrack', 'npcs', 'monsters']


class NpcSerializer(serializers.ModelSerializer):

    class Meta:
        model = Npc
        fields = ['image']


class NpcDetailSerializer(NpcSerializer):

    class Meta(NpcSerializer.Meta):
        fields = '__all__'


class MonsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monster
        fields = ['image']


class MonsterDetailSerializer(MonsterSerializer):

    class Meta(MonsterSerializer.Meta):
        fields = '__all__'

