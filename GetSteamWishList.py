# """ get games and piece in wishlist """
import re
import json
import requests

your_steam_user_id = ""

url = f"https://store.steampowered.com/wishlist/profiles/{ your_steam_user_id }"
wishlist_url =  json.loads(re.findall(r'g_strWishlistBaseURL = (".*?");', requests.get(url).text)[0])

sum_of_price = 0
total_games = 0

page = 0
while 1 :
    data = requests.get(wishlist_url + f"wishlistdata/?p={ page }").json()
    # print(json.dumps(data, indent=4))

    if not len(data) : break
    total_games += len(data)

    for d in data :
        name = data[d]['name']

        try :
            price = int(data[d]['subs'][0]['price'][:-2])
            print(f"name : { name }, price : { price }.")
        except IndexError:
            price = 0
            print(f"name : { name }, price : None.")

        sum_of_price += price

    page += 1

print(f"\nTotal games: { total_games }")
print(f"\nTotal price: { sum_of_price }")