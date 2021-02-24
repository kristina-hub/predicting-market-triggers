import re
class CleanTokens(object):
    
    def clean_pattern(self, text, pattern):
        r = re.findall(pattern, text)
        for search_term in r:
            text = re.sub(search_term, '', text)        
        return text
    
    def clean_noise(self, text):
        cleaned_return_handler = self.clean_pattern(text, "RT @[\w]*:")
        cleaned_handler = self.clean_pattern(cleaned_return_handler, "@[\w]*")
        cleaned_links = self.clean_pattern(cleaned_handler, "https?://[A-Za-z0-9./]*")
        cleaned_tokens = re.sub("(@[A-Za-z0-9_]+)","", cleaned_links)
        return cleaned_tokens