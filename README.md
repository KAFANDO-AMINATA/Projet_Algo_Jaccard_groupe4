# Calculateur de similarite (Jaccard + WordNet)

## Description

Ce projet implémente un **calculateur de similarité sémantique entre deux phrases** en Python.  
Contrairement à la simple similarité de Jaccard qui ne compare que les mots exacts, cette version prend aussi en compte :

- Les **synonymes** (via [WordNet](https://wordnet.princeton.edu/))  
- Les **formes dérivées** (ex : *happy ↔ happiness*, *run ↔ runner*)  
- Les **répétitions de mots** (avec `Counter`)  
- Le **prétraitement linguistique** : stopwords, lemmatisation, ponctuation, casse 

Important : La lemmatisation ne prend en compte que les mots de la même catégorie grammaticale. Par exemple, running (verbe) et runner (nom) auront des lemmes différents. Pour capturer ces relations, le projet utilise aussi les formes dérivées et synonymes via WordNet.

Ce projet est un point de départ pour explorer la **similarité lexicale et sémantique** dans le traitement automatique du langage (NLP).

---

## Technologies utilisées

- **Python 3.10+ – langage principal** des phrases (minuscule, ponctuation, stopwords, lemmatisation)
- **NLTK** pour le prétraitement textuel, stopwords et WordNet
- **WordNet** base de données lexicale pour synonymes et relations dérivées
- **Counter (collections)**pour gérer les répétitions de mots
- **Jupyter Notebook** pour le développement interactif

---

---

## Fonctionnalités principales

- **Nettoyage et prétraitement** des phrases (minuscule, ponctuation, stopwords, lemmatisation)
- **Détection de synonymes et formes dérivées**
- **Calcul de la similarité Jaccard**
- **Interface console simple et interactive**

---

## Architecture du projet

```
projet_jaccard_groupe4/
│
├── jaccard.ipynb        # Contient toutes les fonctions principales (prétraitement, calcul, etc.)
└── README.md            # Ce fichier de documentation
```

---

## Installation

### Cloner le dépôt
```bash
git clone https://github.com/<ton-nom-utilisateur>/sentence_similarity.git
cd sentence_similarity
```


##  Fonctionnement interne

Le programme procède en plusieurs étapes :

1. **Prétraitement linguistique** :
   - Minuscule, suppression de ponctuation, stopwords et lemmatisation.

2. **Extraction des formes dérivées** :
   - Ex. : `get_related_forms("happy") → {"happy", "happiness"}`

3. **Détection de relations sémantiques** :
   - `are_related("happy", "happiness") → True`

4. **Calcul de la similarité Jaccard** :
   \[
   \text{Jaccard}(A,B) = \frac{|A \cap B|}{|A \cup B|}
   \]
   en tenant compte des synonymes et dérivations.

---


---

## Concepts NLP abordés

- Similarité lexicale (Jaccard)
- Lemmatisation
- Synonymie et dérivation morphologique
- Prétraitement textuel
- WordNet et relations sémantiques

---



## Auteur

**Groupe 4**
- KAFANDO aminata
- SAWADOGO Hamidou
- COMPAORE Abdoul Bassy Omar