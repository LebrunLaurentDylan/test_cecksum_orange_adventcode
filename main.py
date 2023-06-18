import json
from collections import Counter

# importer le fichier json contenant les ID des boites
input_boxes = open("input_boxes.json")
data = json.load(input_boxes)


def input_list_transformer(data):
    df_id_boxes = []
    for i in data:
        i_list = list(i)
        df_id_boxes.append(i_list)
    return df_id_boxes


def occurrences_counter(dataset):
    # compteur des boxes contenant deux et trois occurrences
    three_count = 0
    two_count = 0
    # la fonction "Counter()" me permet d'avoir toutes les occurrences de chaque lettre
    # si jamais les deux types d'occurrences sont présents dans la même boxe id alors
    # elles incrémentent les deux compteurs
    for boxes in dataset:
        counts = Counter(boxes)
        # j'utilise "counts" pour incrémenter les variables de 1 si 2 occurrences présentes
        if 2 in counts.values():
            two_count += 1
        # j'utilise "counts" pour incrémenter les variables de 1 si 3 occurrences présentes
        if 3 in counts.values():
            three_count += 1
    # je retourne le résultat (la checksum)
    return three_count * two_count


def difference_de_un(str1, str2):
    result = ""
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if result != "":
                return ""
            result = str1[:i] + str1[i+1:]
    return result


def assembleur(dataset):
    for boxes in dataset:
        for boxes2 in dataset:
            if boxes2 == boxes:
               continue
            result = difference_de_un(boxes, boxes2)
            if result != "":
                return result
    return ""


# charger les données du json dans une liste
df_boxes = input_list_transformer(data)
reste_lettres = assembleur(data)
print("checksum :", occurrences_counter(df_boxes))
print(reste_lettres)

