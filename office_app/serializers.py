from rest_framework import serializers, fields

from .models import *


class ManagementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Management
        fields = ('text_ru', 'text_uz', 'created_at', 'updated_at', 'publish')


class RegionalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regional
        fields = ('title_uz', 'title_ru', 'image', 'numbers', 'address', 'publish', 'created_at', 'updated_at')


class GuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = ('post_ru', 'post_uz', 'name_ru', 'name_uz', 'work_time_ru', 'work_time_uz', 'contact',
                  'work_contact', 'photo', 'publish')


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ('text_ru', 'text_uz')


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('title_ru', 'title_uz', 'created_at', 'updated_at', 'publish')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['post_ru', 'post_uz', 'name_ru', 'name_uz',
                  'photo', 'text_ru', 'text_uz', 'organization']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title_ru', 'title_uz', 'text_ru', 'text_uz', 'publish')


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['title_ru', 'title_uz', 'pdf_ru', 'pdf_uz']


class OpenDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenData
        fields = ['title_ru', 'title_uz', 'pdf_ru', 'pdf_uz']
