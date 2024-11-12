import cohere
api_key = '<your-api-key>'

co = cohere.Client(api_key)
co.check_api_key()

res_embed = co.embed(
    texts=['こんにちは', '世界'],
    model='embed-multilingual-v2.0'
)

print(res_embed)
