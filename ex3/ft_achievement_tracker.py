import random


ACHIEVEMENTS = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer", "Strategist",
    "Speed Runner", "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Unstoppable", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, amount))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    print("=== Achievement Analytics ===")

    all_unique = alice.union(bob).union(charlie).union(dylan)
    common_all = (alice.intersection(bob).intersection(charlie)
                  .intersection(dylan))

    print(f"All distinct achievements: {all_unique}")
    print(f"Common achievements: {common_all}\n")

    alice_only = alice.difference(bob).difference(charlie).difference(dylan)
    bob_only = bob.difference(alice).difference(charlie).difference(dylan)
    charlie_only = (charlie.difference(alice).difference(bob)
                    .difference(dylan))
    dylan_only = dylan.difference(alice).difference(bob).difference(charlie)
    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}\n")

    all_achievements = set(ACHIEVEMENTS)
    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()
