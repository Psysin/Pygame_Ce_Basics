# PyGame CE Basics

Ein persönliches Lern-Repository, in dem ich mich mit **Python** und **pygame-ce** beschäftige — Übungen, kleine Experimente und Zwischenstände aus verschiedenen Tutorials.

## Hintergrund & Lernziel

Ich lerne aktuell Python und vertiefe parallel dazu gezielt **pygame-ce**, um praktische Grundlagen in der Spieleentwicklung zu sammeln (Gameloop, Zustände, Kollisionen, Rendering). pygame-ce ist dabei bewusst als Zwischenstation gewählt: Mein längerfristiges Ziel ist es, mit **Godot** ein eigenes Spiel zu entwickeln — dafür möchte ich mir vorher an kleinen, selbst geschriebenen Python/pygame-Projekten ein solides GameDev-Fundament erarbeiten.

Der Code hier ist entsprechend Lernstand: teils aus Tutorials abgeleitet, teils eigene Übungen und Experimente. Kommentare und Struktur sollen mir (und potenziellen Mitlesern) helfen, den eigenen Fortschritt nachzuvollziehen.

## Struktur

```
PyGame_CE_Basics/
├── 01_Einstieg/         # Erste Schritte mit pygame-ce: Fenster, Gameloop, einfaches Zeichnen
├── 02_Übung_01/         # Übung: Kreisbewegung mit Abprallen an den Fensterrändern (horizontal & vertikal)
└── requirements.txt     # Projektabhängigkeiten
```

Jeder Ordner enthält eine eigenständig lauffähige `main.py`.

## Voraussetzungen

- Python 3.14
- [pygame-ce](https://pyga.me/) `2.5.8`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ausführen

```bash
python 01_Einstieg/main.py
python "02_Übung_01/main.py"
```

## Status

🚧 Laufend — dieses Repo wächst mit jedem neuen Tutorial-Abschnitt bzw. jeder neuen Übung.