# Fake-news
Stiamo realizzando un modello ad agenti in SLAPP, per simulare la diffusione di fake news su Twitter, nello scenario delle presidenziali 
USA del 2016.

## Il modello
I nodi rappresentano gli agenti, cioè gli account twitter.
I link rappresentano i retweet, cioè il nodo A è connesso al nodo B, se l'account A ha retwettato un tweet dell'account B.
1. Si parte da un network random, free scale e diretto, con un numero fissato di nodi.
2. Si impostano le regole della dinamica.
3. Si valuta l'evoluzione del network nel tempo. 
4. Analisi dei dati. 

## Dataset sul network di retweet 
Per quanto riguarda i dati e le regole della dinamica, ci basiamo sul seguente paper:
https://www.nature.com/articles/s41467-018-07761-2
consultabile gratuitamente. 

## Sviluppo
### Fase 1: costruzione della rete ... completata
- Costruire i nodi ... done
- Implementare il preferential attachment ... done
- https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
- Implementazione con Netlogo
https://ccl.northwestern.edu/netlogo/models/PreferentialAttachment

### Fase 2: costruzione degli agenti 
- Assegnare lo score agli agenti ... done 
- Definire gli agenti nel file di testo ... done 
- Implementare la verifica dello scale free: ... done 
https://stackoverflow.com/questions/49908014/how-can-i-check-if-a-network-is-scale-free
- Verificare che la rete sia scale free:
https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test

### Fase 3: meccanismi di interazione
- Implementare meccanismo di creazione della news ... done
- Implementare trasferimento della news ... done
- Implementare integrazione della news ... done

### Fase 4: regole della dinamica 
- Associare ad ogni link un certo peso
https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html
- Capire le regole della dinamica da applicare (guardare articolo)

### Fase 5: analisi dati 
- Impostare l'analisi dati: conviene scrivere i dati in un file separato 
https://www.programiz.com/python-programming/writing-csv-files
https://www.w3schools.com/python/python_file_write.asp
