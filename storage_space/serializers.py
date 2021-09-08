from rest_framework import serializers


class NewStoredIngredientSerializer(serializers.Serializer):
    dataMatrix = serializers.CharField(max_length=100)


class EditStoredIngredientSerializer(serializers.Serializer):
    kg = serializers.IntegerField()
    stored_in = serializers.ChoiceField(
        choices=("pantry", "freezer", "fridge"))

    def update(self, instance, validated_data):
        if validated_data['stored_in'] == "pantry":
            instance.kg_in_pantry = validated_data['kg']
        elif validated_data['stored_in'] == "freezer":
            instance.kg_in_freezer = validated_data['kg']
        elif validated_data['stored_in'] == "fridge":
            instance.kg_in_fridge = validated_data['kg']
        else:
            raise Exception

        instance.save()
        return instance
