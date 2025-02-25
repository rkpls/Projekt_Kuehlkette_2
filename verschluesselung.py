"""Testprogramm der Ent- und Verschlüsselung der Datenbank Daten.
Author: David Grambardt
Datum: 25.02.2025
Hinweis: pip install pycryptodome"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import pyodbc

import pyodbc

# 📡 Verbindungsinfo
server = 'sc-db-server.database.windows.net'
database = 'supplychain'
username = 'rse'
password = 'Pa$$w0rd'

# 🔗 Verbindung zur SQL Server-Datenbank herstellen
conn_str = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("✅ Verbindung erfolgreich!")

    # 🔍 Beispiel-Query – passe die Tabelle und Spalte an!
    query = "SELECT * FROM transportstation_crypt WHERE transportstation = ?"
    cursor.execute(query, (1,))  # Beispiel: Eintrag mit id=1 holen

    # 📋 Daten abrufen
    result = cursor.fetchone()

    if result:
        encrypted_base64 = result[0]  # Base64-codierter String
        print(f"📋 Base64-Daten: {encrypted_base64}")
    else:
        print("❌ Kein Eintrag gefunden.")

except Exception as e:
    print(f"❌ Fehler bei der Verbindung: {e}")

finally:
    # 🔒 Verbindung schließen
    conn.close()

"""
# 🔑 Schlüssel und Initialisierungsvektor (IV)
key = b'mysecretpassword'      # Muss 16 Bytes sein
iv = b'passwort-salzen!'       # 16 Bytes IV

# 📁 Beispiel für einen verschlüsselten Datenbankeintrag (Base64-codiert)
# Ersetze das mit deinem verschlüsselten String!
encrypted_data_base64 = 'VerschlüsselterBase64StringHier'

# 📤 Schritt 1: Base64-String dekodieren
encrypted_data = base64.b64decode(encrypted_data_base64)

# 🔓 Schritt 2: AES-Cipher für Entschlüsselung initialisieren
cipher = AES.new(key, AES.MODE_CBC, iv)

# 📋 Schritt 3: Daten entschlüsseln und Padding entfernen
try:
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded, AES.block_size)  # Padding entfernen

    print(f"🔓 Entschlüsselte Daten: {decrypted_data.decode('utf-8')}")
except ValueError as e:
    print("❌ Entschlüsselung fehlgeschlagen:", e)
"""