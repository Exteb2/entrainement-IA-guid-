# Rapport d'atelier — Coder avec l'IA (BUT 3 Informatique)

- **Étudiant :** Extebe Ernaga
- **Groupe :** BUT3-Parcours-RACDV-Initiale
- **Dépôt Git :** [À compléter : URL ou nom de l'archive remise]

---

## Section 1 — Panorama du marché, benchmark et sélection d'outillage

### 1.1. Protocole d'évaluation expérimentale
- **Langage et framework de test utilisés :** [ Python 3.12 + pytest ]
- **Outil A évalué :** [Antigravity, modèle exact utilisé, modalité d'accès gratuite/étudiante/abonnement]
- **Outil B évalué :** [Gemini, modèle exact utilisé, modalité d'accès gratuite/étudiante/abonnement]

### 1.2. Tableau comparatif multicritères sur l'exercice étalon (Validation IBAN)

| Critère d'évaluation | Outil A ([Antigravity + Modèle]) | Outil B ([Gemini + 3.1pro]) |
| :--- | :--- | :--- |
| **1. Famille d'outil & intégration IDE** | [Editeur de code natif] | [App web] |
| **2. Injection du contexte projet** | [IDE dans le projet contexte direct] | [copié collé le ] |
| **3. Niveau d'action & contrôle du diff** | [diff visuel modification automatique avec demande de validation] | [copié collé] |
| **4. Résultat au 1er essai (IBAN mod 97)** | [test passe avec entier python] | [test passe avec entier python] |
| **5. Coût, limites de quotas & latence** | [pas de plafond pour cette exercice vitesse moyenne] | [pas de plafond constaté vitesse rapide] |
| **6. Confidentialité (Opt-out entraînement)** | [Réglage trouvé dans les paramètres] | [aucune idée] |
| **7. Confort de contrôle humain & limites** | [execution directement dans le code assez confortable mais interface sovuent trop surchargé nécessite peut etre 2 écran] | [assez facile d'utilisation demande de changer de fenetre et de copier collé] |

### 1.3. Sélection motivée pour le projet fil rouge et solution de repli
- **Outil principal retenu et arguments techniques :** [Antigravity est un editeur natif qui a la mais sur le projet entier il est presque conçu pour du multi fichier
- **Outil de secours prévu en cas d'atteinte du quota :** [gemini/chatgpt/claude]

---

## Section 2 — Spécification assistée et planification (SplitIUT v1)

### 2.1. Arbitrage des ambiguïtés métier et cas limites

| Cas limite ou zone floue | Risque identifié en cas d'oubli | Règle précise fixée dans `SPEC.md` |
| :--- | :--- | :--- |
| **1. Représentation de l'argent** | [À compléter] | [À compléter] |
| **2. Distribution des centimes restants** | [À compléter] | [À compléter] |
| **3. Payeur, bénéficiaires et poids** | [À compléter] | [À compléter] |
| **4. Doublons et intégrité JSON** | [À compléter] | [À compléter] |

### 2.2. Architecture modulaire et directives imposées à l'IA (`AGENTS.md`)
- **Justification du découpage en couches (`domain` / `storage` / `cli` ou `api`) :** [Expliquer en 5-6 lignes]
- **Règles principales définies dans `AGENTS.md` :**
```markdown
[Copier ici les règles essentielles de votre fichier AGENTS.md]
```

### 2.3. Plan d'implémentation incrémental (`PLAN.md`)
- **Commit Git initial de spécification :** `[Indiquer le hash court du commit]`

| Incrément | Périmètre fonctionnel codé | Fichiers cibles | Critère de vérification |
| :--- | :--- | :--- | :--- |
| **Inc. 1** | [À compléter] | [À compléter] | [À compléter] |
| **Inc. 2** | [À compléter] | [À compléter] | [À compléter] |
| **Inc. 3** | [À compléter] | [À compléter] | [À compléter] |
| **Inc. 4** | [À compléter] | [À compléter] | [À compléter] |
| **Inc. 5** | [À compléter] | [À compléter] | [À compléter] |
| **Inc. 6** | [À compléter] | [À compléter] | [À compléter] |

---

## Section 3 — Implémentation incrémentale sous contrôle (SplitIUT v1)

### 3.1. Journal de traçabilité des incréments et interventions humaines

| Incrément | Fonctionnalité implémentée | Hash commit Git | Intervention humaine (Accepté / Ajusté / Réécrit & justification) |
| :--- | :--- | :--- | :--- |
| **Inc. 1** | [À compléter] | `[hash]` | [À compléter] |
| **Inc. 2** | [À compléter] | `[hash]` | [À compléter] |
| **Inc. 3** | [À compléter] | `[hash]` | [À compléter] |
| **Inc. 4** | [À compléter] | `[hash]` | [À compléter] |
| **Inc. 5** | [À compléter] | `[hash]` | [À compléter] |

### 3.2. Analyse d'un guidage efficace dès le premier essai
- **Prompt utilisé :**
```text
[Coller ici le prompt exact]
```
- **Analyse technique du succès :** [Expliquer en 5-6 lignes quels éléments de SPEC.md / AGENTS.md ont permis d'obtenir un code juste et propre immédiatement]

### 3.3. Preuve de contrôle : recadrage ou correction d'une proposition de l'IA (Avant / Après)
- **Défaut, fragilité ou sur-ingénierie repéré dans la proposition initiale :** [Expliquer le problème détecté à la relecture]
- **Code initial proposé par l'IA (Avant) :**
```text
[Coller les 8-15 lignes initiales problématiques]
```
- **Code final retenu après correction ou recadrage (Après) :**
```text
[Coller la version corrigée]
```

---

## Section 4 — Génération des tests et contrôle de la justesse

### 4.1. Démarche mise en œuvre pour éviter les tests tautologiques
[Expliquer en 6-10 lignes pourquoi générer des tests depuis le code existant est risqué, et comment vous avez construit/vérifié vos oracles depuis `SPEC.md`]

### 4.2. Matrice de vérification des cas limites et invariants

| Scénario testé | Entrée soumise | Oracle attendu | Résultat initial sur le code v1 & correctif éventuel |
| :--- | :--- | :--- | :--- |
| **1. Division non exacte** | `10,00 €` / 3 parts égales | `3,34 € ; 3,33 € ; 3,33 €` | [À compléter] |
| **2. Centime unique** | `0,01 €` / 3 parts égales | `0,01 € ; 0,00 € ; 0,00 €` | [À compléter] |
| **3. Payeur hors bénéficiaires** | Alice paie `30,00 €` pour Bob, Chloé | A:`+30€`, B:`-15€`, C:`-15€` | [À compléter] |
| **4. Dettes circulaires** | A->B `20€`, B->C `20€`, C->A `20€` | Soldes nuls, `0` virement | [À compléter] |
| **5. Poids asymétriques** | `10,00 €` poids `[2, 1]` | `6,67 €` et `3,33 €` | [À compléter] |
| **6. Invariants (50 tirages aléatoires)** | 50 groupes/dépenses aléatoires | `somme(soldes) == 0` et extinction des dettes | [À compléter] |

### 4.3. Conclusions de l'audit de justesse (Algorithme, robustesse et sécurité)
- **Analyse de l'optimalité de l'algorithme de remboursement (test sur `[+15, +9, +5, -14, -8, -7]`) :** [Indiquer le résultat observé et analyser la justesse des commentaires générés par l'IA]
- **Revue de robustesse et de sécurité (entrées invalides, JSON corrompu, lisibilité) :** [À compléter]

---

## Section 5 — Maintenance évolutive sans régression (SplitIUT v2)

### 5.1. Matrice d'analyse d'impact (passage de la v1 à la v2)

| Partie du code v1 | Modifications apportées pour SF6 (Devises) et SF7 (Remboursements) | Technique utilisée pour éviter toute régression |
| :--- | :--- | :--- |
| **1. Modèle de données** | [À compléter] | [À compléter] |
| **2. Calcul des parts & arrondis** | [À compléter] | [À compléter] |
| **3. Soldes nets & virements** | [À compléter] | [À compléter] |
| **4. Chargement JSON (fichiers v1)** | [À compléter] | [À compléter] |

### 5.2. Retour critique sur le refactoring assisté par IA
- **Apport de l'architecture initiale (Module 2) lors de la modification :** [À rédiger]
- **Difficultés ou régressions observées lors de la modification de l'existant par l'IA :** [À rédiger]

---

## Section 6 — Synthèse réflexive d'ingénieur

### 6.1. Bilan factuel Gains de productivité / Coûts de contrôle

| Étape de l'atelier | Où l'IA m'a fait gagner le plus de temps | Où l'IA a demandé le plus de vigilance ou fait perdre du temps |
| :--- | :--- | :--- |
| **1. Spécification & plan (Module 2)** | [À compléter] | [À compléter] |
| **2. Implémentation v1 (Module 3)** | [À compléter] | [À compléter] |
| **3. Tests & audit (Module 4)** | [À compléter] | [À compléter] |
| **4. Évolution v2 (Module 5)** | [À compléter] | [À compléter] |

### 6.2. Mes 3 règles personnelles pour l'entreprise (Stage / Alternance)
1. **[Règle n°1] :** [Expliquer concrètement]
2. **[Règle n°2] :** [Expliquer concrètement]
3. **[Règle n°3] :** [Expliquer concrètement]

---
