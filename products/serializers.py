from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class CoffeeMachineSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    model = ChoiceField(choices=CoffeeMachine.MODEL_CHOICES)
    machine_type = ChoiceField(choices=CoffeeMachine.MACHINE_TYPE_CHOICES)
    class Meta:
        model = CoffeeMachine
        fields = ['name', 'machine_type', 'water_line_compatible', 'model']
        # read_only_fields = []

    def get_name(self, object):
        return f'{object.machine_type}{object.model}'

class CoffeePodSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    pod_type = ChoiceField(choices=CoffeePod.POD_TYPE_CHOICES)
    flavor = ChoiceField(choices=CoffeePod.FLAVOR_CHOICES)
    package_size = ChoiceField(choices=CoffeePod.PACKAGE_SIZE_CHOICES)
    class Meta:
        model = CoffeePod
        fields = ['name', 'pod_type', 'flavor', 'package_size']
        # read_only_fields = []

    def get_name(self, object):
        return f'{object.pod_type}{object.flavor}{object.package_size}'