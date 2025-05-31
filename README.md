# Imago

**Imago** è un progetto di assessment sviluppato per l’azienda Digimetrica, pensato per dimostrare competenze pratiche nello sviluppo software e nella gestione di applicazioni web.

L’applicazione è progettata per catturare automaticamente screenshot di pagine web partendo da un semplice input: un URL fornito dall’utente. Può operare sia su singoli indirizzi, mostrando l’immagine direttamente nell’interfaccia, sia su liste multiple di URL, elaborandoli in blocco e restituendo un archivio `.zip` contenente tutte le immagini generate.

Grazie alla sua architettura leggera e alla scelta di Streamlit per la visualizzazione, Imago offre un’interfaccia semplice, pulita e immediata. È pensato per essere facilmente eseguibile tramite un container Docker, garantendo massima portabilità e riducendo a zero le configurazioni necessarie.

---

### Utilizzo

Per evitare configurazioni manuali e sfruttare un ambiente già pronto, utilizza Docker:

```sh
docker build -t imago .
docker run -p 8501:8501 imago
```

Successivamente, accedi all’interfaccia Streamlit tramite browser all’indirizzo:
[https://localhost:8501](https://localhost:8501)

---

## Autori

- [@nicecraftz](https://www.github.com/nicecraftz)
