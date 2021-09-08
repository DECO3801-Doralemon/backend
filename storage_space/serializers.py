from rest_framework import serializers

# class CreateStorageSerializer(serializers.Serializer):
#     data_matrix = serializers.CharField(max_length=100)


# class GTINSerializer(serializers.Serializer):
#     gtin = serializers.CharField(max_length=100)


class EditStorageSerializer(serializers.Serializer):
    kg = serializers.IntegerField(min_value=0)

    def update(self, instance, validated_data):
        if (kg := validated_data['kg']) > 0:
            instance.kg = kg
            instance.save()
        else:
            instance.delete()

        return instance
