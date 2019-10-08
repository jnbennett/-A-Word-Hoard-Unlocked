from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Text, Author, Translator
from .serializers import TextSerializer, AuthorSerializer, TranslatorSerializer
from .search_functions import word_occurence, word_count, word_tokenize, phrase_occurence, phrase_count
from collections import Counter
import json

class AuthorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint to allows Authors to be viewed
	"""
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class TranslatorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint to allow translators to be viewed
	"""
	queryset = Translator.objects.all()
	serializer_class = TranslatorSerializer

class TextViewSet(viewsets.ModelViewSet):
	"""
	API endpoint to allow texts to be viewed
	"""
	queryset = Text.objects.all()
	serializer_class = TextSerializer

class HomePageView(TemplateView):
	template_name = 'WordHoard/index.html'

class SearchPageView(TemplateView):
	template_name = 'WordHoard/search.html'

def search(request):
	
	if request.method == 'POST':
		data = json.loads(request.body)
		
		text_keys = [item['pk'] for item in data['text']]
		author_keys = [item['pk'] for item in data['author']]
		time_period_keys = [item for item in data['time_period']]
		
		
		if data['time_period']:
			texts = Text.objects.filter(time_period__in=time_period_keys)
		if data['author']:
			texts = Text.objects.filter(author__in=author_keys)
			
		if data['text']:
			texts = Text.objects.filter(pk__in=text_keys)
		
		search_results = []
		for text in texts:
			with open(text.txt_file.path) as f:
				read = f.read()
				# read = tokenize(read.lower())	
				word_search = word_occurence(read, data['word'])
				count_word = word_count(read, data['word'])
				phrase = phrase_occurence(read, data['word'])
				# count_phrase= phrase_count(read, data['word'])
				count_phrase = len(phrase)
				if data['search_type']== 'Word':
					results = {
						'author': text.author.first_name +' '+ text.author.last_name,
						'text': text.title,
						'word': data.get('word'),
						'sentences': word_search,
						'word_count': count_word,
						}
					search_results.append(results)
				if data['search_type'] == 'Phrase':
					results = {
						'author': text.author.first_name +' '+ text.author.last_name,
						'text': text.title,
						'word': data.get('word'),
						'word_count': count_phrase,
						'sentences': phrase,
						}
					search_results.append(results)
		return JsonResponse(search_results, safe=False)
	# return JsonResponse(search_results, safe=False)
	return HttpResponse(201)
	






# texts = []
# for name in data['authors']:
# 	author = name 
# 	texts.append(Texts.objects.filter(author=author)
# for word in texts:
			
		
# return JsonResponse

# def texts(request):

# 	if request.method=='GET':
# 		# data = json.loads(request.GET)

# 		texts = Text.objects.all()
# 		# text = get_object_or_404(Text, pk=pk)
# 		txt_list = []
# 		for text in texts:
# 			text_dict = {
# 				'pk': text.pk,
# 				'title': text.title,
# 				'author': text.author.first_name +' '+ text.author.last_name,
# 				'genre': text.genre,
# 				'translation': text.translation,
# 				'translator': text.translator,
# 				'txt_file': text.txt_file
# 			}

# 			txt_list.append(text_dict)
# 	return JsonResponse(txt_list, safe=False)

	# return HttpResponse(status=201)



