import streamlit as st
import pandas as pd

# Seitentitel und Icon
st.set_page_config(page_title="Kamera-Anleitung", page_icon="📷")

# Haupttitel
st.title("Digitalkamera - Bedienungsanleitung")

# Sidebar mit Navigation
st.sidebar.title("Navigation")
seite = st.sidebar.radio(
    "Wählen Sie einen Abschnitt:",
    ["Übersicht", "Technische Daten", "Grundfunktionen", "Fortgeschrittene Funktionen", "Fehlerbehebung"]
)

# Übersichtsseite
if seite == "Übersicht":
    st.header("Übersicht")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300x200", caption="Modell: DigiCam X500")
    
    with col2:
        st.write("""
        Willkommen zur interaktiven Bedienungsanleitung für die DigiCam X500. 
        Diese Anleitung führt Sie durch alle Funktionen und Einstellungen Ihrer neuen Kamera.
        
        Nutzen Sie die Navigation in der Seitenleiste, um zu den verschiedenen Abschnitten zu gelangen.
        """)
    
    st.subheader("Lieferumfang")
    st.write("- DigiCam X500 Kamera")
    st.write("- Lithium-Ionen Akku")
    st.write("- USB-C Ladekabel")
    st.write("- Trageriemen")
    st.write("- Schnellstartanleitung")

# Technische Daten
elif seite == "Technische Daten":
    st.header("Technische Daten")
    
    specs = {
        "Eigenschaft": ["Auflösung", "Sensor", "ISO-Bereich", "Verschlusszeiten", "Display", "Videoauflösung", "Gewicht", "Akkulaufzeit"],
        "Wert": ["24 Megapixel", "APS-C CMOS", "100-25600", "1/8000 - 30 Sek.", "3,5 Zoll Touchscreen", "4K/60fps", "450g", "ca. 500 Aufnahmen"]
    }
    
    st.table(pd.DataFrame(specs))

# Grundfunktionen
elif seite == "Grundfunktionen":
    st.header("Grundfunktionen")
    
    tab1, tab2, tab3 = st.tabs(["Ein/Ausschalten", "Foto aufnehmen", "Video aufnehmen"])
    
    with tab1:
        st.subheader("Ein- und Ausschalten")
        st.write("""
        1. Zum Einschalten halten Sie den Ein/Aus-Schalter (oben rechts) für 2 Sekunden gedrückt
        2. Das Display zeigt das Startlogo und wechselt dann zur Liveansicht
        3. Zum Ausschalten halten Sie den gleichen Schalter erneut für 2 Sekunden gedrückt
        """)
    
    with tab2:
        st.subheader("Foto aufnehmen")
        st.write("""
        1. Stellen Sie sicher, dass der Modus-Wahlschalter auf 'FOTO' steht
        2. Komponieren Sie Ihr Bild mit dem LCD-Display oder dem Sucher
        3. Drücken Sie den Auslöser halb durch, um zu fokussieren (grüner Fokuspunkt)
        4. Drücken Sie den Auslöser vollständig durch, um das Foto aufzunehmen
        """)
    
    with tab3:
        st.subheader("Video aufnehmen")
        st.write("""
        1. Drehen Sie den Modus-Wahlschalter auf die Position 'VIDEO'
        2. Drücken Sie den roten Videoaufnahmeknopf, um die Aufnahme zu starten
        3. Die Aufnahmezeit wird in der oberen rechten Ecke des Displays angezeigt
        4. Drücken Sie erneut den roten Knopf, um die Aufnahme zu beenden
        """)

