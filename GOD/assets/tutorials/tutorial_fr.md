# 🎓 Tutoriel – GOD (God Offers Downloads)

## 🚀 Présentation
Bienvenue dans le tutoriel d'utilisation de l'application ! Cette application permet de télécharger des vidéos et playlists YouTube en vidéo ou en audio, avec prise en charge des playlists privées.

L'application propose deux modes principaux :

- 📥 **Téléchargement simple** : pour gérer des vidéos une par une (ou des playlists)
- 📋 **Téléchargement par lot (Batch)** : pour télécharger plusieurs URLs en une seule fois

------

## 📥 Téléchargement simple

1. **Copiez l'URL** de la vidéo YouTube 🔗

2. **Collez-la** dans le champ d'URL

3. **Cliquez** sur le bouton "➕ Vérifier"

4. **Attendez** que les informations de la vidéo se chargent (miniature, durée, taille)

   **Sélectionnez** vos options :

   - 🎥 **Vidéo** : choisissez la résolution (Best, 2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, 144p)
   - 🎵 **Audio seul** : choisissez le bitrate (Best, 320, 256, 192, 128, 96, 64, 32 kbps) et le format (M4A ou MP3)

   **Cliquez** sur "⬇️ Télécharger"

   **Sélectionnez** le dossier de destination

### Astuces 💡

- Vous pouvez **ajouter plusieurs vidéos** à la file d'attente avant de lancer le téléchargement
- La **taille totale** et le nombre de vidéos s'affichent sur le bouton de téléchargement
- Utilisez le bouton **🗑️ Vider la file** pour effacer toutes les vidéos en attente
- Cliquez sur le bouton **ℹ️** à côté de chaque vidéo pour voir les informations détaillées (formats disponibles, description, etc.)
- Cliquez sur **❌** pour retirer une vidéo de la file d'attente

------

## 📚 Playlists

### Playlists publiques

Copiez simplement l'URL de la playlist dans l'onglet "Téléchargement unique", l'application détectera automatiquement toutes les vidéos ! Vous pouvez modifier les options vidéo/audio avant de lancer le téléchargement.

L'application :

- ✅ Charge automatiquement toutes les vidéos de la playlist
- ✅ Affiche une miniature et les informations pour chaque vidéo
- ✅ Permet de personnaliser les options pour chaque vidéo individuellement
- ✅ Télécharge tout en une seule opération

### 🍪 Playlists privées
#### Méthode 1 : Connexion automatique via navigateur (Recommandé ⭐)

**L'application utilise automatiquement vos cookies Firefox si vous êtes connecté à YouTube !**

1. **Connectez-vous** à votre compte YouTube dans Firefox
2. **Copiez** l'URL de votre playlist privée
3. **Collez-la** dans l'application
4. ✅ **Ça fonctionne automatiquement !** L'application accède à vos cookies Firefox

> 💡 **Astuce** : Restez connecté à YouTube dans Firefox pour que l'application puisse toujours accéder à vos playlists privées sans manipulation supplémentaire.

#### Méthode 2 : Export manuel des cookies (Alternative)

Si la méthode automatique ne fonctionne pas ou si vous utilisez un autre navigateur, vous devez fournir vos **cookies YouTube** :

