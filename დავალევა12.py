
print("დავალება 13")

import os, sys, json


def create_json_file(path, file):
  file_path = None

  if len(path.split('/')) == 2:
    file_path = f"{path}/{file}.json"

    os.makedirs(path, exist_ok=True)
  
  try:
    with open(file_path, mode='x', encoding='utf-8'):
      ...
  except FileExistsError:
    print(f"File '{file_path}' already exists...")
    print("Keep working...\n\n")
  except TypeError:
    print("The path must by two-level... For example 'files/jsons'")
    print("Exit...")
    sys.exit()
  
  return file_path


def write_json_file(path, json_data: list):
  with open(path, mode='w', encoding='utf-8') as f:
    f.write(json.dumps(json_data, indent=2))

def read_json_file(path):
  with open(path, mode='r', encoding='utf-8') as f:
    return json.loads(f.read())


def add_player_to_json_file(path, data: dict):
  players = read_json_file(path)

  if type(data['id']) != int:
    print("Players ID must by integer. Please try again...\n")
    return

  for player in players:
    if player['id'] == data['id']:
      print(f"Player with ID '{data['id']}' already exixts...")
      return
  else:
    players.append(data)
    players.sort(key=lambda x: x['id'])

  write_json_file(path, players)


def update_json_file(path):
  players = read_json_file(path)
  data = {}
  
  data['id'] = input("\nID [Press 'Enter' to exit]: ") or None

  if data['id'] is None or not data['id'].isdigit():
    print("ID must by integer. Please, try again...\n")
    return
  
  for i in range(len(players)):
    data['id'] = int(data['id'])
    
    if data['id'] == players[i]['id']:
      print(players[i], "\n")

      data['name'] = input("Name ['Press 'Enter' to continue']: ") or players[i]['name']
      data['country'] = input("Country ['Press 'Enter' to continue']: ") or players[i]['country']

      data['rating'] = input("Rating ['Press 'Enter' to continue']: ")
      data['rating'] = int(data['rating']) if data['rating'].isdigit() else players[i]['rating']

      data['age'] = input("Age ['Press 'Enter' to continue']: ")
      data['age'] = int(data['age']) if data['age'].isdigit() else players[i]['age']

      print(f"\n{data}")
      
      players[i] = data

      break
  else:
    print(f"\nPlayer with ID '{data["id"]}' not found")
    print("exit...\n")
    return
  
  question = input("\nWrite data to a file [y/n]? ")
                   
  if question.lower() != 'n':
    write_json_file(path, players)
    print("Data has been written success")
  else:
    print("Data has not been written")

