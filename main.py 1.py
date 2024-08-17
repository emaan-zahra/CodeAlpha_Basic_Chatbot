import nltk
nltk.download('punkt')  # For sentence tokenization
nltk.download('wordnet')  # For word sense disambiguation
nltk.download('averaged_perceptron_tagger')  # For POS tagging
import nltk
from nltk.stem import WordNetLemmatizer
import random

# Create a dictionary of possible responses 
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!"],
    "goodbye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "default": ["I'm not sure I understand.", "Can you rephrase that?", "Tell me more!"],
  "name": ["My name is Chatbot.", "I'm Chatbot, nice to meet you!"],
"my name is": ["Nice to meet you, Emaan!"]
}

# Define a function to process user input
def chat(user_input):
    # Tokenize the input into words
    tokens = nltk.word_tokenize(user_input)

    # Lemmatize the words (reduce to base form)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]

    # Check for specific keywords
    if any(word in lemmas for word in ["hello", "hi", "greetings"]):
        return random.choice(responses["greeting"])
    elif any(word in lemmas for word in ["goodbye", "see", "later"]):
        return random.choice(responses["goodbye"])
    elif any(word in lemmas for word in ["thank", "thanks"]):
        return random.choice(responses["thanks"])
    elif any(word in lemmas for word in ["name", "who", "what"]):
      return random.choice(responses["name"])
    elif any(word in lemmas for word in ["my name", "my name is"]):
      return random.choice(responses["my name is"])
    else:
        return random.choice(responses["default"])

# Start the chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print("Chatbot: ", response)