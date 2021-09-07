from rest_framework import serializers


class StoredIngredientSerializer(serializers.Serializer):
    expired_date = serializers.DateField()
    weight = serializers.IntegerField()
    stored_in = serializers.ChoiceField(
        choices=("pantry", "freezer", "fridge"))

    def update(self, instance, validated_data):
        instance.expired_date = validated_data.get(
            'expired_date', instance.expired_date)
        
        if validated_data.stored_in == "pantry":
            instance.pantry_weight = validated_data.weight
        elif validated_data.stored_in == "freezer":
            instance.freezer_weight = validated_data.weight
        elif validated_data.stored_in == "fridge":
            instance.fridge_weight = validated_data.weight

        instance.save()
        return instance
