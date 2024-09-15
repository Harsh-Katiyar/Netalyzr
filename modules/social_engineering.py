import os

# Disable oneDNN optimizations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Import TensorFlow after setting the environment variable
import tensorflow as tf
import re
import json
import pytz
import datetime
import matplotlib.pyplot as plt
from collections import Counter
from geopy.geocoders import Nominatim
from transformers import pipeline  # For advanced NLP tasks (Sentiment, NER, Text Summarization)
import cv2  # OpenCV for image processing

# Define your functions here

def extract_geolocation(image_path):
    print("\nExtracting Geolocation from Image...")
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Example coordinates (you would extract this from metadata in real usage)
    location = geolocator.reverse("52.509669, 13.376294")
    print(f"Location: {location.address}")

def time_series_analysis(posts):
    print("\nPerforming Time Series Analysis...")
    print("Analyzing posting frequency over time...")
    times = [datetime.datetime.strptime(post['date'], "%Y-%m-%d %H:%M:%S") for post in posts]
    time_counter = Counter([time.strftime('%H') for time in times])

    plt.bar(time_counter.keys(), time_counter.values())
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Posts')
    plt.title('User Posting Pattern')
    plt.show()

def hashtag_analysis(posts):
    print("\nRunning Hashtag and Keyword Analysis...")
    hashtags = []
    keywords = []
    for post in posts:
        hashtags += re.findall(r"#(\w+)", post['content'])
        keywords += re.findall(r"\b\w+\b", post['content'].lower())

    hashtag_count = Counter(hashtags)
    keyword_count = Counter(keywords)

    print("\nMost Common Hashtags:")
    for tag, count in hashtag_count.most_common(5):
        print(f"{tag}: {count} times")

    print("\nMost Common Keywords:")
    for word, count in keyword_count.most_common(5):
        print(f"{word}: {count} times")

def bot_detection(user_data):
    print("\nRunning Bot Detection...")
    # Placeholder for a machine learning model that analyzes post frequency, language, etc.
    bot_likelihood = "Bot" if user_data.get('post_frequency') > 50 else "Human"
    print(f"Likelihood that account is a bot: {bot_likelihood}")

def engagement_analysis(posts):
    print("\nRunning Engagement Analysis...")
    engagements = [post['likes'] + post['shares'] + post['comments'] for post in posts]
    total_engagement = sum(engagements)
    avg_engagement = total_engagement / len(posts) if posts else 0

    print(f"\nTotal Engagement: {total_engagement}")
    print(f"Average Engagement per Post: {avg_engagement:.2f}")

def sentiment_analysis(posts):
    print("\nPerforming Sentiment Analysis...")
    classifier = pipeline("sentiment-analysis")
    for post in posts:
        sentiment = classifier(post['content'])
        print(f"Post: {post['content']}\nSentiment: {sentiment}\n")

def named_entity_recognition(posts):
    print("\nPerforming Named Entity Recognition (NER)...")
    ner_model = pipeline("ner", grouped_entities=True)
    for post in posts:
        entities = ner_model(post['content'])
        print(f"Post: {post['content']}\nEntities: {entities}\n")

def text_summarization(posts):
    print("\nPerforming Text Summarization...")
    # Use a different model identifier
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    for post in posts:
        summary = summarizer(post['content'], max_length=30, min_length=5, do_sample=False)
        print(f"Post: {post['content']}\nSummary: {summary}\n")
def object_detection(image_path):
    print("\nRunning Object Detection...")
    # Load a pre-trained model for object detection (Example model in TensorFlow)
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (224, 224))
    predictions = model.predict(image_resized.reshape(1, 224, 224, 3))
    print("Detected objects:", predictions)

def image_segmentation(image_path):
    print("\nPerforming Image Segmentation...")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print("Segmentation completed.")

def toxicity_detection(posts):
    print("\nRunning Toxicity Detection...")
    toxicity_classifier = pipeline("text-classification", model="unitary/toxic-bert")
    for post in posts:
        result = toxicity_classifier(post['content'])
        print(f"Post: {post['content']}\nToxicity: {result}\n")

def social_graph_analysis(user_data):
    print("\nPerforming Social Graph Analysis...")
    print("Analyzing connections, followers, and interactions for graph analysis...")
    # Example simulation; real-world scenario would use network analysis tools.
    print(f"User {user_data['name']} has connections with 150 followers and 80 interactions.")

def influence_score(posts):
    print("\nCalculating Social Media Influence Score...")
    engagements = [post['likes'] + post['shares'] for post in posts]
    influence_score = sum(engagements) / len(posts) if posts else 0
    print(f"Influence Score: {influence_score:.2f}")

def export_data(data, filename="social_media_data.json"):
    print(f"\nExporting data to {filename}...")
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    print("Data export completed.")

def main():
    while True:
        print("\n*** Enhanced Social Networking OSINT Tool ***")
        print("1. NLP Sentiment Analysis")
        print("2. Named Entity Recognition (NER)")
        print("3. Text Summarization")
        print("4. Object Detection in Images")
        print("5. Image Segmentation")
        print("6. Toxicity Detection in Social Media Posts")
        print("7. Analyze Video")
        print("8. Social Graph Analysis")
        print("9. Calculate Social Media Influence Score")
        print("10. Export Data")
        print("11. Geolocation Extraction from Social Media Posts")
        print("12. Time Series Analysis of User Posts")
        print("13. Hashtag and Keyword Analysis")
        print("14. AI-Powered Bot Detection")
        print("15. Social Media Engagement Analysis")
        print("0. Exit")
        choice = input("Choose an option (1-15): ")

        if choice == '1':
            posts = [{"content": "I love programming!"}, {"content": "AI is amazing."}]
            sentiment_analysis(posts)
        elif choice == '2':
            posts = [{"content": "Elon Musk is the CEO of Tesla."}]
            named_entity_recognition(posts)
        elif choice == '3':
            posts = [{"content": "Artificial intelligence is the simulation of human intelligence by machines."}]
            text_summarization(posts)
        elif choice == '4':
            image_path = input("Enter image path for object detection (e.g., '/path/to/image.jpg'): ")
            object_detection(image_path)
        elif choice == '5':
            image_path = input("Enter image path for segmentation (e.g., '/path/to/image.jpg'): ")
            image_segmentation(image_path)
        elif choice == '6':
            posts = [{"content": "You are a bad person!"}]
            toxicity_detection(posts)
        elif choice == '8':
            user_data = {"name": "John Doe"}
            social_graph_analysis(user_data)
        elif choice == '9':
            posts = [{"likes": 100, "shares": 50}, {"likes": 120, "shares": 60}]
            influence_score(posts)
        elif choice == '10':
            data = [{"user": "John Doe", "content": "Sample post"}]
            export_data(data)
        elif choice == '11':
            image_path = input("Enter image path for geolocation extraction (e.g., '/path/to/image.jpg'): ")
            extract_geolocation(image_path)
        elif choice == '12':
            posts = [{"date": "2023-09-01 12:00:00", "content": "First post"},
                     {"date": "2023-09-01 14:00:00", "content": "Second post"}]
            time_series_analysis(posts)
        elif choice == '13':
            posts = [{"content": "Loving the #sunny weather today!"}]
            hashtag_analysis(posts)
        elif choice == '14':
            user_data = {"post_frequency": 100}
            bot_detection(user_data)
        elif choice == '15':
            posts = [{"likes": 100, "shares": 50, "comments": 20}, {"likes": 120, "shares": 60, "comments": 25}]
            engagement_analysis(posts)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
