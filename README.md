# Fake-news
Stiamo realizzando un modello ad agenti in SLAPP, per simulare la diffusione di fake news su Twitter, nello scenario delle presidenziali 
USA del 2016.

![alt text](https://dynaimage.cdn.cnn.com/cnn/q_auto,h_600/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F180126190057-08-white-house-mueller-denial-quotes-restricted.jpg)

## Il modello
I nodi rappresentano gli agenti, cioè gli account twitter.
I link rappresentano i retweet, cioè il nodo A è connesso al nodo B, se l'account A ha retwettato un tweet dell'account B.
1. Si parte da un network random, scale free e diretto, con un numero fissato di nodi.
2. Si impostano le regole della dinamica.
3. Si valuta l'evoluzione del network nel tempo. 
4. Analisi dei dati. 

## Dataset sul network di retweet 
Per quanto riguarda i dati e le regole della dinamica, ci basiamo sul seguente [paper](https://www.nature.com/articles/s41467-018-07761-2) consultabile gratuitamente. 
Vorremmo arrivare a riprodurre i seguenti [risultati](https://www.nature.com/articles/s41467-018-07761-2/tables/2)

## Sviluppo
### Fase 1: costruzione della rete ... completata
- Costruire i nodi ... done
- Implementare il preferential attachment ... done
- [Forest Fire](https://arxiv.org/pdf/physics/0603229.pdf)
- [Forest Fire Algorithm](http://snap.stanford.edu/snappy/doc/reference/GenForestFire.html)
- [Modello](https://ccl.northwestern.edu/netlogo/models/PreferentialAttachment) in Netlogo

### Fase 2: costruzione degli agenti 
- Assegnare lo score agli agenti ... done 
- Definire gli agenti nel file di testo ... done 
- Implementare la verifica dello scale free: ... done 
[Verificare che un network sia scale free](https://stackoverflow.com/questions/49908014/how-can-i-check-if-a-network-is-scale-free)
- Verificare che la rete sia scale free:
[Kolmogorov Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)

### Fase 3: meccanismi di interazione
- Implementare meccanismo di creazione della news ... done
- Implementare trasferimento della news ... done
- Implementare integrazione della news ... done

### Fase 4: regole della dinamica 
- Associare ad ogni link un certo peso
[Network pesati](https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_weighted_graph.html)
-[Regole della dinamica](https://docs.google.com/document/d/1kIeEAsEj68Kzrlez-EyenRuGMm5y2Hc0zdkFIFzppUE/edit?usp=sharing):
  - Creazione bot ... done 
  - Meccanismi di interazione bot ... done
  - Creare gli agenti (con i diversi score) rispettando le [proporzioni](https://docs.google.com/spreadsheets/d/12tik2m_w-y7LoZE5tSWOoTFDNzIT6hjsoO4Oaqabnoc/edit#gid=0) indicate in tabella
  - Frequenza di creazione delle news rispettando le proporzioni ... done

### Fase 5: analisi dati 
- Impostare l'analisi dati: conviene scrivere i dati in un file separato 
[Scrivere un file csv](https://www.programiz.com/python-programming/writing-csv-file)
[Scrivere un file da python](https://www.w3schools.com/python/python_file_write.asp)
- Network Analysis: 
[Power law fitting](https://github.com/micheletizzoni/Complexity-in-social-systems/blob/master/2-networkx/nb04_powerlaw_fitting.ipynb) //
[Clustering](https://github.com/micheletizzoni/Complexity-in-social-systems/blob/master/2-networkx/nb05_network_analysis.ipynb)
//[Barabasi power law fitting](https://barabasi.com/f/623.pdf) vedere pagina 44. 

## Run it online with Binder
[Binder](https://mybinder.org/v2/gh/alessandrotofani/Fake-news/snap?filepath=iRunShellOnline.ipynb)

## Useful links
[md file cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Un'altra immagine su Trump, why not?
![alt text](https://images.axios.com/YWMPTIF_Za_LAeU4cHUJwxe1R0M=/1920x1080/smart/2017/12/15/1513303959471.png)
