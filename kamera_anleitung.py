import streamlit as st
import pandas as pd
from PIL import Image
import os

# Seitentitel und Icon
st.set_page_config(page_title="Kamera-Anleitung", page_icon="📷")

# Haupttitel
st.title("Bedienungsanleitung Kamera")

# Sidebar mit Navigation
st.sidebar.title("Navigation")
seite = st.sidebar.radio(
    "Wählen Sie einen Abschnitt:",
    ["Schnellstart", "Technische Daten", "Grundfunktionen", "Fortgeschrittene Funktionen", "Fehlerbehebung"]
)

# Schnellstartseite
# CSS für Rahmen
st.markdown("""
    <style>
    .tabelle-block {
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 1px;
        margin-bottom: 10px;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

if seite == "Schnellstart":
    st.header("Schnellstart")

    data = [
    {
        "image_path": "content/01_Identnummer_eingeben.png",
        "image_caption": "Ident-Nr. eingeben",
        "description": "Identnummer des zu messenden Werkzeugs eingeben, den Eintrag markieren und mit STRG-C in die Zwischenablage kopieren."
    },
    {
        "image_path": "content/02_Alt-Tab.png",
        "image_caption": "App-Wechsel",
        "description": "Mit Alt-Tab von der Messsoftware zur Kamera-App wechseln."
    },
    {
        "image_path": "content/03_Foto_schießen.png",
        "image_caption": "Foto machen",
        "description": "Kameraeinstellungen vornehmen und durch Klicken des \"Auslösers\" ein Foto schießen."
    },
    {
        "image_path": "content/04_open_Folder.png",
        "image_caption": "Ablageordner öffnen",
        "description": "Mittels [1] und [2] den Ordner mit dem erstellten Foto öffnen."
    },
    {
        "image_path": "content/05_Datei_umbennen.png",
        "image_caption": "Datei umbenennen",
        "description": "Dateinamen des erzeugten Fotos in \"1\" umbenennen."
    },
    {
        "image_path": "content/06_Bild_drehen.png",
        "image_caption": "Bild drehen",
        "description": "Mit Doppelklick auf die Datei \"rotate\" das Foto um 90° nach rechts drehen."
    },
    {
        "image_path": "content/07_rotiertes Bild.png",
        "image_caption": "Bild gedreht",
        "description": "Das gedrehte Foto heißt jetzt \"2.jpg\""
    },
    {
        "image_path": "content/08_Datei in Verzeichnis verschieben.png",
        "image_caption": "Datei umbenennen und verschieben",
        "description": "Datei \"1.jpg\" löschen, Datei \"2.jpg\" mit F2 und STRG-V (kopieren aus Zwischenablage) in Identnummer umbenennen."
    },
    {
        "image_path": "content/09_Zeichnung auswählen.png",
        "image_caption": "Zeichnung auswählen",
        "description": "Mit Alt-Tab wieder zurück in die Messsoftware wechseln und über den Zeichnungsbutton in die Grafikbibliothek wechseln."
    },
    {
        "image_path": "content/10_Grafikgruppe auswählen.png",
        "image_caption": "Grafikgruppe auswählen",
        "description": "In der Grafikbibliothek die richtige Grafikgruppe per Doppelklick, oder selektieren und mit OK (rechts unten), auswählen."
    },
    {
        "image_path": "content/11_erstelltes Foto auswählen und bestätigen.png",
        "image_caption": "Frisch gepresstes Foto auswählen",
        "description": "In der Grafikgruppe das erstellte Foto per Doppelklick, oder selektieren und mit OK (rechts unten), auswählen."
    },
    {
        "image_path": "content/12_erstelltes Foto ist Werkzeug zugeordnet.png",
        "image_caption": "Herzlichen Glückwunsch",
        "description": "Das Foto ist jetzt mit dem Werkzeug verknüpft."
    },
    {
        "image_path": "content/13_erstelltes Foto in groß anzeigen.png",
        "image_caption": "Großdarstellung",
        "description": "Durch Klicken des Buttons rechts neben dem Zeichnungsname kann das Bild im Großformat angezeigt werden."
    },
]

    # Tabelle anzeigen
    for idx, item in enumerate(data, start=1):
        with st.container():
            st.markdown('<div class="tabelle-block">', unsafe_allow_html=True)

            col1, col2, col3 = st.columns([1, 2, 4])
            
            with col1:
                st.write(f"**{idx}.**")

            with col2:
                if os.path.exists(item["image_path"]):
                    image = Image.open(item["image_path"])
                    st.image(image, caption=item["image_caption"], use_container_width=True)

            with col3:
                st.write(item["description"])

# Technische Daten
elif seite == "Technische Daten":
    st.header("Technische Daten")
    
    specs = {
        "Eigenschaft": ["Auflösung", "Sensor", "ISO-Bereich", "Verschlusszeiten", "Videoauflösung", "Gewicht"],
        "Wert": ["5 Megapixel", "APS-C CMOS", "100-25600", "1/8000 - 30 Sek.", "4K/60fps", "450g"]
    }
    
    st.table(pd.DataFrame(specs))

# Footer
st.divider()
st.write("© 2025 CNC-Katze • Version 1.0 • info@cnckatze.de")