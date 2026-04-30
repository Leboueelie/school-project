#FAIRE LES INSCRIPTIONS
def name() :
    name==input('entrez votre nom:')
    while name==str(input('entrez votre nom:')):
        if  name !=str(input('entrez votre nom:')): 
         print('erreur')
         return(str(name))
        else:
            print('nom enregisre')
#definir le mot de passe utilisateur            
def mot_de_passe():
    mot_de_passe=input('insérer votre mot de pass:')    
    while len(mot_de_passe)==12 :
        if len(mot_de_passe) < 12 :
            print('mot de passe invalide')  
        if len(mot_de_passe)> 12 :
            print('mot de passe errone')
def livres():
    with open('livre.text','r')  as f:
        f.read(livres)            


    
#faire un livre    
def book():
    with open('book.text','r') as f:
        livres=f.read()
        print(livres)
#faire une presentation de bienvenue
def presentation() :
    print('bienvenue{}'.format(name))
#creer un panier pour les livres    
def panier() :
    panier=[] 
    for livre in livres  :
        panier.append(livre)
#ajouter les livres au panier
def ajouter_livre(panier):
    livres = input("ecrivez le nom du livre: ")
    panier.append(livres)
    print("book added!")
    livre = input("nom du livre: ")
    panier.append(livre)
    print("book added!")
# afficher le panier
def affiche_panier(panier):
    if len(panier) == 0:
        print("aucun livre dans le panier!")
    else:
        print("livres:")
        for livres in panier:
            print("-", livres)
# definir le nombre de livre            
def nombre_livre(panier):
    print("nombre de livres:", len(panier))
#sauvegarder le panier    
def sauvegarder_panier(panier):
    with open('panier.txt', 'w') as f:
        for livres in panier:
            f.write(livres + '\n')
    print("basket saved!")
# DATABASE FOR USER REGISTRATION
import sqlite3
from unittest import case

# Create/connect to database
conn = sqlite3.connect('users_db.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
conn.commit()

# Register user in database
def register_user_db(name):
    try:
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        print(f"User {name} ENREGISTRE!")
    except Exception as e:
        print(f"Error: {e}")

# View all registered users
def view_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n--- liste des utilisateurs enregister ---")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}")
    print()
    return users

