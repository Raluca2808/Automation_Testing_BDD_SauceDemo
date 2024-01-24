* The structure of a BDD framework:

     1. Folder features= Feature files - It contains files written in a more natural language (gherkin) to describe business scenarios
        * Given (the context in which the action takes place)
        * When (the action we do)
        * Then (the denouement - the check we want to do)
     2. Folder steps = Step definition files - technical mapping of business files - feature files
     3. Folder pages = Mapping pages for browser elements (POM -page object model)
        - We will have files for each web page of the application
        - base_page file - is a class that contains methods that can be used in several classes, which are useful for all pages
     4. File browser - contains installation and browser opening instructions
     5. File environment - contains the instantiation of all classes of type pages

* Work methodologies:
    1. Waterfall:
        - strict
        - any necessary modification after the start of the project will have to be implemented in a new project
        - it is planned at the beginning, then it is developed, then it is tested and then it is put on the market
        - product feedback from customers is received late, at the end
        - usually a lot of functionality is developed
    2. Agile:
        - less strict, flexible and organized
        - any change that occurs during implementation can be changed along the way
        - work is done in sprints (usually 2-week cycles)
        - in a sprint it is planned, developed, tested and released to the market (to the client)
        - the feedback for the product to the customers is received after each sprint and can be implemented in the following sprints
        - *(Scrum and Kanban, Scrumban)
    
Functionalities can be grouped as follows:
1. Epic -> major components (ex: shopping page)
2. Story -> independent functionalities from the same component (add to cart, filters, etc.)

User story:
As a customer I want to view all electronics products.
As a customer I want to add a product to my shopping cart.
As a {user} I want to {action} *(so that i can {reason}).

Command: behave -f html -o behave_raport.html --tags=smoke