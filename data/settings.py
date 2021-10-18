import os
import dotenv

dotenv.load_dotenv('.env')

BOT_TOKEN = str(os.environ['BOT_TOKEN'])
ADMIN_ID = int(os.environ['ADMIN_ID'])
HOST = str(os.environ['HOST'])
USER = str(os.environ['USER'])
PASSWORD = str(os.environ['PASSWORD'])
DB_NAME = str(os.environ['DB_NAME'])
PORT = int(os.environ['PORT'])
