from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from .models import Text, Author, Translator
from .serializers import TextSerializer, AuthorSerializer, TranslatorSerializer
from .search_functions import occurence, word_count
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
	queryset = Text.objects.filter()
	serializer_class = TextSerializer

def search(request):
	
	if request.method == 'POST':
		data = json.loads(request.body)
		print(data)
		texts = Text.objects.filter(author=data['author']['pk'])
		for text in texts:
			with open(text.txt_file.path) as f:
				read = f.read()
				# read = tokenize(read.lower())	
				word_search = occurence(read, data['word'])
				count = word_count(read, data['word'])
				
				search_results = {
					'author': data.get('author'),
					'text': data.get('text'),
					'word': data.get('word'),
					'sentences': word_search,
					'count': count,
					}
				return JsonResponse(search_results, safe=False)
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



