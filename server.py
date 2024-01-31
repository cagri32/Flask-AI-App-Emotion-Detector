"""
This is the main module for the Emotion Detector application.

It contains the Flask application setup and routes.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using detect_emotion()
        function. The output returned shows the emotion scores
        and dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    if anger is None:
        return "Invalid input ! Try again."
    emotions = {
        'anger': anger, 
        'disgust': disgust, 
        'fear': fear, 
        'joy': joy, 
        'sadness': sadness
        }
    dominant_emotion = max(emotions, key=emotions.get)
    result = "For the given statement, the system response is \n"
    result += "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, and 'sadness': {}. "
    result += "\nThe dominant emotion is {}."
    return result.format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    '''Renders HTML '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    