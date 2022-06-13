# Projekt automatyzacji testów strony internetowej www.demoblaze.com

# TC01: Logowanie
Warunki wstępne: 
1. Otwarta strona główna
2. Użytkownik niezalogowany
Kroki:
1. Kliknij „Log in”
2. Wpisz nazwę użytkownika
3. Wpisz hasło
4. Kliknij przycisk „Log in”
Oczekiwany rezultat:
	Na stronie głównej pojawia się „Log out” gotowy do aktywacji
Warunki końcowe:
	Użytkownik zostaje poprawnie zalogowany

# TC02: Wylogowanie
Warunki wstępne: 
1. Otwarta strona główna
2. Użytkownik zalogowany
Kroki:
1. Kliknij „Log out”
Oczekiwany rezultat:
	Na stronie głównej pojawia się „Log in” gotowy do aktywacji
Warunki końcowe:
	Użytkownik zostaje poprawnie wylogowany

# TC03: Dodawanie produktu do koszyka
Warunki wstępne: 
1. Otwarta strona główna
2. Użytkownik niezalogowany
Kroki:
1. Kliknij „Samsung Galaxy S6”
2. Kliknij „Add to cart”
3. Kliknij „Ok” w popupie
4. Kliknij „Cart”
5. Pobierz nazwę produktu w koszyku
Oczekiwany rezultat:
	Nazwa produktu w koszyku to Samsung Galaxy S6
Warunki końcowe:
	Wybrany produkt został poprawnie dodany do koszyka

# TC04: Usuwanie produktu do koszyka
Warunki wstępne: 
1. Otwarta strona z koszykiem
2. Samsung Galaxy S6 dodany do koszyka
3. Użytkownik niezalogowany
Kroki:
1. Kliknij „Delete”
Oczekiwany rezultat:
	W koszyku nie znajduje się żaden przedmiot
Warunki końcowe:
	Wybrany produkt został poprawnie usunięty z koszyka

# TC05: Zakup produktu
Warunki wstępne: 
1. Otwarta strona z koszykiem
2. W koszyku znajduje się przedmiot
3. Użytkownik niezalogowany
Kroki:
1. Kliknij „Place order”
2. Wpisz imię i nazwisko
3. Wpisz kraj
4. Wpisz miasto
5. Wpisz numer karty kredytowej
3. Wpisz miesiąc
3. Wpisz rok
4. Kliknij przycisk „Purchase”
Oczekiwany rezultat:
	Pojawia się okno z potwierdzniem dokonania zamówienia
Warunki końcowe:
	Wybrane produkty zostały poprawnie zakupione
