# DIS: Detenuti in Istituti Sovraffollati

Definizione, metodo e serie storica di un indicatore sul sovraffollamento delle carceri italiane, elaborato dalla redazione di [Ottorighe](https://www.ottorighe.it/) e pubblicato ogni mese nel *Report mensile sulle carceri italiane*.

> **In breve.** Il DIS è il numero di persone detenute presenti in istituti penitenziari nei quali, alla data di rilevazione, le presenze superano la capienza. Si esprime in valore assoluto o come quota percentuale sul totale dei detenuti. Un istituto entra nel conteggio quando le presenze sono maggiori della capienza, senza margini di tolleranza.

## Che cosa c'è in questo repository

| Percorso | Contenuto |
|---|---|
| [`DEFINIZIONE.md`](DEFINIZIONE.md) | Definizione formale, le due varianti (capienza regolamentare ed effettiva), differenza dal tasso di affollamento, casi limite |
| [`DIZIONARIO-DATI.md`](DIZIONARIO-DATI.md) | Significato di ogni colonna dei file di dati |
| [`dati/dis_nazionale_mensile.csv`](dati/dis_nazionale_mensile.csv) | Serie nazionale mensile da gennaio 2025: presenze, capienza, tasso di affollamento, istituti sovraffollati e DIS (variante ufficiale) e, da giugno 2026, variante effettiva |
| [`src/calcola_dis.py`](src/calcola_dis.py) | Implementazione di riferimento: calcola il DIS da un file CSV di istituti (poche righe, nessuna dipendenza) |
| [`esempio/istituti_esempio.csv`](esempio/istituti_esempio.csv) | Esempio **inventato** di cinque istituti, per provare il calcolo |
| [`tests/test_dis.py`](tests/test_dis.py) | Verifiche automatiche dell'implementazione |
| [`CITATION.cff`](CITATION.cff) | Come citare questo lavoro |

Non è un archivio del codice di raccolta e normalizzazione dei dati: qui si pubblicano la definizione, il metodo e i risultati, in modo che chiunque possa rifare i conti partendo dalle fonti ufficiali.

## Fonti dei dati

- **Bollettini mensili del Dipartimento dell'amministrazione penitenziaria** (Ministero della giustizia), sezione [Statistiche](https://www.giustizia.it/giustizia/page/it/statistiche): per ogni istituto, capienza regolamentare e detenuti presenti.
- **Schede di trasparenza degli istituti penitenziari** (Ministero della giustizia, [istituti penitenziari](https://www.giustizia.it/giustizia/page/it/istituti_penitenziari)): posti non disponibili, da cui si ricava la capienza effettiva.

Il Ministero della giustizia resta la fonte primaria: per un uso scientifico va citata quella. Questo lavoro serve a renderla leggibile.

## Come si calcola, in due righe

```
capienza_effettiva = capienza_regolamentare - posti_non_disponibili
un istituto è sovraffollato se presenti > capienza        (regolamentare o effettiva)
DIS = somma dei presenti negli istituti sovraffollati     (valore assoluto)
DIS % = DIS / somma di tutti i presenti x 100
```

Si contano **tutte** le persone presenti nell'istituto sovraffollato, non solo l'eccedenza. Il DIS in percentuale non supera mai il 100%; il tasso di affollamento (presenti / capienza) invece può superarlo.

## Provarlo

```
python src/calcola_dis.py esempio/istituti_esempio.csv
python -m unittest discover tests
```

## Limiti

La rilevazione è una fotografia riferita a una data e non registra i movimenti fra una rilevazione e l'altra; la soglia è netta (un istituto con una presenza in più della capienza conta come uno che la supera di molto); bollettini e schede non sono aggiornati alla stessa data. Il dettaglio è nella [pagina di metodologia](https://www.ottorighe.it/metodologia-sovraffollamento/).

## Licenza

Dati e testi: [Creative Commons Attribuzione 4.0](LICENSE) (CC BY 4.0), con indicazione della fonte. Codice di esempio: licenza MIT ([`LICENSE-CODICE`](LICENSE-CODICE)).

## Contatti

redazione@ottorighe.it · [www.ottorighe.it](https://www.ottorighe.it/) · [Pagina del DIS con i dati del mese](https://www.ottorighe.it/carceri/dis/)

---

## English summary

**DIS (Detenuti in Istituti Sovraffollati, "prisoners in overcrowded institutions")** is a statistical indicator of prison overcrowding in Italy, devised by the editorial team of Ottorighe: the number of people held in prisons where the number of inmates exceeds capacity, as an absolute figure or as a share of the total prison population. It is computed on two capacity bases (regulatory capacity, and effective capacity net of unavailable places) from public data of the Italian Department of Penitentiary Administration and the Ministry of Justice. This repository contains the definition, the data dictionary, the monthly national series and a small reference implementation. Data and text are released under CC BY 4.0.
