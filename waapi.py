import requests

#full result
#https://api.wolframalpha.com/v2/query?input=bitcoin+at+blockchain&format=image,plaintext&output=XML&appid=DEMO
FR_ROOT = 'https://api.wolframalpha.com/v2/query'

#query recognizer
#http://www.wolframalpha.com/queryrecognizer/query.jsp?appid=DEMO&mode=Default
QR_ROOT = 'http://www.wolframalpha.com/queryrecognizer/query.jsp'

#short answers api
#https://api.wolframalpha.com/v2/result?i=What+is+the+stock+price+of+Twitter%3F&appid=DEMO
SA_ROOT = 'http://api.wolframalpha.com/v2/result'

#spoken result api
#'https://api.wolframalpha.com/v2/spoken?i=How+many+megabytes+are+in+a+gigabyte%3F&appid=DEMO'
SR_ROOT = 'https://api.wolframalpha.com/v2/spoken'

API_SIGNUP_PAGE = 'https://developer.wolframalpha.com'

class NoAPIKeyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class waAPI(object):
    def __init__(self, key = None):
        """
        Initializes the booksAPI class with a developer key. Raises an exception if a key is not given.
        
        Request a key at https://developer.wolframalpha.com
        
        :param key: Wolfram Alpha App ID Developer Key
        
        """
        self.key = key
        self.response_format = 'json'
        
        if self.key is None:
            raise NoAPIKeyException('Warning: Missing API Key. Please visit ' + API_SIGNUP_PAGE + ' to register for a key.')

    def spoken_results(self, 
                key = None, 
                i = None):
        """
        Calls the API and returns a string of text
                                
        :param key: a developer key. Defaults to key given when the waAPI class was initialized.
        
        :query examples:
			i = 'How many megabytes are in a gigabyte'			        
        """
        result = ''
        
        if key is None:
        	key = self.key
        
        if i is None:
        	result = 'Sorry, I did not get your question.'	
        else:
        	url = '%s?i=%s&appid=%s' % (
        	SR_ROOT, i.encode('utf8').lower(), key
        	)
        	r = requests.get(url)			
        	if r.text == 'No spoken result available': 
        		result = self.short_answers(i=i)
        	else:
        		result = r.text
        return result			
						
    def short_answers(self, 
                key = None, 
                i = None):
        """
        Calls the API and returns a string of text
                                
        :param key: a developer key. Defaults to key given when the waAPI class was initialized.
        
        :query examples:
			i = 'How many megabytes are in a gigabyte'			        
        """
        
        if key is None:
            key = self.key
        if i is None:
        	result = 'Sorry, I did not get your question.'	
        else:
        	url = '%s?i=%s&appid=%s' % (
        		SA_ROOT, i.encode('utf8').lower(), key
        		)
        	r = requests.get(url)
        	if r.text == 'No short answer available': 
        		result = 'This is a tough one. You got me.'
        	else:
        		result = r.text
        	return result	
			
    def query_recognizer(self, 
                response_format = None, 
                mode = 'Voice', 
                key = None, 
                i = None):
        """
        Calls the API and returns a dictionary of the search results
        
        :param response_format: the format that the API uses for its response, 
                                includes JSON (.json) and XML. 
                                Defaults to '.json'.
                                
        :param key: a developer key. Defaults to key given when the waAPI class was initialized.
        
        :query examples:
			i = 'How many megabytes are in a gigabyte'			        
        """
        if key is None:
            key = self.key
        if response_format is None:
        	response_format = self.response_format
        if i is None:
        	return 'Sorry, I did not get your question.'
        else:
        	url = '%s?i=%s&output=%s&mode=%s&appid=%s' % (
        		QR_ROOT, i.encode('utf8').lower(), response_format, mode, key
        		)
        	r = requests.get(url)
        	return r.json()

    def full_results(self, 
                response_format = None,     
                key = None, 
                i = None):
        """
        Calls the API and returns a dictionary of the search results
        
        :param response_format: the format that the API uses for its response, 
                                includes JSON (.json) and XML. 
                                Defaults to '.json'.
                                
        :param key: a developer key. Defaults to key given when the waAPI class was initialized.
        
        :**kwargs examples:
			query = 'How many megabytes are in a gigabyte'			        
        """
        if key is None:
            key = self.key
        if response_format is None:
        	response_format = self.response_format            
        if i is None:
        	return 'Sorry, I did not get your question.'
        else:
        	url = '%s?input=%s&output=%s&appid=%s' % (
        		QR_ROOT, i.encode('utf8').lower(), response_format, key
        		)
        	r = requests.get(url)
        	return r.json()						
	