def get_suggestion(emotion):
    return {
        "joy": "Keep doing what makes you happy!",
        "sadness": "Take rest and talk to someone you trust.",
        "anger": "Take a deep breath and relax.",
        "fear": "Stay calm and take small steps forward.",
        "surprise": "Stay positive and enjoy the moment!",
        "neutral": "Keep going, you're doing well."
    }.get(emotion, "Stay positive!")
