import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class SpamClassifierModel:
    def __init__(self):
        self.tdidf_vectorizer = TfidfVectorizer(tokenizer=self._custom_tokenizer, token_pattern=None)
        data = pd.read_csv("sms_spam_collection.csv")
        X = data['message']
        y = data["target"]
        X_vectorized = self.tdidf_vectorizer.fit_transform(X)
        self.log_classifier = LogisticRegression(C=1).fit(X_vectorized, y)

    def _custom_tokenizer(self, text):
        en_stopwords = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()
        new_text = text.lower() #lowercase

        new_text = re.sub(r"([^\w\s])", "", new_text) #remove punctuation

        for word in new_text.split(): #remove stopwords
            if word in en_stopwords:
                new_text = new_text.replace(word, "")
        
        new_text = word_tokenize(new_text) #tokenize

        new_text = [lemmatizer.lemmatize(token) for token in new_text] #lemmatize
        return new_text
    
    def predict(self, text):
        vectorized_output = self.tdidf_vectorizer.transform([text])
        prediction = self.log_classifier.predict(vectorized_output)
        return prediction
    

# message = "I HAVE A DATE ON SUNDAY WITH WILL!!"
# spamModel = SpamClassifierModel()
# prediction = spamModel.predict(message)
# print(prediction)

        
        