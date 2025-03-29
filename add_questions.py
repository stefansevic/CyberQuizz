import random
from database import Database

def add_questions():
    db = Database()
    db.create_database()

    chapter = "Sigurnosni protokoli"
    subchapter = "IPSec"

    questions = [
    ("Koja je osnovna funkcija IPSec protokola?", "Omogućavanje sigurne komunikacije preko nesigurnih mreža", "Povećanje brzine prenosa podataka", "Skladištenje enkriptovanih lozinki", "Autentifikacija korisnika na serveru", 1),
    
    ("Gde se najčešće koristi IPSec?", "VPN veze i zaštita IP komunikacije", "Web šifrovanje", "Lokalna autentifikacija korisnika", "Šifrovanje email poruka", 1),
    
    ("Šta znači kada IPSec radi u transportnom režimu?", "Štiti samo podatke, ne i IP zaglavlje", "Šifruje ceo IP paket", "Koristi se samo za interne mreže", "Radi samo na bežičnim konekcijama", 1),
    
    ("Koji režim IPSec protokola se koristi za VPN tunelovanje?", "Tunelski režim", "Transportni režim", "SSH mod", "Hybrid režim", 1),
    
    ("Koja je glavna razlika između AH i ESP protokola u IPSec-u?", "ESP obezbeđuje šifrovanje podataka, dok AH samo autentifikaciju", "AH koristi jače šifrovanje od ESP-a", "ESP radi na aplikativnom sloju, dok AH radi na mrežnom sloju", "AH se koristi samo u transportnom režimu, dok ESP radi samo u tunelskom", 1),
    
    ("Koji je nedostatak IPSec-a u odnosu na SSL VPN?", "Kompleksnija implementacija i veći zahtevi resursa", "Slabija enkripcija", "Veća latencija", "Manja kompatibilnost sa mobilnim uređajima", 1),
    
    ("U kojoj situaciji bi IPSec bio bolji izbor od SSL-a?", "Za zaštitu celokupnog saobraćaja između mreža", "Za sigurnu razmenu poruka preko web pretraživača", "Za autentifikaciju korisnika u online sistemima", "Za zaštitu fajlova na lokalnom disku", 1),
    
    ("Koji protokol IPSec-a se koristi za integritet i autentifikaciju podataka?", "AH (Authentication Header)", "ESP (Encapsulating Security Payload)", "TLS", "SSH", 1),
    
    ("Šta omogućava ESP protokol u okviru IPSec-a?", "Šifrovanje i autentifikaciju paketa", "Samo autentifikaciju paketa", "Komunikaciju između IoT uređaja", "Distribuciju enkripcijskih ključeva", 1),
    
    ("Koji sloj OSI modela koristi IPSec?", "Mrežni sloj", "Transportni sloj", "Sloj aplikacije", "Fizički sloj", 1),
    
    ("Koji su izazovi pri implementaciji IPSec-a?", "Kompleksnost konfiguracije i visok zahtev resursa", "Nedostatak podrške za mobilne uređaje", "Slaba otpornost na MITM napade", "Zahtev za fizičkom autentifikacijom korisnika", 1),
    
    ("Koja je uloga IKE (Internet Key Exchange) protokola u IPSec-u?", "Omogućava sigurno razmenjivanje ključeva", "Šifruje poruke između klijenta i servera", "Optimizuje mrežni saobraćaj", "Validira korisničke lozinke", 1),
    
    ("Koja metoda se koristi za autentifikaciju u IPSec protokolima?", "Pre-shared keys ili digitalni sertifikati", "Biometrijska verifikacija", "Jednokratne lozinke", "Korišćenje privatnih IP adresa", 1),
    
    ("Kako IPSec osigurava integritet podataka?", "Koristi hash funkcije i digitalne potpise", "Kriptuje svaki paket pojedinačno", "Menja IP adrese u realnom vremenu", "Automatski menja lozinke korisnika", 1),
    
    ("Koji je podrazumevani port za IPSec VPN?", "500 (IKE)", "22", "443", "80", 1)
]





    for question in questions:
        question_text, *options, correct_option = question
        correct_answer = options[correct_option - 1]  
        random.shuffle(options)
        new_correct_option = options.index(correct_answer) + 1  

        question_data = (question_text, *options, new_correct_option, chapter, subchapter)
        try:
            db.add_question(question_data)
        except Exception as e:
            print(f"Došlo je do greške pri dodavanju pitanja: {e}")

if __name__ == "__main__":
    add_questions()
