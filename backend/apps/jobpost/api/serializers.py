import re
from rest_framework import serializers
from django.utils.html import strip_tags
from ..models import JobPost, Company



class FormatMixins:
    def truncate(self, text, length=200):
        return f"{text[:length - 3]}..." if len(text) > length else text[:length] 
    
    def format(self, text):
        if isinstance(text, str):
            text = re.sub('</?strong>', '', text)
            text = re.sub('<h[1-9]>[^<]+</h[1-9]>', '', text)
            
            return self.truncate(strip_tags(text).strip())


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'name',
            'logo'
        ]


class ListJobPostSerializer(serializers.HyperlinkedModelSerializer, FormatMixins):
    categories = serializers.StringRelatedField(many=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = JobPost
        fields = [
            'title',
            'description',
            'origin_url',
            'release_date',
            'categories',
            'company'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['description'] = self.format(data['description'])

        return data
    

class ListCompanySerializer(serializers.HyperlinkedModelSerializer, FormatMixins):
    class Meta:
        model = Company
        fields = [
            'name',
            'logo',
            'website',
            'description',
            'slug'
        ]

    @property
    def is_list(self):
        return len(self._args) > 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['url'] = f'/companies/{data.get("slug", "")}'

        if isinstance(self._args[0], list):
            data['description'] = self.format(data['description'])

        return data
