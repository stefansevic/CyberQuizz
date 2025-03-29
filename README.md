CyberQuizz - Kviz za praćenje napretka u učenju
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*******************
* Opis aplikacije *
*******************

CyberQuizz je aplikacija koja omogućava praćenje napretka u učenju kroz kreiranje i upravljanje kvizovima. U aplikaciji se beleže chapter-i i subchapter-i naučenog iz knjiga, kurseva ili drugih materijala dostupnih za učenje. Konkretno, ova aplikacija je korišćena za praćenje napretka i obnavljanje naučenog iz knjige Sigurnost računarskih sistema i mreža.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Aplikacija se sastoji od četiri glavne klase:

main.py: Srž i logika celog projekta. Služi za izvršavanje kviza i obradom podataka.

database.py: Povezivanje sa bazom podataka i njeno kreiranje.

add_questions.py: Skripta za dodavanje pitanja, odgovora, chapter-a i subchapter-a u kviz.

quiz_ui.py: Dizajn i korisnički interfejs aplikacije.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*****************************
* Kako koristiti aplikaciju *
*****************************

1. Način - Korisćenje podataka iz moje baze vezane za knjigu Sigurnost računarskih sistema i mreža:
   
- Otvorite database_dump.sql i izvršite SQL komande iz dump fajla kako bi se kreirala baza sa svim potrebnim podacima.

- Pokrenite klasu database.py kako biste povezali aplikaciju sa bazom podataka.

- (Opcionalno) Dodajte dodatna pitanja, odgovore, chapter-e i subchapter-e koristeći klasu add_questions.py i izvršite je.

- Pokrenite klasu main.py kako biste započeli kviz.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Način - Pravite vaš sopstveni kviz po mom šablonu:
   
- Pokrenite klasu database.py kako biste kreirali i povezali aplikaciju sa bazom podataka.

- (Opcionalno) Dodajte pitanja, odgovore, chapter-e i subchapter-e koristeći klasu add_questions.py i izvršite je.

- Pokrenite klasu main.py kako biste započeli svoj kviz.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

***************
* INSTALACIJA *
***************


- Klonirajte ovaj repozitorijum:

git clone https://github.com/stefansevic/CyberQuizz.git

- Instalirajte potrebne pakete (ako koristite virtuelno okruženje):

pip install -r requirements.txt

Postavite i povežite bazu podataka prema uputstvu.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Autori:

Stefan Sević - Autor aplikacije.
