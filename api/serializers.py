from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Report, Category



class CategorySerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ('name', )


# Serializer classes form Creating and List the total reports:
class ReportListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    reporter = serializers.StringRelatedField()

    class Meta:
        model = Report
        fields = ('title', 'description','reported_time', 'date_reported', 'category',
            'reporter',
        )
        depth = 1

class ReportCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'description','reported_time', 'date_reported', 'category',
            'reporter',
        )







class UserSerializer(serializers.ModelSerializer):
    reporters = ReportListSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'username', 'reporters'
        ]

    def create(self, validated_data):
        reporters = validated_data.pop('reporters')
        report = User.objects.create(**validated_data)
        for reporter in reporters:
            Report.objects.create(report=report, **reporter)
        return report