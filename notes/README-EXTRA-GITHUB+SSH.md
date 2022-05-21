## Github poprzez autoryzacje za pomocą SSH

Działa z MacO i Linux.

UWAGA: W wielu miejscach podanych koment trzeba wstawić własne dane jak: adres email, imię i nazwisko, nazwę konta na GitHub, nazwę respozytorium.

#### 1) Tworzymy klucze SSH, konfigurujemy SSH i dodajemy klucz publiczny do GitHub

Wydajemy komendy

```
cd .ssh
ssh-keygen -t ed25519 -C "twoj_email@domena.pl"
```

Zatwierdzamy nazwę pliku bez zmiany ich nazwy.

Przy pytaniu o `passphare` podajecie hasło do klucza, albo jeśli jesteście całkowicie początkujący naciskacie ENTER

Edytujemy plik `~/.ssh/config` i doprowadzamy go do wyglądu

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

W przypadku jeśli chcemy bardziej zaawansowanej konfiguracji i używania wielu różnych kluczy to doprowadzamy plik do wyglądu

```
Host *
  AddKeysToAgent yes
  UseKeychain yes

Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
```

Wrzucamy czawartość pliku `~/.ssh/id_ed25519.pub` do ustawień własnego profilu na GitHub -> ścieżka postępowania:

klikamy w Menu Górne obok ikony awarata -> "Settings" -> "SSH and GPG keys" -> klikamy w przycisk "New SSH key" -> wypełniamy pole "Title" własną nazwę, a w pole "Key" wklejamy zawartość pliku `~/.ssh/id_ed25519.pub` i klikamy przycisk "Add SSH key".

Teraz zweryfikujmy czy wszystko działa.

Wydajemy komendę
`ssh -T git@github.com`

Przy poprawności wcześniejszych kroków otrzymamy komunikat:
`Hi Nazwa_konta-GitHub! You've successfully authenticated, but GitHub does not provide shell access.`

Mogą się pojawić pewne błędy, na przykład `Bad configuration option: usekeychain`.
Nalezy wtedy do pliku `~/ssh/config` dodać do sekcji z `Host *` wpis w nowej linijce `IgnoreUnknown UseKeychain`.

#### 2) Konfigurujemy dostęp po SSH dla wybranego projektu.

UWAGA: Zakładam, że masz już pobraną zawartość poleceniem `git clone` lub nawet skonfigurowany dostęp po HTTPS.

Przechodzimy do katalogu projektu, który chcemy synchronizować z GitHub.

Wydajemy komendę:

```
git remote set-url origin git@github.com:Nazwa_Uzytkownika/Nazwa_Projektu.git
```

W przypadku, kiedy nie mieliśmy wczęśniej skonfigurowanego dostępu po HTTPS proponuje wydac dodatkowo komendy.

```
git config --global user.email "twoj_email@domena.pl"
git config --global user.name "Imię i Nazwisko"
git config pull.rebase false
```

Potwierdzamy działanie poprzez komendy:
`git pull`
oraz
`git-push`
