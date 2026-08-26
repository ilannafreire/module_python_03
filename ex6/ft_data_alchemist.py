import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]
    capitalized_players = [player.capitalize() for player in players]
    original_capitalized = [player for player in players
                            if player == player.capitalize()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {original_capitalized}\n")

    scores = {player: random.randint(1, 1000)
              for player in capitalized_players}
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    high_scores = {player: score for player, score in scores.items()
                   if score > average_score}

    print(f"Score dict: {scores}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")
