import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion API and returns formatted emotion scores
    """

    # Watson NLP API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Required header
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send request
    response = requests.post(url, json=input_json, headers=headers)

    # Error handling for blank input
    if response.status_code == 400:
        return None

    # Convert response to JSON
    formatted_response = response.json()

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
