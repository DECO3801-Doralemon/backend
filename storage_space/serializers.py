from rest_framework import serializers


class EditStorageSerializer(serializers.Serializer):
    kg = serializers.IntegerField(min_value=0)

    def update(self, instance, validated_data):
        kg = validated_data['kg']
        if kg > 0:
            instance.kg = kg
            instance.save()
        else:
            instance.delete()

        return instance
