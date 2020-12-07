import boto3

def compute_translation(text, src="auto", target="en"):
    
    ''' Translate text from different supported languages to English by 
        default or to an specified target. 
        :params text: text to be translated.
                src: language to be translated.
                target: language to translate to.
        :return: a translated string of the input text string
    '''
    
    client = boto3.client("translate", region_name="us-east-1")
    
    result = client.translate_text(Text=text, SourceLanguageCode=src, 
            TargetLanguageCode=target)
    
    return result['TranslatedText']
    
# test example

compute_translation("Til at understøtte hjemmesidens", "auto","it")

# the above translates from danish using auto detect to Italian as specified.