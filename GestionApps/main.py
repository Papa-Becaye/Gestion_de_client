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
    class Client:
        nombre_client = 0
        def __init__(self):
            Client.nombre_client = Client.nombre_client + 1
        def infos_client(self):
            self.nom = input("veuillez entrer le nom du client :")
            self.prenom = input("veuillez entrer le prenom du client :")
            self.telephone = input("veuillez entrer le numéro du client :")
            self.dateDeNaissance = []
    Client_1 = Client()
    Client_1.infos_client()
    def change_id(chemin,identifiant):
        for i in root.findall("{}".format(chemin)):
            current_id = i.attrib['{}'.format(identifiant)]
            new_id = ('wikipedia_yosakoi-{}'.format(current_id))
            i.attrib['{}'.format(identifiant)] = new_id
    change_id("buyer","number")
    def change_Element(chemin):
        for element in root.findall("{}".format(chemin)):
            rescent_element = element.text
            if element == name:
                new_element = Client_1.nom
            elif element == surname:
                new_element = Client_1.prenom
            elif element == call_number :
                new_element = Client_1.telephone
            element.text = new_element
    change_Element("./buyer/nom")
    change_Element("./buyer/prenom")
    change_Element("./buyer/telephone")
    xml_output = ET.tostring(root, encoding="unicode", method="xml")
    with open('Gestclient/tempclient.xml', 'w') as sys.stdout:
       print(xml_output)