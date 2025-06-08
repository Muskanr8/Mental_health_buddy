from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("sentiment-analysis")

def detect_mood(text):
    result = classifier(text)[0]
    label = result['label']
    
    if label == 'POSITIVE':
        mood = "Happy"
    elif label == 'NEGATIVE':
        mood = "Sad or Stressed"
    else:
        mood = "Neutral"
    
    return mood, result['score']
