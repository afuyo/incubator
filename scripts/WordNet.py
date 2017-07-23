from nltk.corpus import wordnet as wn

def main():

    synsetWord = input('Provide a word to receive its list of synonyms:')
    synsetsAll = wn.synsets(synsetWord)

    for i in range(len(synsetsAll)):
        print('Lemma names: ', synsetsAll[i].lemma_names())
        print('Definition:', synsetsAll[i].definition())
        if synsetsAll[i].examples() != []: print('Examples:', synsetsAll[i].examples())
        print('Lemmas:', synsetsAll[i].lemmas())
        #Hyponyms:
        types_of = synsetsAll[i].hyponyms()
        print('Types of/Hyponyms: ', sorted(lemma.name() for synset in types_of for lemma in synset.lemmas()))
        #Hypernyms:
        if synsetsAll[i].hypernyms() != []: print('Hypernyms:', synsetsAll[i].hypernyms())
        word_paths = synsetsAll[i].hypernym_paths()
        print('Path to root:', [synset.name() for synset in word_paths[0]])
        # Meronyms
        if synsetsAll[i].part_meronyms() != []: print('Components Meronyms:', synsetsAll[i].part_meronyms())
        if synsetsAll[i].substance_meronyms() != []: print('Substance Meronyms:', synsetsAll[i].substance_meronyms())
        if synsetsAll[i].member_meronyms() != []: print('Collections of Meronyms:', synsetsAll[i].member_meronyms())
        #Holonyms
        if synsetsAll[i].part_holonyms() != []: print('Components Holonyms:', synsetsAll[i].part_holonyms())
        if synsetsAll[i].substance_holonyms() != []: print('Substance Holonyms:', synsetsAll[i].substance_holonyms())
        if synsetsAll[i].member_holonyms() != []: print('Collections of Holonyms:', synsetsAll[i].member_holonyms())

if __name__ == '__main__':
        main()