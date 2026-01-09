import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re


class SpamClassifierModel:
    """
    A class to generate instance of Spam Classifier ML Model
    """
    def __init__(self):
        """
        constructor for SpamClassifierModel
        
        :param self: SpamClassifierModel - The SpamClassifierModel object
        """

        # Read data in and split it
        data = pd.read_csv("./Desktop/Data/sms_spam_collection.csv")
        X = data['message']
        y = data["target"]

        # Create text vectorizer
        self.tdidf_vectorizer = TfidfVectorizer(tokenizer=self._custom_tokenizer, token_pattern=None)
        X_vectorized = self.tdidf_vectorizer.fit_transform(X)

        #Create classifier model
        self.log_classifier = LogisticRegression(C=1).fit(X_vectorized, y)

    def _custom_tokenizer(self, text):
        """
        A method to process text into vectors to be used
        as input to spam classifier ml model
        
        :param self: SpamClassifierModel - The SpamClassifierModel object
        :param text: String - spam message string

        :return an array of words
        """

        # Get stopwords function and Word Lemmatizer
        en_stopwords = stopwords.words('english')
        lemmatizer = WordNetLemmatizer()

        # Process text
        new_text = text.lower() #lowercase
        new_text = re.sub(r"([^\w\s])", "", new_text) #remove punctuation
        new_text = word_tokenize(new_text) #tokenize
        for word in new_text: #remove stopwords
            if word in en_stopwords:
                new_text.remove(word)
        new_text = [lemmatizer.lemmatize(token) for token in new_text] #lemmatize

        return new_text
    
    def predict(self, text):
        """
        A method that calls the classifier's predict method to
        find prediction of whether a message is spam or ham
        
        :param self: SpamClassifierModel - The SpamClassifierModel object
        :param text: String - spam message string from user

        :return the prediction as a String
        """
        
        #Transform text
        vectorized_output = self.tdidf_vectorizer.transform([text])

        #Get prediction
        prediction = self.log_classifier.predict(vectorized_output)
        prediction = prediction[0]

        return prediction
    

# message = "Did you catch the bus ? Are you frying an egg ? Did you make a tea? Are you eating your mom's left over dinner ? Do you feel my Love ?"
# spamModel = SpamClassifierModel()
# text_vector = spamModel._custom_tokenizer(message)
# print(text_vector)
# prediction = spamModel.predict(message)
# print(prediction)


        