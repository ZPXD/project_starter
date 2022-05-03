## ZPXD Project Starter

Skrytpy dzięki któremu szybko postawisz projekt na serwerze (przeczytaj wymagania). 

```
# Unite the clans

su root
wget https://raw.githubusercontent.com/ZPXD/project_starter/main/scripts/project_starter.sh 
# przerwa na edycję pliku - patrz opis na dole.
bash project_starter.sh $domena $project_name $project_user $project_repo
```
Wszystkie pliki aplikacji znajdą się w folderze `/var/www/app_name`

Połączysz się z projektem swojej przeglądarki np. po tunelu, wpisz w `terminalu/powershellu` u siebie na komputerze: 
```
ssh -L 5000:localhost:80 -i klucz username@1.1.1.1 # <-------- EDYTUJ username i ip :)
```


**Wymagania:**
1. Czysty (nowy, bez niczego innego) Serwer Linux Ubuntu 18/20 bez podpiętej domeny z dostępem do root.
2. Domena połączona z Twoim Serwerem, jeżeli projekt ma być widoczny dla przeglądarek.
3. Repozytorium z projektem zaprogramowanym we Flasku w stylu `app_name/app.py` z `requirements.txt`.
4. Przypisanie wartości - napisz w terminalu:

```
domena=     # [tu wpisz nazwę Twojej domeny bez www. ]
project_name=what_what     # [projekt nazywa się tak jak Twoje repozytorium]
project_user=root # [raczej zmien na uzytkownika]
project_repo=https://github.com/ZPXD/what_what.git # git z repo projektu
```

**Aby projekt był dostępny dla przeglądarek:**

Usuń w `/var/www/<app_name>/app.py` w ostatniej linii `localhost`.

Twoja strona będzie widoczna pod Twoją domeną.


