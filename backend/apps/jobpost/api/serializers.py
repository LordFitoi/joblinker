from rest_framework import serializers
from ..models import JobPost


class JobPostSerializer(serializers.HyperlinkedModelSerializer):
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = JobPost
        fields = [
            'title',
            'description',
            'release_date',
            'categories',
        ]
