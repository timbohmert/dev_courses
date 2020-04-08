#preloaded lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#builing point dictionary
letters_to_points = {key: value for key, value in zip(letters, points)}

letters_to_points[" "] = 0

#program to score a word

def score_word(word):
    point_total = 0
    for l in word:
        point_total += letters_to_points.get(l, 0)
    return point_total

#score a game
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi_Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof_Reader': ['ZAP', 'COMA', 'PEROID']}

player_to_points = {}

def updated_points_total:
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

#Add word to dictionairy
def play_word(player, word):
    player_to_words[player].append(word)
    updated_points_total

play_word('player1', 'HELLO')

print(player_to_words)