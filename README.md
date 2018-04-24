# Smart Room Projekt
 Discontinued
 
# Software-Locations
  Android-Client: \ui\android\app\build\outputs\apk\debug\app-debug.apk <br>
  Desktop-Client: \ui\desktop\app\bin\Debug\app.exe <br>
  
  Server: \server\Server.py
  
  Aktor-Module: \hardware\actor-TODO | \server\testDevices\test_actorX.py
  
  
# TODO
  ## 1. Standard-SmartHome Funktionalität + Basic-UI ✓
     - Server ✓
     - UI ✓
     - Aktoren ✓
  ## 2. User-Tracking
     - Personenerkennung (ohne blinde Winkel)
     - Logging
  ## 3. Aktivitäts/Interaktions-Erkennung & Log
     - Interaktions-Punkte erkennen & manuell hinzufügen
     - 3D-Sphere um Punkte + Erkennung von Person in Sphere
     - Log
  ## 4. Gewohnheiten/Tagesabläufe lernen (RNN)
     - Daten aus Log zu Koordsystem (Zeit, (X, Y))
     - Daten -> Gewohnheiten/Tagesabläufen
  ## 5. Kombinieren
     - Tagesabläufe -> Aktionen
     - Gewohnheiten -> Aktionen
