import spacy

# NOTE:tags shouldn't be one word unless it convey porper meaning
# Loading the large English pipeline
nlp = spacy.load("en_core_web_lg")


# used to change verbs to ing format following general language rules
def to_ing_form(lemma: str) -> str:
    if lemma.endswith("e") and not lemma.endswith("ee"):
        return lemma[:-1] + "ing"
    elif lemma.endswith("ie"):
        return lemma[:-2] + "ying"
    else:
        return lemma + "ing"


def generateTags(paragraph: str) -> list:
    doc = nlp(paragraph)
    # Iterate over the tokens
    tags = set()
    # adding to tag if the word represent any kind of person, organization or event
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "EVENT"]:
            tags.add(ent.text.strip().lower())
    for token in doc:
        # skipping iteration if the word is already in tags or as part of a tag
        if any(token.text in tag.split() for tag in tags):
            continue
        elif token.pos_ == "ADJ":
            # only adding head if it's an NOUN
            tags.add(
                f"{token.lemma_.lower()} {token.head.text.lower() if token.head.pos_ =='NOUN' else ''}"
            )
        elif token.pos_ == "NOUN" and token.head.pos_ == "VERB":
            # only adding head if it's a VERB and that too in ing format
            tags.add(f"{token.lemma_.lower()} {to_ing_form(token.head.lemma_)}")
    for chunk in doc.noun_chunks:
        # skipping iteration if the chunk noun or any part of the chunk noun exists in the tags or as part of any tag
        if any(word in tag.split() for tag in tags for word in chunk.text.split()):
            continue
        elif len(chunk.text.strip().lower()) > 1:
            # only adding to tag if the chunk noun is a multi word
            tags.add(chunk.text.strip().lower())
    final_list = []
    for tag in tags:
        doc_tag = nlp(tag)
        #removing any stop words or punctuations
        if any(not token.is_stop and not token.is_punct for token in doc_tag):
            print(tag)
            final_list.append(tag)
    return final_list
