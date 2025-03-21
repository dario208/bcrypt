
# Documentation sur le fichier MIB `cfgmib.mib`

Le fichier MIB `cfgmib.mib` contient de nombreuses définitions d'objets qui peuvent être utilisés pour surveiller et gérer le matériel. Voici un aperçu de certains OIDs (Object Identifiers) extraits de votre fichier, ainsi que leur utilisation et les données qu'ils retournent.

## Exemples d'OIDs et leur Utilisation

1. **vMainsLoadCharacterL1**

   - **OID** : `{ groupRdCfg 8818 }`
   - **Utilisation** : Caractéristique de charge du réseau pour la phase L1.
   - **Données retournées** : Une chaîne de caractères (DisplayString).
2. **vMainsLoadCharacterL2**

   - **OID** : `{ groupRdCfg 8819 }`
   - **Utilisation** : Caractéristique de charge du réseau pour la phase L2.
   - **Données retournées** : Une chaîne de caractères (DisplayString).
3. **vMainsLoadCharacterL3**

   - **OID** : `{ groupRdCfg 8820 }`
   - **Utilisation** : Caractéristique de charge du réseau pour la phase L3.
   - **Données retournées** : Une chaîne de caractères (DisplayString).
4. **vFrequencyRegulatorOutput**

   - **OID** : `{ groupRdCfg 9052 }`
   - **Utilisation** : Mesure de la sortie du régulateur de fréquence.
   - **Données retournées** : Un entier de type `Integer32` représentant la valeur en volts (V).
5. **vVoltageRegulatorOutput**

   - **OID** : `{ groupRdCfg 9053 }`
   - **Utilisation** : Mesure de la sortie du régulateur de tension.
   - **Données retournées** : Un entier de type `Integer32` représentant la valeur en volts (V).
6. **vCUAIN01**

   - **OID** : `{ groupRdCfg 9151 }`
   - **Utilisation** : Mesure du courant pour l'entrée 01.
   - **Données retournées** : Un entier de type `Integer32` représentant le courant en ampères (A).
7. **vCUAIN02**

   - **OID** : `{ groupRdCfg 9152 }`
   - **Utilisation** : Mesure du courant pour l'entrée 02.
   - **Données retournées** : Un entier de type `Integer32` représentant le courant en ampères (A).
8. **vCUTemperature**

   - **OID** : `{ groupRdCfg 10124 }`
   - **Utilisation** : Mesure de la température.
   - **Données retournées** : Un entier de type `Integer32` représentant la température en degrés Celsius (°C).
9. **vMainsKWh**

   - **OID** : `{ groupRdCfg 11025 }`
   - **Utilisation** : Mesure de l'énergie active consommée ou produite par le système.
   - **Données retournées** : Un entier de type `Integer32` représentant l'énergie en kilowattheures (kWh).
10. **vNumEStops**

    - **OID** : `{ groupRdCfg 11195 }`
    - **Utilisation** : Compte le nombre d'arrêts d'urgence.
    - **Données retournées** : Un entier de type `Gauge32`.

## Utilisation pour le Monitoring

Pour surveiller le matériel à l'aide de ces OIDs, vous pouvez utiliser un outil de gestion SNMP (comme `snmpget` ou `snmpwalk`) pour interroger les appareils. Voici un exemple de commande pour obtenir la valeur d'un OID :
