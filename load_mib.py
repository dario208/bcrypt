import json
import re

def parse_mib_file(mib_file):
    mib_data = {}
    current_object = None

    with open(mib_file, 'r') as file:
        for line in file:
            line = line.strip()
            # Vérifie si la ligne commence par OBJECT-TYPE
            if line.startswith('OBJECT-TYPE'):
                # Commence une nouvelle définition d'objet
                object_name = re.search(r'(\w+)\s+OBJECT-TYPE', line)
                if object_name:
                    current_object = object_name.group(1)
                    mib_data[current_object] = {}
            elif current_object:
                # Récupère les informations de l'objet
                if line.startswith('SYNTAX'):
                    syntax = re.search(r'SYNTAX\s+(.+)', line)
                    if syntax:
                        mib_data[current_object]['SYNTAX'] = syntax.group(1).strip()
                elif line.startswith('MAX-ACCESS'):
                    max_access = re.search(r'MAX-ACCESS\s+(.+)', line)
                    if max_access:
                        mib_data[current_object]['MAX-ACCESS'] = max_access.group(1).strip()
                elif line.startswith('STATUS'):
                    status = re.search(r'STATUS\s+(.+)', line)
                    if status:
                        mib_data[current_object]['STATUS'] = status.group(1).strip()
                elif line.startswith('DESCRIPTION'):
                    description = re.search(r'DESCRIPTION\s+"(.+?)"', line)
                    if description:
                        mib_data[current_object]['DESCRIPTION'] = description.group(1).strip()
                elif '::=' in line:
                    oid = line.split('::=')[1].strip()
                    mib_data[current_object]['OID'] = oid

    return mib_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    mib_file_path = 'cfgmib.mib'  # Chemin vers votre fichier MIB
    output_json_path = 'mib_data.json'  # Chemin vers le fichier JSON de sortie

    mib_data = parse_mib_file(mib_file_path)
    save_to_json(mib_data, output_json_path)

    print(f"Les données MIB ont été converties en JSON et enregistrées dans {output_json_path}.")