# Fortgeschrittene Funktionen
elif seite == "Fortgeschrittene Funktionen":
    st.header("Fortgeschrittene Funktionen")
    
    option = st.selectbox(
        "Wählen Sie eine Funktion:",
        ["Belichtungsmodi", "Weißabgleich", "Autofokus-Modi", "WiFi-Verbindung"]
    )
    
    if option == "Belichtungsmodi":
        st.subheader("Belichtungsmodi")
        st.write("""
        **P (Programmautomatik)**: Kamera wählt Blende und Verschlusszeit automatisch
        
        **S (Zeitpriorität)**: Sie wählen die Verschlusszeit, Kamera stellt Blende ein
        
        **A (Blendenpriorität)**: Sie wählen die Blende, Kamera stellt Verschlusszeit ein
        
        **M (Manuell)**: Volle manuelle Kontrolle über Blende und Verschlusszeit
        """)
    
    elif option == "Weißabgleich":
        st.subheader("Weißabgleich")
        st.write("""
        Zugriff über Menü > Aufnahme > Weißabgleich oder über die WB-Taste.
        
        - Auto: Automatischer Weißabgleich für die meisten Situationen
        - Sonnig: Für Außenaufnahmen bei Sonnenschein (ca. 5500K)
        - Schatten: Für Aufnahmen im Schatten (ca. 7000K)
        - Bewölkt: Für bewölkten Himmel (ca. 6000K)
        - Kunstlicht: Für Glühlampen und warmes Licht (ca. 3200K)
        - Leuchtstofflampe: Für Leuchtstoffröhren (mehrere Presets)
        - Manuell: Eigene Einstellung mit Referenz-Weißkarte
        """)
    
    elif option == "Autofokus-Modi":
        st.subheader("Autofokus-Modi")
        st.write("""
        - Einzel-AF (AF-S): Fokussiert einmal und hält den Fokus
        - Kontinuierlicher AF (AF-C): Passt den Fokus kontinuierlich an
        - Automatischer AF (AF-A): Wechselt zwischen AF-S und AF-C
        - Manueller Fokus (MF): Volle manuelle Kontrolle über den Fokus
        
        Wechseln zwischen den Modi über den AF-Schalter an der Kameraseite.
        """)
    
    elif option == "WiFi-Verbindung":
        st.subheader("WiFi-Verbindung zur Smartphone-App")
        st.write("""
        1. Installieren Sie die "DigiCam Connect" App aus dem App Store oder Google Play
        2. Drücken Sie die WiFi-Taste an der Kamera oder aktivieren Sie WiFi im Menü
        3. Öffnen Sie die WLAN-Einstellungen auf Ihrem Smartphone
        4. Verbinden Sie sich mit dem Netzwerk "DigiCam_X500" (Passwort: im Menü unter Netzwerk > WiFi-Passwort)
        5. Starten Sie die DigiCam Connect App und folgen Sie den Anweisungen
        """)

# Fehlerbehebung
elif seite == "Fehlerbehebung":
    st.header("Fehlerbehebung")
    
    expander = st.expander("Kamera lässt sich nicht einschalten")
    expander.write("""
    1. Überprüfen Sie, ob der Akku geladen ist
    2. Entnehmen Sie den Akku für 10 Sekunden und setzen Sie ihn wieder ein
    3. Versuchen Sie ein anderes Ladegerät oder Kabel
    4. Wenn das Problem weiterhin besteht, kontaktieren Sie den Support
    """)
    
    expander = st.expander("Fotos sind unscharf")
    expander.write("""
    1. Reinigen Sie das Objektiv mit einem Mikrofasertuch
    2. Prüfen Sie, ob der Autofokus aktiviert ist
    3. Stellen Sie sicher, dass genügend Licht vorhanden ist
    4. Verwenden Sie bei schwachem Licht ein Stativ
    5. Versuchen Sie, die ISO-Einstellung zu erhöhen
    """)
    
    expander = st.expander("Speicherkartenfehler")
    expander.write("""
    1. Schalten Sie die Kamera aus
    2. Entnehmen Sie die Speicherkarte und setzen Sie sie wieder ein
    3. Formatieren Sie die Karte (Achtung: Alle Daten gehen verloren)
    4. Versuchen Sie eine andere Speicherkarte
    """)
    
    expander = st.expander("Akku entlädt sich schnell")
    expander.write("""
    1. Deaktivieren Sie WiFi und Bluetooth, wenn nicht benötigt
    2. Reduzieren Sie die Display-Helligkeit
    3. Aktivieren Sie den Energiesparmodus im Menü
    4. Bei kaltem Wetter die Kamera warm halten
    5. Erwerben Sie einen Ersatzakku für längere Fotosessions
    """)

# Footer
st.divider()
st.write("© 2025 DigiCam GmbH • Version 1.0 • kontakt@digicam.de")