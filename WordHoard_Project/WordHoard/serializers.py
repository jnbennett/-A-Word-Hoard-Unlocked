from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from WordHoard.models import Text, Author, Translator

class TextSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.PrimaryKeyRelatedField(read_only=True)
	# author = serializers.HyperlinkedRelatedField(read_only=True, view_name='WordHoard:author-detail')
	class Meta:
		model = Text
		fields = ('pk', 'title', 'author', 'publication_date', 'time_period', 'genre', 'translation', 'translator', 'txt_file')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	texts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='WordHoard:text-detail')

	class Meta:
		model = Author
		fields = ('pk', 'first_name', 'last_name', 'date_birth', 'date_death', 'gender', 'texts')


class TranslatorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Translator
		fields = ('first_name', 'last_name')
		