"""
Serializers for handling
Scenario, Npc and Monster
data
"""
from rest_framework import serializers
from scenario.models import Scenario, Npc, Monster
from core.validators import FileExtensionValidator


# ----------------------------------------------------------------------------
# ----------------------- RETRIEVE SERIALIZERS -------------------------------
# ----------------------------------------------------------------------------

class MonsterRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving Monsters
    """
    index = serializers.CharField(
        required=False,
        help_text='Monster index'
    )

    class Meta:
        model = Monster
        fields = ['id', 'index']
        read_only_fields = fields


class NpcRetrieveSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving Npcs
    """
    name = serializers.CharField(
        required=False,
        help_text='Npc name'
    )
    description = serializers.CharField(
        required=False,
        help_text='Npc description'
    )
    race = serializers.CharField(
        required=False,
        help_text='Npc race'
    )

    class Meta:
        model = Npc
        fields = ['id', 'name', 'description', 'race']
        read_only_fields = fields


class ScenarioRetrieveSerializer(serializers.ModelSerializer):
    """
    Detail Scenario serializer
    """
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    order = serializers.IntegerField(required=True)
    lvl_requirement = serializers.IntegerField(required=False)
    map = serializers.CharField(required=False)
    # map = serializers.FileField(validators=[FileExtensionValidator], required=False)
    # soundtrack = serializers.FileField(required=False)

    monsters = MonsterRetrieveSerializer(
        many=True,
        required=False,
        help_text='Monsters'
    )
    npcs = NpcRetrieveSerializer(
        many=True,
        required=False,
        help_text='Npcs'
    )

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'description', 'order', 'lvl_requirement', 'map', 'monsters', 'npcs']
        read_only_fields = fields


# ----------------------------------------------------------------------------
# ------------------------- UPDATE SERIALIZERS -------------------------------
# ----------------------------------------------------------------------------

class MonsterUpdateListSerializer(serializers.ListSerializer):
    """
    List serializer for updating Monsters
    """

    class Meta:
        model = Monster
        fields = ['id', 'index']
        read_only_fields = ['id']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        scenario = self.context.get('scenario')
        bulk_create_items = []
        bulk_update_items = []
        input_ids = []

        for monster_data in validated_data:
            monster_id = monster_data.pop('id', None)
            input_ids.append(monster_id)

            if monster_id:
                monster = Monster(
                    id=monster_id,
                    scenario=scenario,
                    **monster_data
                )
                bulk_update_items.append(monster)
            else:
                monster = Monster(
                    scenario=scenario,
                    **monster_data
                )
                bulk_create_items.append(monster)

        if input_ids:
            # delete monster not included in the lists
            Monster.objects.filter(
                scenario=scenario,
            ).exclude(id__in=input_ids).delete()

        if bulk_create_items:
            Monster.objects.bulk_create(bulk_create_items)

        if bulk_update_items:
            update_fields = [f.name for f in Monster._meta.fields if f.name not in ['id', 'scenario']]
            Monster.objects.bulk_update(bulk_update_items, fields=update_fields)

        return instance


class MonsterUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Monsters
    """
    class Meta:
        model = Monster
        list_serializer_class = MonsterUpdateListSerializer
        fields = ['id', 'index']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        return instance


class NpcUpdateListSerializer(serializers.ListSerializer):
    """
    List serializer for updating Npcs
    """

    class Meta:
        model = Npc
        fields = ['id', 'name', 'description', 'race']
        read_only_fields = ['id']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        scenario = self.context.get('scenario')
        bulk_create_items = []
        bulk_update_items = []
        input_ids = []

        for npc_data in validated_data:
            npc_id = npc_data.pop('id', None)
            input_ids.append(npc_id)

            if npc_id:
                npc = Npc(
                    id=npc_id,
                    scenario=scenario,
                    **npc_data
                )
                bulk_update_items.append(npc)
            else:
                npc = Npc(
                    scenario=scenario,
                    **npc_data
                )
                bulk_create_items.append(npc)

            if input_ids:
                # delete npcs not included in the lists
                Npc.objects.filter(
                    scenario=scenario,
                ).exclude(id__in=input_ids).delete()

            if bulk_create_items:
                Npc.objects.bulk_create(bulk_create_items)

            if bulk_update_items:
                update_fields = [f.name for f in Npc._meta.fields if f not in ['id', 'scenario', 'user']]
                Npc.objects.bulk_update(bulk_update_items, fields=update_fields)

        return instance


class NpcUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Npcs
    """
    class Meta:
        model = Npc
        list_serializer_class = NpcUpdateListSerializer
        fields = ['id', 'name', 'description', 'race']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        return instance


class ScenarioCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Scenarios
    """
    title = serializers.CharField(
        max_length=255,
        required=True,
        allow_null=False,
        help_text='Scenario title'
        )
    description = serializers.CharField(
        max_length=255,
        required=False,
        allow_null=True,
        help_text='Scenario description'
    )
    order = serializers.IntegerField(
        required=True,
        allow_null=False,
        help_text='Scenario order'
    )
    lvl_requirement = serializers.IntegerField(
        required=False,
        allow_null=True,
        help_text='Scenario lvl_requirement'
    )
    story_mode = serializers.BooleanField(
        required=False,
        allow_null=False,
        default=False,
        help_text='Scenario mode'
    )
    map = serializers.CharField(
        required=False,
        allow_null=True,
        help_text='Scenario map path'
    )
    soundtrack = serializers.CharField(
        required=False,
        allow_null=True,
        help_text='Scenario soundtrack path'
    )
    monsters = MonsterUpdateSerializer(
        many=True,
        required=False,
        help_text='Monsters'
    )
    npcs = NpcUpdateSerializer(
        many=True,
        required=False,
        help_text='Npcs'
    )

    class Meta:
        model = Scenario
        fields = ['id', 'title', 'description', 'order', 'lvl_requirement',
                  'story_mode', 'map', 'soundtrack', 'monsters', 'npcs']
        read_only_fields = ['id']

    def create(self, validated_data):
        instance = Scenario.objects.create(
            title=validated_data['title'],
            campaign=validated_data['campaign']
        )
        self.update(instance, validated_data)
        return instance

    def update(self, instance, validated_data):
        monster_data = validated_data.pop('monsters', [])
        npc_data = validated_data.pop('npcs', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if monster_data:
            monster_serializer = MonsterUpdateSerializer(
                instance=instance.monsters.all(),
                data=monster_data,
                many=True,
                context={'scenario': instance}
            )
            monster_serializer.is_valid(raise_exception=True)
            monster_serializer.save()

        if npc_data:
            npc_serializer = NpcUpdateSerializer(
                instance=instance.npcs.all(),
                data=npc_data,
                many=True,
                context={'scenario': instance}
            )
            npc_serializer.is_valid(raise_exception=True)
            npc_serializer.save()

        instance.save()
        return instance
