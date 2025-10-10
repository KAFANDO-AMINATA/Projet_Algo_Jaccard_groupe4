import string

def jaccard_similarity_sentences(sentence1, sentence2):
    """
    Calcule la similarité de Jaccard entre deux phrases.
    Gère les cas particuliers : None, chaînes vides, ponctuation.
    """
    try:
        # Vérification des entrées
        if not sentence1 or not sentence2:
            return 0.0

        # Mise en minuscules
        sentence1 = sentence1.lower()
        sentence2 = sentence2.lower()

        # Suppression de la ponctuation
        translator = str.maketrans("", "", string.punctuation)
        sentence1 = sentence1.translate(translator)
        sentence2 = sentence2.translate(translator)

        # Découpage en ensembles de mots
        set1 = set(sentence1.split())
        set2 = set(sentence2.split())

        if not set1 and not set2:
            return 0.0  # Les deux phrases sont vides ou sans mots valides

        # Intersection et union
        intersection = set1.intersection(set2)
        union = set1.union(set2)

        # Calcul Jaccard
        similarity = len(intersection) / len(union) if union else 0.0
        return similarity

    except Exception as e:
        print(f"Erreur lors du calcul : {e}")
        return 0.0


# Tests
s1 = "je mange une banane"
s2 = "je mange une mangue"
s3 = "il conduit une voiture"
s4 = ""  # phrase vide
s5 = None  # entrée None
s6 = "je, mange; une: banane!"  # avec ponctuation

print("J(s1, s2) =", jaccard_similarity_sentences(s1, s2))  # attendu ≈ 0.6
print("J(s1, s3) =", jaccard_similarity_sentences(s1, s3))  # attendu ≈ 0.1667
print("J(s1, s4) =", jaccard_similarity_sentences(s1, s4))  # attendu 0.0
print("J(s1, s5) =", jaccard_similarity_sentences(s1, s5))  # attendu 0.0
print("J(s1, s6) =", jaccard_similarity_sentences(s1, s6))  # doit gérer la ponctuation
