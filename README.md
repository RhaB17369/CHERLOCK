# Spynet

https://www.google.com/imgres?q=espionage&imgurl=https%3A%2F%2Fpbs.twimg.com%2Fprofile_images%2F1110008469841686534%2FzLyyxGjW_400x400.jpg&imgrefurl=https%3A%2F%2Ftwitter.com%2Fespionageulti&docid=X_0UOiN_gELp-M&tbnid=6pSyTZJ3N_X8WM&vet=12ahUKEwiE2af5g7OJAxWjppUCHYGNNy0QM3oECGMQAA..i&w=267&h=267&hcb=2&ved=2ahUKEwiE2af5g7OJAxWjppUCHYGNNy0QM3oECGMQAA

**Spynet** est un outil avancé de détection et d'analyse des vulnérabilités conçu pour fournir une évaluation exhaustive et proactive des failles de sécurité au sein des systèmes d'information. Il se concentre sur la reconnaissance et la collecte d'informations en mettant l'accent sur la simplicité et la performance.

## Caractéristiques

### Détails DNS
- **Cartographie DNS** : Visualisation DNS via des techniques avancées, y compris la benne DNS.
- **Informations WHOIS** : Récupération complète des données WHOIS pour les domaines.

### Sécurité TLS
- **Chiffrements supportés** : Identification des algorithmes de chiffrement pris en charge.
- **Versions TLS** : Détection des versions de TLS actives.
- **Détails de certificat et SAN** : Extraction des informations de certificat, y compris les noms alternatifs de sujet (SAN).

### Analyse des Ports
- **Scans de Port** : Évaluation des ports ouverts pour détection de services actifs.
- **Scan de Services et Scripts** : Utilisation de scripts spécifiques pour obtenir des informations détaillées sur les services en ligne.

### Fuzzing et Énumération
- **Fuzzing d'URL et Détection de fichiers/dir** : Recherche de fichiers et répertoires cachés ou sensibles.
- **Énumération de sous-domaines** : Inclut Google Dorking, DNS, découverte SAN et bruteforce.

### Analyse d'Applications Web
- **Détection CMS** : Identification des Content Management Systems utilisés.
- **Serveur Web et X-Powered-By** : Découverte des technologies de serveur.
- **Extraction robots.txt et sitemap** : Accès aux fichiers robots.txt et sitemaps.
- **Inspection des cookies** : Détection et analyse des cookies.
- **Extraction d'URL fuzzables et formulaires HTML** : Identification des points d'interaction.
- **Récupération d'adresses Email** : Analyse et récupération d'adresses email publiques.
- **Analyse de Stockage** : Recherche de seaux S3 vulnérables et énumération des fichiers sensibles.
- **Détection WAF** : Identification de pare-feu applicatifs connus.

### Performance et Anonymat
- **Routage via Tor/Proxy** : Prend en charge l'anonymisation des requêtes.
- **Support asyncio** : Exécution asynchrone des scans pour une performance optimale.
- **Logging avancé** : Sauvegarde des sorties en fichiers, par cibles et modules.

---

## Feuille de route
- Développer et tester davantage d’attaques et analyses d'applications Web (branche *OWASP*, #28).
- Prise en charge de plus de fournisseurs pour l’analyse des stocks vulnérables (#27).
- Amélioration de la détection WAF avec ajout de nouveaux WAF supportés.
- Prise en charge multi-hôtes et IP ranges (notation CIDR).
- Ajout de formats de sortie supplémentaires (JSON, CSV).
- Optimisation des limites de taux pour contourner les restrictions.

---

## Installation

### Depuis PyPI
Pour la dernière version stable, installez Spynet via pip :

```bash
pip install spynet-scanner
