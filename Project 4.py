def classify_sentiment(text):
    positive_words = {"good", "great", "excellent", "love", "best"}
    negative_words = {"bad", "terrible", "hate", "worst", "awful"}
    
    words = text.lower().split()
    pos_count = sum(1 for w in words if w in positive_words)
    neg_count = sum(1 for w in words if w in negative_words)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    return "Neutral"

print(classify_sentiment("This movie is great and excellent"))