first_basketball_player = {'full_name:': 'Michael Jordan', 'height:': 198}
second_basketball_player = {'full_name:': 'LeBron James', 'height:': 206}
third_basketball_player = dict({'full_name:': 'Magic Johnson', 'height:': 206})


first_basketball_player['birthday:'] = 'February 17, 1963'
second_basketball_player['current_team:'] = 'Los Angeles Lakers'
third_basketball_player['number:'] = 32

first_basketball_player.pop("height:")

print("Результат поиска: ", second_basketball_player.get("full_name:"), end="\n")
print("Результат поиска: ", third_basketball_player.get("current_team:"), end="\n\n")

first_basketball_player.update({"height:": "198"})
second_basketball_player.update({"current_team:": "Alexey team"})

for key, value in first_basketball_player.items():
    print(key, value)

print(end="\n")

for key, value in second_basketball_player.items():
    print(key, value)

print(end="\n")

for key, value in third_basketball_player.items():
    print(key, value)
