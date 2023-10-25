# Oh My Tello

Questo programma è progettato per controllare uno sciame di droni Tello utilizzando la libreria djitellopy. Di seguito sono fornite istruzioni su come configurare e eseguire il programma.

La libreria utilizzata è la seguente [Djitellopy](https://djitellopy.readthedocs.io/en/latest/swarm/), tutte le funzioni sono disponibili nella wiki

# Istruzioni

## 1. Installazione

Per prima cosa, assicurati di avere Python installato sul tuo sistema. Puoi scaricarlo da [python.org](https://www.python.org/).

### Clona il repository
```bash
git clone https://github.com/passarelli-dev/Oh-my-tello.git
```

### Naviga nella cartella del progetto
```bash
cd oh-my-tello
```

### Crea e attiva un virtualenv (comandi per Mac e Windows)
```bash
python -m venv venv  # Mac
python -m venv venv  # Windows
```

### Attiva il virtualenv (comandi per Mac e Windows)
```bash
source venv/bin/activate  # Mac
.\venv\Scripts\activate  # Windows
```
## 2. Installa i requisiti

```bash
pip install -r requirements.txt
```
## 3. Configura gli indirizzi IP dei droni

Apri il file main.py e sostituisci gli indirizzi IP dei droni con quelli dei tuoi droni Tello.

```bash
swarm = TelloSwarm.fromIps([
    "192.168.1.101",
    "192.168.1.103"
])
```

## 4. Esegui il programma
```bash
python main.py
```

Il programma si connetterà ai droni, verificherà la batteria, eseguirà una sequenza di comandi (decolla, si sposta in alto, esegue un flip in avanti, atterra) e quindi terminerà.

Ricorda di rispettare tutte le normative locali e di volo sicuro durante l'utilizzo di droni. Buon divertimento con il tuo sciame di droni Tello!