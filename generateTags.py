import spacy
from scipy.spatial.distance import cosine

# NOTE:tags shouldn't be one word unless it convey porper meaning
# Load the small English pipeline
nlp = spacy.load("en_core_web_lg")


def is_tag_worthy(word: str, threshold=0.5) -> bool:
    if word not in nlp.vocab and not nlp(word).has_vector:
        print(f"{word} is not a word or doesnt have vector")
        return False  # returning if no vector exists or if the word itself exists
    similarity_count = 0  # setting count to check how not generic a word is
    for Word in nlp.vocab.strings:
        if Word == word:
            continue  # skipping the word itself to optimize function from unwanted calles
        similarity = 1 - cosine(
            nlp.vocab[word].vector, nlp.vocab[Word].vector
        )  # checking genratily distance using cosine distance
        # to know how generic a word is
        if similarity > threshold:
            similarity_count += 1  # considering the word only if it has a similarity more than threshold (0.5)
    print(similarity_count)
    return (
        similarity_count > 150
    )  # choosing words only with higher similarity count, more higher more tag worthy


def generateTags(paragraph: str) -> list:
    doc = nlp(paragraph)
    # Iterate over the tokens
    tags = []
    for token in doc:
        print(f"{token.text} {token.pos_} {token.head.text}")
        if token.pos_ == "ADJ" and is_tag_worthy(token.text):
            tags.append(f"{token.text}")
        elif token.pos_ == "NOUN" and is_tag_worthy(token.text):
            tags.append(f"{token.text}")
    print(tags)
    return tags
