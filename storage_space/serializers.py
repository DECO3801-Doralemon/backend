from rest_framework import serializers


class CreateStorageSerializer(serializers.Serializer):
    dataMatrix = serializers.CharField(max_length=100)


class EditStorageSerializer(serializers.Serializer):
    kg = serializers.IntegerField()


class EditFreezerStorageSerializer(EditStorageSerializer):
    def update(self, instance, validated_data):
        instance.kg = validated_data['kg']
        instance.save()
        return instance


class EditFridgeStorageSerializer(EditStorageSerializer):
    def update(self, instance, validated_data):
        instance.kg = validated_data['kg']
        instance.save()
        return instance


class EditPantryStorageSerializer(EditStorageSerializer):
    def update(self, instance, validated_data):
        instance.kg = validated_data['kg']
        instance.save()
        return instance
