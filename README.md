#### Riak

##### Instalacja

```buildoutcfg
$ git clone https://github.com/olechanastazja/riak_app.git

$ cd riak_app

$ virtualenv -p python3 venv/

$ source venv/bin/activate

$ pip install -r requirements.txt
```

Aby uruchomić riaka w kontenerze:
```buildoutcfg
# docker build -t  "<yourname>/riak" .

# docker run "<yourname>/riak"
```

Dane, które zostaną dodane znajdują się w pliku `data.json`.

W `config.ini` znajduje się konfiguracja (host i port) za pomocą której skrypt łączy się z bazą.

##### Użycie

```
$ python3 main.py [klucz]
```


Klucz jest opcjonalny. Można go dodać jeśli chcemy mieć własną wartość.

Aby zapisać wynik działania programu do pliku skrypt należy wywołać w następujący sposób:
```
$ python3 main.py [klucz] >> komunikaty.txt
```
