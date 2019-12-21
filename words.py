import nltk
import re
from nltk.corpus import stopwords

nltk.download('stopwords')

def frequency(url):

	#test_phrase = "Hi, this is a a string! But it has punctuation. How can we remove it? Hi, Bye. this is me me ."
	myfile = open(url, "rt") 
	test_phrase = myfile.read() 
	print(test_phrase)

	test_phrase=test_phrase.lower()

	en_stops = set(stopwords.words('english'))

	# frequency of words in a paragraph after removing stop words
	phrase = re.findall('[^?!. ]+', test_phrase)
	new_phrase=[]
	for w in phrase: 
		if w not in en_stops:
			new_phrase.append(w)
	#print("paragraph after removing all the stop words: ",new_phrase)

	freq=[]
	for p in new_phrase:
		freq.append(new_phrase.count(p))
	#print(freq)
	print("frequency of each word in the paragraph:\n ",str(list(zip(new_phrase, freq))))


	#frequency of words in each sentence after removing the stop words
	phrase= re.split('\s+',test_phrase)
	sentence=[]
	for w in phrase: 
		if w not in en_stops:
			sentence.append(w)

	new_sentence=' '
	new_sentence= new_sentence.join(sentence)
	#print(new_sentence) #paragraph after removing the stop words

	s=re.findall('[^!.?]+', new_sentence)
	s=s[:-1]
	#print(s)

	words= []
	for i in s:
		sentences= re.findall('[^!?. ]+',i)
		#print(sentences)
		words.append(sentences)
	#print(words)
	#for j in words:
	#	print(len(j)) 
	print("frequency of words in each sentence: ")
	for i in range(0,len(words)):
		wordfreq = []

		for w in words[i]:
			wordfreq.append(words[i].count(w))
		#print(wordfreq)
		print(str(list(zip(words[i], wordfreq))))
		#print("\n")

	myfile.close()

frequency("test_phrase.txt")