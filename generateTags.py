import spacy

# NOTE:tags shouldn't be one word unless it convey porper meaning
# Loading the large English pipeline
nlp = spacy.load("en_core_web_lg")


def generateTags(paragraph: str) -> list:
    doc = nlp(paragraph)
    # Iterate over the tokens
    tags = set()
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "EVENT"]:
            tags.add(ent.text.strip().lower())
    for token in doc:
        if any(token.text in tag.split() for tag in tags):
            continue
        elif token.pos_ == "ADJ":
            tags.add(
                f"{token.lemma_.lower()} {token.head.text.lower() if token.head.pos_ =='NOUN' else ''}"
            )
        elif token.pos_ == "NOUN" and token.head.pos_ == "VERB":
            tags.add(f"{token.lemma_.lower()} {token.head.text}")
    for chunk in doc.noun_chunks:
        if any(word in tag.split() for tag in tags for word in chunk.text.split()):
            continue
        elif len(chunk.text.strip().lower()) > 1:
            tags.add(chunk.text.strip().lower())
    return list(tags)
