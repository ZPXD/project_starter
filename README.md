## ZPXD Project Starter

Skrytpy dzięki któremu szybko postawisz projekt na serwerze (dostępny dla przeglądarek).

```
# Unite the clans

su root
wget https://raw.githubusercontent.com/ZPXD/project_starter/main/scripts/project_starter.sh 
# przerwa na edycję pliku - patrz opis na dole.
bash project_starter.sh $domena $project_name $project_user $project_repo
```

Twoja strona będzie widoczna pod Twoją domeną.

Wszystkie pliki aplikacji znajdą się w folderze `/var/www/app_name`

**Wymagania:**
1. Czysty (nowy, bez niczego innego) Serwer Linux Ubuntu 18/20 bez podpiętej domeny z dostępem do root.
2. Domena połączona z Twoim Serwerem
3. Repozytorium z projektem zaprogramowanym we Flasku w stylu `app_name/app.py` z `requirements.txt`
4. Przypisanie wartości - napisz w terminalu:


```
domena=    [tu wpisz nazwę Twojej domeny bez www. ]
project_name=what_what    [projekt nazywa się tak jak Twoje repozytorium]
project_user=root # change it
project_repo=https://github.com/ZPXD/what_what.git # git z repo projektu
```
