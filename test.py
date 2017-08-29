from waapi import waAPI

key = 'YOUR-WOLFRAMALPHA-API-KEY'

api = waAPI(key)

spoken  = api.spoken_results(i="stock price of google")

print spoken
