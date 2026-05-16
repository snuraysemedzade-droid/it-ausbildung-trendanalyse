# -*- coding: utf-8 -*-
"""
Projekt: IT-Ausbildung Trendanalyse in Deutschland
Autorin: Nuray Samadzade
Ziel: Analyse von Städten, Fachrichtungen und Gehaltssimulationen für Fachinformatiker.
"""

import time

def begruessung():
    print("=" * 60)
    print("    WILLKOMMEN ZUR IT-AUSBILDUNG TRENDANALYSE (2026)    ")
    print("=" * 60)
    print("Analysiere Daten für Fachinformatiker für Anwendungsentwicklung...\n")
    time.sleep(1)

def staedte_analyse():
    # Almanya'daki popüler IT şehirleri ve popülerlik skorları (Simülasyon Verisi)
    it_staedte = {
        "München": "Sehr Hoch (Hub für Großunternehmen)",
        "Berlin": "Sehr Hoch (Start-up und Tech-Metropole)",
        "Frankfurt": "Hoch (FinTech und Banken-IT)",
        "Hamburg": "Hoch (Logistik-IT und Agenturen)",
        "Stuttgart": "Hoch (Automobil-IT & Embedded Systems)"
    }
    
    print("-" * 55)
    print("1. Top-Städte für IT-Ausbildung in Deutschland:")
    print("-" * 55)
    
    for stadt, trend in it_staedte.items():
        print(f"📍 Stadt: {stadt:<12} | Trend-Score: {trend}")
        time.sleep(0.5)
    print()

def gehalt_rechner(brutto_gehalt):
    # Basit bir Netto maaş hesaplama simülasyonu (Almanya Vergi Sınıfı 1 için yaklaşık %35 kesinti)
    abzuege = brutto_gehalt * 0.35
    netto = brutto_gehalt - abzuege
    return netto

def gehalts_analyse():
    # Yıllara göre ortalama Ausbildung brüt maaşları (Euro)
    ausbildung_gehaelter = {
        "1. Lehrjahr": 1150,
        "2. Lehrjahr": 1250,
        "3. Lehrjahr": 1380
    }
    
    print("-" * 55)
    print("2. Gehaltsanalyse & Netto-Simulation (Steuerklasse 1):")
    print("-" * 55)
    
    for jahr, brutto in ausbildung_gehaelter.items():
        netto_betrag = gehalt_rechner(brutto)
        print(f"💶 {jahr}: Brutto: {brutto}€ | Geschätztes Netto: {netto_betrag:.2f}€")
        time.sleep(0.5)
    print()

def main():
    begruessung()
    staedte_analyse()
    gehalts_analyse()
    
    print("=" * 60)
    print("   ANALYSE ERFOLGREICH BEENDET | BEREIT FÜR DIE ZUKUNFT   ")
    print("=" * 60)

if __name__ == "__main__":
    main()
