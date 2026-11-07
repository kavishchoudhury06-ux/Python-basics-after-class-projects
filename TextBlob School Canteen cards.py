from textblob import TextBlob

POSITIVE, NEGATIVE = 0.25, -0.25

feedback = [
    "The pasta was delicious and the staff were friendly.",
    "The queue was too long and the soup was cold.",
    "Lunch was okay.",
    "I love the new fruit salad!",
    "The chairs are broken and the room is dirty.",
    "Great, they forgot my order again.",
    "The pizza on Friday is amazing.",
    "Food is served at noon.",
]

print(f"{len(feedback)} feedback cards")

# ---------- PART 1: score every card ----------
print("\nPART 1: Scores")

scores = [TextBlob(card).sentiment.polarity for card in feedback]

for score, card in zip(scores, feedback):
    print(f"{score:+.2f}  {card}")

# ---------- PART 2: moods and counts ----------
print("\nPART 2: Moods")

moods = []

for score in scores:
    if score > POSITIVE:
        moods.append("Positive")
    elif score < NEGATIVE:
        moods.append("Negative")
    else:
        moods.append("Neutral")

print(f"Positive: {moods.count('Positive')}")
print(f"Neutral: {moods.count('Neutral')}")
print(f"Negative: {moods.count('Negative')}")

# ---------- PART 3: best and worst ----------
print("\nPART 3: Best and worst")

best_pos = scores.index(max(scores))
worst_pos = scores.index(min(scores))

print(f"Best ({scores[best_pos]:2f}): {feedback[best_pos]}")
print(f"Worst ({scores[worst_pos]:2f}): {feedback[worst_pos]}")

# ---------- PART 4: why the worst card scored low ----------
print("\nPART 4: Clues for the worst card")

worst_card = feedback[worst_pos]

for word in worst_card.split():
    clean_word = word.strip(".,!?;:").lower()
    word_score = TextBlob(clean_word).sentiment.polarity

    if word_score != 0:
        print(f"{clean_word} {word_score:+.2f}")