1. Installez une extension navigateur :
   - **Firefox** : [cookies.txt](https://addons.mozilla.org/fr/firefox/addon/cookies-txt/) ou [get cookies](https://addons.mozilla.org/fr/firefox/addon/get_cookies/)
   - **Chrome** : [Get cookies.txt LOCALLY](https://chrome.google.com/webstore)

2. Connectez-vous à YouTube
3. **Exportez** vos cookies au format Netscape (fichier `.txt`)
4. **Cliquez** sur le bouton "🍪 ⬆️ cookies.txt" en haut à gauche de l'application
5. **Sélectionnez** votre fichier `cookies.txt`
6. **Testez** avec votre playlist privée

> ⚠️ **Attention** : Ne partagez jamais votre fichier cookies.txt, il contient vos identifiants de connexion !

### ⚠️ Conseils
- Ne supprimez pas le fichier cookies.txt
- Si une erreur apparaît, rechargez les cookies

------

## 📦 Téléchargement en lot (Batch)

L'onglet "Téléchargement en lot" permet de télécharger plusieurs vidéos avec les **mêmes paramètres** pour toutes.

### Utilisation

1. **Ouvrez** l'onglet "Téléchargement en lot"
2. **Entrez** les URLs des vidéos (une par ligne) dans la zone de texte
   - OU cliquez sur "⬆️ Charger depuis un fichier" pour importer un fichier `.txt` contenant vos URLs
3. **Sélectionnez** le type :
   - 🎥 **Vidéo** : avec résolution commune pour toutes
   - 🎵 **Audio seul** : avec bitrate commun pour toutes
4. **Choisissez** la résolution (si vidéo) et le bitrate audio
5. **Cliquez** sur "⬇️ Télécharger"
6. **Sélectionnez** le dossier de destination

### Différence avec le téléchargement simple

| Téléchargement simple                  | Téléchargement en lot                    |
| -------------------------------------- | ---------------------------------------- |
| Options **personnalisées** par vidéo   | Options **identiques** pour toutes       |
| Affiche miniatures et infos détaillées | Interface simplifiée                     |
| Idéal pour quelques vidéos variées     | Idéal pour beaucoup de vidéos similaires |

------

## ⚙️ Options avancées

### Résolution vidéo

| Résolution          | Usage recommandé                     | Taille approximative (1h) |
| ------------------- | ------------------------------------ | ------------------------- |
| **Best**            | Meilleure qualité disponible         | Variable                  |
| **2160p (4K)**      | Écrans 4K, archivage                 | ~4-8 Go                   |
| **1440p (2K)**      | Moniteurs haute définition           | ~2-4 Go                   |
| **1080p (Full HD)** | Usage standard, meilleur compromis ⭐ | ~1-2 Go                   |
| **720p (HD)**       | Appareils mobiles, économie d'espace | ~500 Mo-1 Go              |
| **480p**            | Connexion lente, stockage limité     | ~300-500 Mo               |
| **360p**            | Très faible connexion                | ~200-300 Mo               |

> 💡 **Conseil** : Pour un usage quotidien, **1080p** offre le meilleur compromis qualité/taille.

### Bitrate audio

| Bitrate      | Qualité            | Usage recommandé         | Taille (1h) |
| ------------ | ------------------ | ------------------------ | ----------- |
| **Best**     | Maximum disponible | Archivage, audiophiles ⭐ | Variable    |
| **320 kbps** | Excellente         | Musique haute qualité    | ~140 Mo     |
| **256 kbps** | Très bonne         | Usage standard           | ~115 Mo     |
| **192 kbps** | Bonne              | Compromis qualité/taille | ~85 Mo      |
| **128 kbps** | Correcte           | Podcasts, conférences    | ~60 Mo      |
| **96 kbps**  | Acceptable         | Voix uniquement          | ~45 Mo      |
| **64 kbps**  | Faible             | Très faible connexion    | ~30 Mo      |

### Format audio

- **M4A** :
  - ✅ Meilleure qualité à taille égale
  - ✅ Fichiers plus légers
  - ✅ Format natif YouTube (pas de conversion)
  - ❌ Moins compatible sur vieux lecteurs
- **MP3** :
  - ✅ Compatible avec tous les appareils
  - ✅ Largement supporté
  - ✅ Personnalisable (bitrate au choix)
  - ❌ Nécessite une conversion (FFmpeg requis)

------

## Personnalisation

### 🌍 Changer la langue

Cliquez sur le sélecteur de langue 🌐 en haut à gauche pour choisir parmi les langues disponibles.
### 🌓 Mode sombre / clair

Utilisez le switch **🌙 / ☀️** pour basculer entre les thèmes.

------

## ❓ Problèmes fréquents

### "The playlist does not exist"

**Causes possibles :**

1. La playlist est **privée** → Assurez-vous d'être connecté à YouTube dans Firefox, ou fournissez un fichier `cookies.txt`
2. L'URL est incorrecte → Vérifiez que vous avez copié l'URL complète de la playlist
3. La playlist a été supprimée → Vérifiez qu'elle existe toujours sur YouTube

### "ERROR: unable to download video data"

**Causes possibles :**

1. Connexion internet instable
2. Vidéo supprimée ou privée
3. YouTube a changé son format → Mettez à jour yt-dlp : `pip install -U yt-dlp`

### Téléchargement lent

- **Solutions :**
  - ✅ Vérifiez votre connexion internet 📶
  - ✅ YouTube limite parfois la vitesse selon votre localisation
  - ✅ Essayez de télécharger à un autre moment
  - ✅ Téléchargez une résolution plus basse (720p au lieu de 1080p)

### Erreur de conversion MP3

**Erreur** : `ERROR: ffmpeg not found`

**Solution** : La conversion MP3 nécessite **FFmpeg** installé sur votre système.

**Installation FFmpeg :**

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Windows (Chocolatey)
choco install ffmpeg
```

**Vérifier l'installation :**

```bash
ffmpeg -version
```

### Le téléchargement s'arrête à 99%

C'est normal ! L'application est en train de **fusionner** la vidéo et l'audio (ou de convertir en MP3). Cette étape peut prendre quelques secondes à quelques minutes selon :

- La taille du fichier
- La puissance de votre ordinateur
- La résolution choisie

> 💡 **Astuce** : Ne fermez pas l'application pendant que la barre de progression est à 99% !

### "Permission denied" lors du téléchargement

**Causes possibles :**

1. Le dossier de destination est protégé en écriture
2. Un fichier avec le même nom est déjà ouvert
3. Votre antivirus bloque l'écriture

**Solutions :**

- ✅ Choisissez un dossier dans votre répertoire personnel (Documents, Téléchargements)
- ✅ Fermez tout fichier vidéo ouvert
- ✅ Ajoutez une exception dans votre antivirus

## 📞 Support

### Obtenir de l'aide

Pour toute question ou problème :

- 🐛 Signalez un bug sur [GitHub](https://github.com/richbenji/Ultimate-GUI-YouTube-Downloader-yt-dlp-Ctk)

- 💬 **Question** : Consultez d'abord ce tutoriel, puis ouvrez une issue sur GitHub

- ⭐ **Vous aimez l'application ?** : Mettez une étoile sur GitHub !

### Contribuer

  Le projet est open-source ! Les contributions sont les bienvenues :

  - 🔧 Corrections de bugs
  - ✨ Nouvelles fonctionnalités
  - 🌍 Traductions supplémentaires
  - 📖 Amélioration de la documentation

------

## 📜 Mentions légales

### Utilisation responsable

Cette application est un outil de téléchargement. **Vous êtes responsable** de l'utilisation que vous en faites :

- ✅ **Autorisé** : Télécharger vos propres vidéos, du contenu sous licence libre, ou du contenu dont vous avez l'autorisation
- ❌ **Interdit** : Télécharger du contenu protégé par des droits d'auteur sans permission, redistribuer du contenu téléchargé

> ⚠️ **Important** : Respectez toujours les conditions d'utilisation de YouTube et les lois sur le droit d'auteur de votre pays.

------

**Bon téléchargement ! 🎉**