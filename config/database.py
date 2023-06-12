# Configurations de la base de données

# Importation du module os pour manipuler les chemins de fichiers
import os

# Obtention du chemin absolu du dossier actuel
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Chemin complet du fichier SQLite dans le dossier "static"
DATABASE_PATH = os.path.join(BASE_DIR, '../static/your_database.db')

# URI de la base de données SQLite
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'

# Désactivation du suivi des modifications de SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
