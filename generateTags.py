import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")


# tags shouldn't be one word unless it convey porper meaning
def generateTags(paragraph: str) -> list:
    doc = nlp(paragraph)
    # Iterate over the tokens
    tags = []
    for token in doc:
        print(f"{token.text} {token.pos_} {token.head.text}")
        if token.pos_ == "ADJ":
            tags.append(f"{token.text} {token.head.text}")
        elif token.pos_ == "NOUN":
            tags.append(f"{token.text} {token.head.text}")
    print(tags)
    return tags
