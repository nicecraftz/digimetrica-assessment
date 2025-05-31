# Imago

**Imago** è un progetto di assessment sviluppato per l’azienda Digimetrica.

Si tratta di una piccola applicazione capace di catturare screenshot di pagine web a partire da un URL fornito in input.

---

## Documentazione

Il progetto è organizzato in due sottosistemi, pensati per poter essere eseguiti anche senza l’uso di Docker.

---

### Requisiti comuni (senza Docker)

Prima di eseguire qualsiasi modalità, assicurati di:
- Installare le dipendenze Python:
    ```sh
    pip install -r requirements.txt
    ```
- Installare i browser Playwright (solo al primo utilizzo o dopo aggiornamenti):
    ```sh
    playwright install
    ```

---

### Esecuzione senza visualizzazione (input JSON)

Per eseguire solo l’elaborazione tramite il file `data.json`, imposta correttamente la variabile `PYTHONPATH` e avvia:

- **Linux / macOS**
    ```sh
    export PYTHONPATH=$(pwd)
    python3 main.py
    ```

- **Windows (cmd)**
    ```batch
    set PYTHONPATH=%cd%
    python main.py
    ```

- **Windows (PowerShell)**
    ```ps
    $env:PYTHONPATH = (Get-Location)
    python main.py
    ```

---

### Esecuzione con visualizzazione (interfaccia Streamlit)

Per avviare l’interfaccia grafica Streamlit, sempre dopo aver configurato `PYTHONPATH`:

- **Linux / macOS**
    ```sh
    export PYTHONPATH=$(pwd)
    streamlit run visualization/streamlit_app.py
    ```

- **Windows (cmd)**
    ```cmd
    set PYTHONPATH=%cd%
    streamlit run visualization/streamlit_app.py
    ```

- **Windows (PowerShell)**
    ```powershell
    $env:PYTHONPATH = (Get-Location)
    streamlit run visualization/streamlit_app.py
    ```

⚠ **Nota:**
L’esportazione della variabile `PYTHONPATH` è richiesta solo una volta per sessione di terminale, fino alla sua chiusura.

---

### Utilizzo tramite Docker

Per evitare configurazioni manuali e sfruttare un ambiente già pronto, puoi utilizzare Docker:

```sh
docker build -t imago .
docker run -p 8501:8501 imago
```

Successivamente, accedi all’interfaccia Streamlit tramite browser all’indirizzo:
[https://localhost:8501](https://localhost:8501)

---

## Autori

- [@nicecraftz](https://www.github.com/nicecraftz)
