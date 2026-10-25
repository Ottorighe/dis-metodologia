# Definizione del DIS

## Definizione

**DIS, Detenuti in Istituti Sovraffollati.** Numero complessivo delle persone presenti in istituti penitenziari nei quali le presenze superano la capienza. Si esprime in valore assoluto oppure come quota percentuale sul totale dei detenuti.

Un istituto entra nel conteggio quando **presenze > capienza**. La soglia è questa, senza margini di tolleranza. Un istituto con presenze uguali alla capienza non è sovraffollato.

## Perché una misura diversa

La misura più diffusa del sovraffollamento conta quante persone sono *in eccedenza* rispetto ai posti: in un istituto da 100 posti con 150 presenti, 50 persone. Ma docce, infermeria, ore d'aria, colloqui, personale e spazi comuni sono dimensionati per 100 e usati da 150: il sovraffollamento è una condizione dell'istituto, non di alcuni dei suoi detenuti. Il DIS risponde a un'altra domanda: non quanti sono di troppo, ma **quante persone vivono dentro un istituto sovraffollato**.

## Formula

Per ogni istituto *i* di una data di rilevazione:

```
p_i  = detenuti presenti
c_i  = capienza (regolamentare, oppure effettiva)
sovraffollato_i = (p_i > c_i)

DIS (assoluto)   = somma di p_i  per gli istituti con sovraffollato_i
DIS (percentuale) = DIS (assoluto) / somma di p_i su tutti gli istituti x 100
```

## Le due varianti

| Variante | Capienza usata | Fonte della capienza |
|---|---|---|
| **Ufficiale** (regolamentare) | posti previsti dalle norme | bollettini mensili del DAP |
| **Effettiva** | capienza regolamentare meno posti non disponibili (lavori, inagibilità, chiusura di sezioni) | bollettini DAP e schede di trasparenza degli istituti |

La variante effettiva è disponibile dal giugno 2026, quando le schede di trasparenza sono entrate nel ciclo di elaborazione. Per i mesi precedenti esiste solo la variante ufficiale. Si indica sempre quale delle due si sta usando.

## Differenza dal tasso di affollamento

| Indicatore | Calcolo | Valori possibili | Che cosa dice |
|---|---|---|---|
| Tasso di affollamento | presenti / capienza x 100 | da 0% senza limite superiore | quanto è pieno il sistema rispetto ai posti |
| DIS | detenuti in istituti dove presenti > capienza | da 0% a 100% | quale quota della popolazione detenuta è esposta al problema |

Sono grandezze diverse con scale diverse e non vanno confuse.

## Esempio numerico

Tre istituti, capienza regolamentare e presenti: A 100 posti e 150 presenti; B 200 posti e 180 presenti; C 50 posti e 50 presenti.
- A è sovraffollato (150 > 100); B no; C no (50 non supera 50).
- DIS assoluto = 150. Totale presenti = 380. DIS percentuale = 150 / 380 = 39,5%.
- Tasso di affollamento = 380 / 350 = 108,6%.

Se in B risultassero 30 posti non disponibili, la capienza effettiva di B sarebbe 170 e B (180 > 170) entrerebbe nel conteggio: DIS effettivo = 330 (86,8%).

## Casi limite

- **Capienza effettiva zero o negativa:** l'istituto non entra nella variante effettiva se la capienza effettiva non è positiva (è un caso di dato incoerente, da segnalare).
- **Istituti senza scheda di trasparenza:** nella variante effettiva restano fuori; il perimetro dichiarato è di 189 istituti per adulti.
- **Cambi di denominazione:** gli istituti si identificano con il codice ufficiale, non con il nome, che nei bollettini varia da un mese all'altro.
- **Soglia netta:** piccoli spostamenti attorno alla soglia (una presenza in più o in meno) possono muovere il dato aggregato; nel Report si segnala quando succede.

Metodologia completa e limiti dichiarati: https://www.ottorighe.it/metodologia-sovraffollamento/
