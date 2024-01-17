* Structura unui framework BDD:

     1. Folder features= Feature files - Contine fisiere scrise intr-un limbaj mai natural (gherkin) care sa descrie scenariile de business
        * Given (contextul in care se desfasoara actiunea)
        * When (actiunea pe care o facem)
        * Then (deznodamantul - verificarea pe care vrem sa o facem)
     2. Folder steps = Step definition files - maparea tehnica a fisierelor de business - feature files
     3. Folder pages = Pagini de mapare pentru elementele din browser (POM -page object model)
        - Vom avea fisiere pentru fiecare pagina web a aplicatiei
        - base_page file - este o clasa ce contine metode care pot fi folosite in mai multe clase, adica care sunt utile pentru toate paginile
     4. Fisier browser - contine instrunctiuni de instalare si deschidere browser
     5. Fisier environment - contine instantierea tuturor claselor de tip pages

* Metodologii de lucru:
    1. Waterfall:
        - stricta
        - orice modificare necesara dupa inceperea proiectului va trebui implementata intr-un proiect nou
        - se planuieste tot la inceput, apoi se dezvolta, apoi se testeaza si apoi se da in piata
        - feedback-ul pentru produs de la clienti se primeste tarziu,la final
        - de regula se dezvolta multa functionalitate
    2. Agile:
        - mai putin stricta, este flexibila si organizata
        - orice modificare aparuta in timpul implementarii, se poate modifica pe parcurs
        - se lucreaza in sprint-uri (de regula cicluri de 2 saptamani)
        - intr-un sprint se planifica, se dezolta, se testeaza si se da in piata (clientului)
        - feedback-ul pentru produs se la clienti se primeste dupa fiecare sprint si se poate implementa in urmatoarele sprint-uri
        - *(Scrum si Kanban, Scrumban)
    
Functionalitatile se pot grupa in felul urmator:
1. Epic -> componente majore (ex: pagina de cumparaturi)
2. Story -> functionalitati independente din aceeasi componenta(adaugarea in cos ,filtre,etc.)

User story:
As a customer I want to view all electronics products.
As a customer I want to add a product to my shopping cart.
As a {user} I want to {action} *(so that i can {reason}).

Comanda: behave -f html -o behave_raport.html --tags=smoke