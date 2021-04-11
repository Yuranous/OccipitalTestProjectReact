from rest_framework import serializers

from backend.models import Task, Commentary


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'status']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TranslationAddSerializer(serializers.Serializer):
    translation = serializers.CharField()
    task_id = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class CommentaryAddSerializer(serializers.Serializer):
    commentary = serializers.CharField()
    task_id = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
