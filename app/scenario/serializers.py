"""
Serializers for handling
Scenario, Npc and Monster
data
"""
from rest_framework import serializers
from scenario.models import Scenario, Npc, Monster
from core.validators import FileExtensionValidator


class ScenarioListSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.context.get('story_mode'):
            self.fields['story_mode'] = serializers.BooleanField()

        if self.context.get('combat_mode'):
            self.fields['combat_mode'] = serializers.BooleanField()

    def validate(self, attrs):
        """Ensures scenario mode can either be story or combat"""
        if attrs.get('story_mode', False) and attrs.get('combat_mode', False):
            raise serializers.ValidationError('mode can either be story or combat')

        if attrs.get('story_mode', False):
            attrs['combat_mode'] = False

        if attrs.get('combat_mode', False):
            attrs['story_mode'] = False

        return attrs

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'order', 'lvl_requirement']


class ScenarioDetailSerializer(ScenarioListSerializer):
    map = serializers.FileField(validators=[FileExtensionValidator])

    class Meta(ScenarioListSerializer.Meta):
        fields = ScenarioListSerializer.Meta.fields + ['description', 'map', 'soundtrack', 'npcs', 'monsters', 'campaign']


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

