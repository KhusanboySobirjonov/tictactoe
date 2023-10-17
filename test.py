import json

data = {
    "fplayer_name": "asd",
    "splayer_name": "asd",
    "choose_char": "ada"
}

with open("data_players.json", "w") as f:
    json.dump(data, f)
