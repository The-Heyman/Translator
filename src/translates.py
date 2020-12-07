import boto3

client = boto3.client("translate", region_name="us-east-1")
text = "Hvor gammel er du?"
result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")
print(result['TranslatedText'])