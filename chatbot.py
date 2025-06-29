faqs = {
    "what is your return policy": "You can return any item within 30 days.",
    "how can i track my order": "You can track your order using the link in your email.",
    "what payment methods do you accept": "We accept credit cards and PayPal.",
}
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')

faqs = {
    "what is your return policy": "You can return any item within 30 days.",
    "how can i track my order": "You can track your order using the link in your email.",
    "what payment methods do you accept": "We accept credit cards and PayPal.",
}

def get_best_match(user_input):
    questions = list(faqs.keys())
    questions.append(user_input)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer().fit_transform(questions)
    similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    match_index = similarity.argmax()

    return faqs[questions[match_index]]

# Chat loop
print("Chatbot: Ask me anything (type 'exit' to quit)")
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        break
    response = get_best_match(user_input)
    print("Chatbot:", response)
