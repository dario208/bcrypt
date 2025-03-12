import re
import json

# Chemin du fichier contenant les données SNMP
input_file = "snmp_data.txt"
output_file = "snmp_data.json"

# Dictionnaire pour stocker les données parsées
parsed_data = {}

# Lire le fichier ligne par ligne
with open(input_file, "r") as file:
    for line in file:
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            # Extraire l'OID et le nom de la MIB
            match = re.match(r"([A-Za-z0-9-]+)::([A-Za-z0-9-]+)\.(\d+)", key)
            if match:
                mib, oid, index = match.groups()
                if mib not in parsed_data:
                    parsed_data[mib] = {}
                parsed_data[mib][f"{oid}.{index}"] = value

# Écrire les données parsées dans un fichier JSON
with open(output_file, "w") as json_file:
    json.dump(parsed_data, json_file, indent=4)

print(f"Les données SNMP ont été converties en JSON et enregistrées dans {output_file}")