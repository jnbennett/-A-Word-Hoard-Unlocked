import nltk
from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize


def occurence(text, word):
	"""
	return a concordance of word in text
	"""
	# phrase = nltk.Text(text)
	sents = [word_tokenize(t) for t in sent_tokenize(text)]
	sent_list = [' '.join(sents[i]) for i in range(len(sents)) if word in sents[i]]
	# for i in range(len(sents)):
	# 	if word in sents[i]:
	# 		sent_list.append(' '.join(sents[i])

	return sent_list
		
	# [word_tokenize(sents) for word in sents]
	# if word in  sents:
	# 	return sents

	

	# # return phrase.concordance(word)
	# return phrase.concordance_list(word)

# def analogous(text, word):
# 	return text.similar(word)
	

# def shared_context(text, word_list):
# 	return text.common_contexts(word_list)
	

def text_length(text):
	return len(text)

def word_count(text, word):
	"""
	returns number of times a given word occurs.
	"""
	token = word_tokenize(text)
	return token.count(word)

# def tokenize(text):
# 	return nltk.word_tokenize(text)

# nltk.TextCollection can import multiples texts to analyze
