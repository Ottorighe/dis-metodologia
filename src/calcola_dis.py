# -*- coding: utf-8 -*-
"""Implementazione di riferimento del DIS (Detenuti in Istituti Sovraffollati).

Uso:  python src/calcola_dis.py file.csv

Il file CSV (separatore virgola, UTF-8) ha le colonne: istituto, capienza_regolamentare, posti_non_disponibili
(facoltativa) e presenti. Per ogni istituto sovraffollato (presenti maggiori della capienza) si sommano TUTTI i
presenti. Vengono stampate le due varianti: sulla capienza regolamentare e sulla capienza effettiva.
Nessuna dipendenza esterna.
"""
import csv
import sys


def leggi(percorso):
    righe = []
    with open(percorso, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            righe.append({
                "istituto": r["istituto"],
                "cap_reg": int(r["capienza_regolamentare"]),
                "non_disp": int(r.get("posti_non_disponibili") or 0),
                "presenti": int(r["presenti"]),
            })
    return righe


def dis(righe, effettiva=False):
    """Restituisce (dis_assoluto, dis_percentuale, istituti_sovraffollati, tasso_affollamento_percentuale)."""
    totale_presenti = sum(r["presenti"] for r in righe)
    capienza_totale = 0
    esposti = 0
    n_sovr = 0
    for r in righe:
        cap = r["cap_reg"] - (r["non_disp"] if effettiva else 0)
        capienza_totale += max(cap, 0)
        if effettiva and cap <= 0:
            continue  # capienza effettiva non positiva: dato incoerente, l'istituto non entra nel conteggio
        if r["presenti"] > cap:
            esposti += r["presenti"]
            n_sovr += 1
    pct = esposti / totale_presenti * 100 if totale_presenti else 0.0
    tasso = totale_presenti / capienza_totale * 100 if capienza_totale else 0.0
    return esposti, pct, n_sovr, tasso


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    righe = leggi(sys.argv[1])
    for nome, eff in (("ufficiale (capienza regolamentare)", False), ("effettivo (capienza regolamentare meno posti non disponibili)", True)):
        a, p, n, t = dis(righe, effettiva=eff)
        print(f"DIS {nome}: {a} persone, {p:.1f}% dei presenti; istituti sovraffollati {n} su {len(righe)}; tasso di affollamento {t:.1f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
