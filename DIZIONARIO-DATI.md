# Dizionario dei dati

## `dati/dis_nazionale_mensile.csv`

Separatore virgola, codifica UTF-8, punto decimale. Una riga per mese di rilevazione dei bollettini DAP (dati al 31 del mese, o all'ultimo giorno disponibile).

| Colonna | Tipo | Significato |
|---|---|---|
| `mese` | testo `AAAA-MM` | mese di riferimento del bollettino |
| `presenze` | intero | detenuti presenti negli istituti per adulti del perimetro |
| `capienza_regolamentare` | intero | somma delle capienze regolamentari |
| `tasso_affollamento_ufficiale_pct` | decimale | presenze / capienza regolamentare x 100 |
| `istituti_sovraffollati_ufficiale` | intero | istituti con presenze maggiori della capienza regolamentare |
| `dis_ufficiale_assoluto` | intero | DIS, variante ufficiale: presenti negli istituti sovraffollati sulla capienza regolamentare |
| `dis_ufficiale_pct` | decimale | `dis_ufficiale_assoluto` / `presenze` x 100 |
| `capienza_effettiva` | intero, vuoto prima di giugno 2026 | capienza regolamentare meno posti non disponibili (schede di trasparenza) |
| `posti_non_disponibili` | intero, vuoto prima di giugno 2026 | `capienza_regolamentare` meno `capienza_effettiva` |
| `tasso_affollamento_effettivo_pct` | decimale, vuoto prima di giugno 2026 | presenze / capienza effettiva x 100 |
| `istituti_sovraffollati_effettivo` | intero, vuoto prima di giugno 2026 | istituti con presenze maggiori della capienza effettiva |
| `dis_effettivo_assoluto` | intero, vuoto prima di giugno 2026 | DIS, variante effettiva |
| `dis_effettivo_pct` | decimale, vuoto prima di giugno 2026 | `dis_effettivo_assoluto` / `presenze` x 100 |
| `istituti_totali` | intero | istituti nel perimetro del bollettino del mese (189 o 190; il Report ne considera 189) |

**Note.**
- Le colonne effettive sono vuote prima di giugno 2026, perché le schede di trasparenza sono entrate nel ciclo di elaborazione solo allora.
- I dati ufficiali provengono dai bollettini del Ministero della giustizia; la variante effettiva usa in più la data di aggiornamento delle schede, che può non coincidere con quella del bollettino.
- Controllo incrociato: i valori di agosto e settembre 2026 coincidono con quelli pubblicati nel Report (numeri 4 e 5).

## `esempio/istituti_esempio.csv`

Cinque istituti **inventati**, solo per provare `src/calcola_dis.py`.

| Colonna | Significato |
|---|---|
| `istituto` | nome (di fantasia) |
| `capienza_regolamentare` | posti previsti |
| `posti_non_disponibili` | posti inagibili o chiusi (può essere vuoto o 0) |
| `presenti` | detenuti presenti |
