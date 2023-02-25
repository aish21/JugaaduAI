from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
import numpy as np

# Sample dataset of text examples and their corresponding function categories
dataset = [
    ("Can you add the two input videos together", "Combine"),
    ("can you combine the two", "Combine"),
    ("can you combine them", "Combine"),
    ("can you add the two", "Combine"),
    ("Can you add them", "Combine"),
    ("can you combine them all", "Combine"),
    ("can you add them all", "Combine"),
    ("Can you combine the videos", "Combine"),
    ("can you add the videos", "Combine"),
    ("Can you add them all together", "Combine"),
    ("can you combine them all together", "Combine"),
    ("add them all together", "Combine"),
    ("combine them all together", "Combine"),
    ("combine videos", "Combine"),
    ("add videos", "Combine"),
    ("Add background music", "AddBGM"),
    ("Can you add background music", "AddBGM"),
    ("Add background music to my video", "AddBGM"),
    ("background music", "AddBGM"),
    ("bg music videos", "AddBGM"),
    ("Add background music to input", "AddBGM"),
    ("music background", "AddBGM"),
    ("Add music", "AddBGM"),
    ("music add", "AddBGM"),
    ("overlay with bg music", "AddBGM"),
    ("overlay with background music videos", "AddBGM"),
    ("overlay video with background music", "AddBGM"),
    ("add captions to the video", "AddCap"),
    ("add captions", "AddCap"),
    ("auto captions", "AddCap"),
    ("captions", "AddCap"),
    ("add subtitles to the video", "AddCap"),
    ("subtitle the video", "AddCap"),
    ("subtitles", "AddCap"),
    ("add subtitles", "AddCap"),
    ("add subs", "AddCap"),
    ("auto subs and caption", "AddCap"),
    ("trim the video from 10seconds for 3 seconds", "Trimming"),
    ("trim the video to 98 seconds", "Trimming"),
    ("trim the video in half", "Trimming"),
    ("trim the video", "Trimming"),
    ("trim the video in seconds", "Trimming"),
    ("cut the video in seconds", "Trimming"),
    ("cut the video from 10seconds for 3 seconds", "Trimming"),
    ("cut the video to 98 seconds", "Trimming"),
    ("cut the video in half", "Trimming"),
    ("cut the video", "Trimming"),
    ("cut the video at 5 seconds", "Trimming"),
    ("cut the video in 3s", "Trimming"),
    ("snip the video in 2 parts", "Snipping"),
    ("snip the video from 5 to 10 seconds", "Snipping"),
    ("break the video from 5 to 10 seconds", "Snipping"),
    ("snip the video", "Snipping"),
    ("break the video", "Snipping"),
    ("break the video into 3 parts", "Snipping"),
    ("snip the video at 5 seconds and 15 seconds", "Snipping"),
    ("break the video at 15 seconds and 35 seconds", "Snipping"),
    ("snip the video at 5 seconds for 15 seconds", "Snipping"),
    ("break the video at 5 seconds for 15 seconds", "Snipping"),
    ("compress the video", "Compression"),
    ("reduce the video size", "Compression"),
    ("reduce the size of the video", "Compression"),
    ("reduce video size", "Compression"),
    ("compress the video size", "Compression"),
    ("compress the size of the video", "Compression"),
    ("reduce video's size", "Compression"),
    ("reduce video", "Compression"),
    ("compress video", "Compression"),
    ("compress my video", "Compression"),
]

# Preprocess the text by removing stop words and converting to lowercase
preprocessed_text = [" ".join(word.lower() for word in example[0].split() if word not in stopwords.words('english')) for example in dataset]

# Convert the preprocessed text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(preprocessed_text)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, [example[1] for example in dataset], test_size=0.2, random_state=42)

# Train a Naive Bayes classifier on the training set
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Evaluate the classifier on the testing set
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Use the classifier to predict the function category of new text examples
new_text = ["Can you help me add captions to this video"]
new_preprocessed_text = [" ".join(word.lower() for word in example.split() if word not in stopwords.words('english')) for example in new_text]
new_features = vectorizer.transform(new_preprocessed_text)
new_pred = clf.predict(new_features)
print(new_pred)

def predText(textList):
    new_preprocessed_text = [" ".join(word.lower() for word in example.split() if word not in stopwords.words('english')) for example in new_text]
    new_features = vectorizer.transform(new_preprocessed_text)
    new_pred = clf.predict(new_features)
    text = new_pred.tostring().decode('utf-8')
    return text