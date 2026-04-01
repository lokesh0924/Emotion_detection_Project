def get_suggestion(emotion):
    # Normalize emotion
    emotion = str(emotion).lower().strip()

    suggestions = {
        "joy": "That's wonderful! Keep doing what makes you happy 😊",
        "sadness": "Take some rest and talk to someone you trust 💙",
        "anger": "Pause and take deep breaths. Try to relax 😌",
        "fear": "Stay calm and focus on what you can control 💪",
        "surprise": "Hope it's a pleasant surprise! Stay positive 😄",
        "neutral": "You're doing fine. Keep going 👍"
    }

    return suggestions.get(emotion, f"Try to stay positive and take care! (Detected: {emotion})")