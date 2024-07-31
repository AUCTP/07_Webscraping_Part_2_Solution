import requests
import json

def query_listings(offset):
    querystring = {"offset": offset}
    response = requests.post(url, data=payload, headers=headers, params=querystring)
    data = json.loads(response.text)
    return data

def parse_listings(listing):
    url = listing['url']
    title = listing['title']
    rooms = listing['rooms']
    size = listing['size_m2']
    rent = listing['monthly_rent']
    data = {
        'url': url,
        'title': title,
        'rooms': rooms,
        'size': size,
        'rent': rent
    }
    return data

def print_info(house):
    print(30*'-')
    print(f'Title: {house["title"]}')
    print(f'Rooms: {house["rooms"]}')
    print(f'Rent: {house["rent"]}')
    print(30*'-')
    print()


url = "https://www.boligportal.dk/en/api/search/list"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

payload = "{\"categories\":{\"values\":null},\"city_level_1\":{\"values\":[\"Aarhus\"]}}"


offset = 0
listings = []
max_offset = 100
while True:
    data = query_listings(offset)
    # total = int(data['result_count'])
    listings += (data['results'])
    if offset >= max_offset:
        break
    else:
        offset += 18

houses = []
for listing in listings:
    data = parse_listings(listing)
    houses.append(data)

for house in houses:
    print_info(house)