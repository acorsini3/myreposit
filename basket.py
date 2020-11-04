players = ["Lebron James", "Anthony Davis", "James harden", "Giannis Antetokumpo", "Kevin Durant"]
print (players)
players.sort()
print (players)

number_of_players = len(players)
message = "In my team, there are " + str(number_of_players) + " players."
print(message)

print("I forgot myself !")
players.append("And myself !")
number_of_players = len(players)
message = "In my team, there are now " + str(number_of_players) + " players."
print(message)