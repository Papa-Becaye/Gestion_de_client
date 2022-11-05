#coding: utf-8
import xml.etree.ElementTree as ET
from lxml import etree
import sys

# tree = etree.parse("Gestclient/client.xml")
# for client in tree.xpath("/client/buyer/nom"):
#     client.text = input("veuillez entrer le nom du client :")
# for buyer in tree.xpath("buyer/nom"):
#     buyer.text = input("veuillez entrer le nom du client :")
# nom = etree.SubElement(buyer, "nomclient")
# nom.text = input("veuillez enter le nom de l'autre client :")
# print(etree.tostring(client, pretty_print=True))

with open("Gestclient/client.xml", encoding="utf-8") as corpus:
    tree = ET.parse(corpus)
    root = tree.getroot()
    name = root.find("./buyer/nom")
    surname = root.find("./buyer/prenom")
    call_number = root.find("./buyer/telephone")
    adresse = root.find("./buyer/adresse")
    day_birthday = root.find("./buyer/date_lieunaissance/jour")
    month_birthday = root.find("./buyer/date_lieunaissance/mois")
    year_birthday = root.find("./buyer/date_lieunaissance/annee")
    adresse = root.find("./buyer/adresse")
    class Client:
        nombre_client = 0
        def __init__(self):
            Client.nombre_client = Client.nombre_client + 1
        def infos_client(self):
            self.nom = input("veuillez entrer le nom du client :")
            self.prenom = input("veuillez entrer le prenom du client :")
            self.telephone = input("veuillez entrer le numéro du client :")
            self.dateDeNaissance = []
            self.adresse = input("veuillez entrer l'adresse du client :")
            for i in range(0,3):
                if i == 0:
                    day = input("veuillez entrer le jour de naissance du client :")
                    self.dateDeNaissance.append(day)
                elif i == 1 :
                    month = input("veuillez entrer le mois de naissance du client :")
                    self.dateDeNaissance.append(month)
                else :
                    year = input("veuillez entrer l'année de naissance du client :")
                    self.dateDeNaissance.append(year)
        def change_Element(self,chemin):
            for element in root.findall("{}".format(chemin)):
                rescent_element = element.text
                if element == name:
                        new_element = self.nom
                elif element == surname:
                        new_element = self.prenom
                elif element == call_number :
                        new_element = self.telephone
                elif element == day_birthday :
                        new_element = self.dateDeNaissance[0]
                elif element == month_birthday :
                        new_element = self.dateDeNaissance[1]
                elif element == year_birthday :
                        new_element = self.dateDeNaissance[2]
                elif element == adresse :
                        new_element = self.adresse
                element.text = new_element
    
    def change_id(chemin,identifiant):
        for i in root.findall("{}".format(chemin)):
            current_id = i.attrib['{}'.format(identifiant)]
            new_id = ('wikipedia_yosakoi-{}'.format(current_id))
            i.attrib['{}'.format(identifiant)] = new_id
    change_id("buyer","number")
    List_Client = []
    record = True
    compteur = 0
    while record == True:
        personne = Client()
        List_Client.append(personne)
        List_Client[compteur].infos_client()
        List_Client[compteur].change_Element("./buyer/nom")
        List_Client[compteur].change_Element("./buyer/prenom")
        List_Client[compteur].change_Element("./buyer/telephone")
        List_Client[compteur].change_Element("./buyer/date_lieunaissance/jour")
        List_Client[compteur].change_Element("./buyer/date_lieunaissance/mois")
        List_Client[compteur].change_Element("./buyer/date_lieunaissance/annee")
        List_Client[compteur].change_Element("./buyer/adresse")
        print("voudriez vous quitter ?")
        quitter = input("Cliquer \"Oui\" ou \"Non\" :")
        if quitter == "Oui":
            record = False
        elif quitter == "Non" :
            record = True
            compteur = compteur + 1
            xml_output = ET.tostring(root, encoding="unicode", method="xml")
            with open('Gestclient/tempclient.xml','a') as sys.stdout:
                print(xml_output)
    xml_output = ET.tostring(root, encoding="unicode", method="xml")
    with open('Gestclient/tempclient.xml','a') as sys.stdout:
        print(xml_output)