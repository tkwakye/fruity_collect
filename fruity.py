import requests

base_url = 'https://www.fruityvice.com/api/fruit/'

fruit_name = 'apple'
actualurl = base_url + fruit_name
text = {'fruit':fruit_name}

try:
  response = requests.get(actualurl)

  if response.status_code == 200:
    fruit_info = response.json()

    print(f"Fruit Name: {fruit_info['name']}")
    print(f"Genus: {fruit_info['genus']}")
    print(f"Family: {fruit_info['family']}")
    print(f"Order: {fruit_info['order']}")

  else:
    print(f"Failed. Status code: {response.status_code}")

except requests.exceptions.RequetException as e:
  print(f"Error getting the data: {e}")


