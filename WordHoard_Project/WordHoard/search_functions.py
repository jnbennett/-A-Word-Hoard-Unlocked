import nltk
from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize


def word_occurence(text, word):
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
def phrase_occurence(text, phrase):
	# words = [word_tokenize(word) for word in sent_tokenize(text)]
	sentences = sent_tokenize(text)

	phrase_list = [sentences[i] for i in range(len(sentences)) if phrase in sentences[i]]

	return phrase_list

def word_count(text, word):
	"""
	returns number of times a given word occurs.
	"""
	token = word_tokenize(text)
	return token.count(word)

def phrase_count(text, phrase):
	"""
	returns number of times a phrase occurs

	"""
	token = sent_tokenize(text)
	return token.count(phrase)
# def tokenize(text):
# 	return nltk.word_tokenize(text)

# nltk.TextCollection can import multiples texts to analyze