# Search user by name
def search_user_db(name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()
    if user:
        print(f"Found: Name={user[1]}")
        return user
    else:
        print("Utilisateur non trouves!")
        return None

# Delete user
def delete_user_db(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    print(f"User {name}supprime de la base de donnes !")


# ===================== BOOK RATING SYSTEM =====================

# Create book ratings table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book_ratings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT NOT NULL,
        rating INTEGER NOT NULL,
        user_name TEXT
    )
''')
conn.commit()

# Display stars (golden stars ★)
def display_stars(rating):
    """Display book rating as golden stars"""
    stars = "★" * rating + "☆" * (5 - rating)
    return stars

# notez le livre
def rating_book(book_name, user_name, rating):
    """Add a rating for a book"""
    if rating < 1 or rating > 5:
        print("la note est comprise entre 1  et 5!")
        return
    
    try:
        cursor.execute('''
            INSERT INTO book_ratings (book_name, rating, user_name)
            VALUES (?, ?, ?)
        ''', (book_name, rating, user_name))
        conn.commit()
        print(f"\n'{book_name}' rated {rating} stars by {user_name}")
        print(f"Rating: {display_stars(rating)}\n")
    except Exception as e:
        print(f"Erreur: {e}")

# Get all ratings for a book
def get_book_ratings(book_name):
    """Get all ratings for a specific book"""
    cursor.execute('''
        SELECT book_name, rating, user_name FROM book_ratings
        WHERE book_name = ?
    ''', (book_name,))
    ratings = cursor.fetchall()
    return ratings

# Calculer la moyenne des notes
def calculate_average_rating(book_name):
    """Calculate and display average rating for a book"""
    cursor.execute('''
        SELECT AVG(rating) FROM book_ratings
        WHERE book_name = ?
    ''', (book_name,))
    
    result = cursor.fetchone()
    average = result[0] if result[0] else 0
    
    return round(average, 2)

# montrez les details des notes des livres
def show_all_book_ratings():
    """Display all books with their ratings and averages"""
    cursor.execute("SELECT DISTINCT book_name FROM book_ratings")
    books = cursor.fetchall()
    
    print("\n" + "="*50)
    print("liste des notes")
    print("="*50)
    
    for book in books:
        book_name = book[0]
        avg_rating = calculate_average_rating(book_name)
        ratings = get_book_ratings(book_name)
        
        print(f"\nlivre: {book_name}")
        print(f"note pondere: {avg_rating}/5 {display_stars(int(avg_rating))}")
        print(f"total: {len(ratings)}")
        print("Reviews:")
        for rating in ratings:
            print(f"  - {rating[2]}: {rating[1]} stars {display_stars(rating[1])}")
    
    print("\n" + "="*50 + "\n")

# menu de notation rapide
def rating_menu():
    """Interactive menu for rating books"""
    while True:
        print("\n--- systeme de notation des livres ---")
        print("1. noter un livre")
        print("2. voir les notes des livres")
        print("3. voir tous les livres et les avis")
        print("4. retour au menu principal")
        
        choice = input("choisissez option: ")
        
        if choice == "1":
            book_name = input("entrez le nom du livre: ")
            user_name = input("entrez votre nom: ")
            try:
                rating = int(input("notez le livre (1-5 stars): "))
                rating_book(book_name, user_name, rating)
            except ValueError:
                print("s'il vous plait ,entrez un numero valide!")
        
        elif choice == "2":
            book_name = input("Entrer le nom du livre que vous chercher: ")
            ratings = get_book_ratings(book_name)
            if ratings:
                avg = calculate_average_rating(book_name)
                print(f"\n'{book_name}' Ratings:")
                print(f"Average: {avg}/5 {display_stars(int(avg))}")
                for rating in ratings:
                    print(f"  - {rating[2]}: {rating[1]} ★ {display_stars(rating[1])}")
            else:
                print("pas de notes pour ce livres!")
        
        elif choice == "3":
            show_all_book_ratings()
        
        elif choice == "4":
            break
        
        else:
            print("choix erroné!")
#menu 
def afficher_menu():
    print("\n==== MENU ====")
    print("1.AJOUTER UN LIVRE")
    print("2.AFFICHER LE PANIER")
    print("3.SAUVEGARDER LE PANIER")
    print("4.SORTIE")
    choix=input('choisissez une option (1-4): ')
    if choix=="1":
        ajouter_livre(panier=[])
    elif choix=="2":
        affiche_panier(panier=[])
    elif choix=="3":
        sauvegarder_panier(panier=[])
    elif choix=="4":
        print("a bientot !")
    else:  
        print('choix invalide') 
#AJOUTERUN PRIX        
def  paiement():
    while True:
        print("\n==== paiement  ====")
        print("1.payer")
        print("2.sortie")
        resultat=input('veuiller choisir une option (1-2): ')
        
        if resultat=="1":
         prices=[100,200,300,400]
        for price in prices:
          prices.append()
          prices.append(price)
          prices.append(price=(prices[1] or prices[0] or prices[2] or prices[3]))          
        if resultat=="2":
            print("a bientot !")
            exit()
#lien whatsapp pour payer les abonnements
def payer_taliopay():
    import django.shortcuts.redirect # type: ignore
    import webbrowser
    print("pour payer cliquez sur le lien suivant:") 
    webbrowser.open("je voudrait payer mon abonnement mensuel") 
def retour_client():
    import pandas as pd
    df = pd.DataFrame({
        "nom": [input("nom: ")],
        "book_name": [input("book_name: ")],
        "rating": [input("rating: ")]
                    })
    #create a csv file to save data and build a datatable
    df.to_csv('client_data.csv', index=False)
    


    



    
    

    
    

 






