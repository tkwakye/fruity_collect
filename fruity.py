import requests
import pandas as pd
import sqlalchemy as db


base_url = 'https://www.fruityvice.com/api/fruit/'

fruit_name = input('Enter fruit name: ')
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

    fruit_data = {
      'name': fruit_info['name'],
      'genus': fruit_info['genus'],
      'family': fruit_info['family'],
      'order': fruit_info['order'],
      'calories': fruit_info['nutritions']['calories'],
      'fat': fruit_info['nutritions']['fat'],
      'sugar': fruit_info['nutritions']['sugar'],
      'carbohydrates': fruit_info['nutritions']['carbohydrates'],
      'protein': fruit_info['nutritions']['protein'],

    }

    df = pd.DataFrame.from_dict([fruit_data])
    engine = db.create_engine('sqlite:///fruits.db')
    df.to_sql('fruits', con=engine, if_exists='replace', index = False)
    with engine.connect() as connection:

      query_result = connection.execute(db.text("SELECT * FROM fruits;")).fetchall()
      print(pd.DataFrame(query_result))
  else:
    print(f"Failed. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
  print(f"Error getting the data: {e}")


