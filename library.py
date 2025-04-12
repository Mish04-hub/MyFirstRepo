import time

# List of available books in the library
library_books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction"},
    {"title": "Harry Potter Series", "author": "J.K. Rowling", "genre": "Fantasy"},
    {"title": "Interstellar", "author": "Christopher Nolan", "genre": "Sci-Fi"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "genre": "Thriller"},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Thriller"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "Twisted Love", "author": "Ana Huang", "genre": "Romance"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help"},
    {"title": "It Ends With Us", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Finance"},
]

users = {}
current_user = None
cart = []
borrowed_books = []
MAX_BORROW = 2

# User registration function
def register():
    global current_user
    print("\nRegister New Account")
    name = input("Name: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    users[username] = {"name": name, "password": password}
    print("\n **** Registration successful! ****")
    current_user = username
    return True

# User login function
def login():
    global current_user
    print("\nLogin")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username]['password'] == password:
        print(f"Welcome back, {users[username]['name']}!")
        current_user = username
        return True
    else:
        print("Invalid credentials.")
        return False
    
# Search for books by title, author, or genre
def search_books(keyword):
    results = [book for book in library_books if keyword in book['title'].lower()
               or keyword in book['author'].lower()
               or keyword in book['genre'].lower()]
    if results:
        print("\nBooks Found:")
        for book in results:
            print(f"- {book['title']} by {book['author']} [{book['genre']}]")
    else:
        print("No matching books found.")
    return results

# Add a book to the cart by matching the title
def add_book_by_title(title_input):
    for book in library_books:
        if book['title'].lower() == title_input.lower():
            if book in cart:
                print("Already in cart.")
            else:
                cart.append(book)
                print(f"'{book['title']}' added to cart.")
            return
    print("Book not found. Please try the exact title shown in search results.")

# Display the current cart contents
def view_cart():
    print("\nYour Cart:")
    if cart:
        for book in cart:
            print(f"- {book['title']} by {book['author']}")
    else:
        print("Your cart is empty.")

# Borrow books from the cart and process mock payment
def borrow_books():
    global borrowed_books
    if not cart:
        print("Your cart is empty.")
        return

    if len(borrowed_books) + len(cart) > MAX_BORROW:
        print(f"You can only borrow {MAX_BORROW} books in total.")
        return

    total_cost = len(cart) * 5  # $5 per book
    print(f"\nYou are borrowing {len(cart)} books.")
    print(f"Total cost: ${total_cost}.00")
    confirm = input("Proceed with payment? (yes/no): ").strip().lower()

    if confirm == 'yes':
        print("Processing payment...")
        time.sleep(1)
        print("Payment successful!")

        borrowed_books.extend(cart)
        for book in cart:
            print(f"Borrowed: {book['title']} by {book['author']}")
        cart.clear()
    else:
        print("Payment cancelled. Returning to menu.")


# Generate a report of all borrowed books
def generate_report():
    print("\nBorrowing Report:")
    if borrowed_books:
        for book in borrowed_books:
            print(f"- {book['title']} by {book['author']} [{book['genre']}]")
    else:
        print("No books borrowed yet.")

# Display the main library menu for logged-in users
def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("\n 1. Search Books")
        print(" 2. View Cart")
        print(" 3. Borrow Books")
        print(" 4. Generate Report")
        print(" 5. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            keyword = input("Enter keyword (title/author/genre): ").strip().lower()
            results = search_books(keyword)
            if results:
                while True:
                    book_title = input("\nEnter exact book title to add to cart (or 'back' to return): ").strip()
                    if book_title.lower() == 'back':
                        break
                    add_book_by_title(book_title)
        elif choice == '2':
            view_cart()
        elif choice == '3':
            borrow_books()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

# Main program
def main():
    print("\n******** Welcome to the Library Application ********")
    while True:
        print("\n 1. Register\n 2. Login\n 3. Exit")
        choice = input("\nChoose an option: ").strip()
        if choice == '1':
            if register():
                library_menu()
        elif choice == '2':
            if login():
                library_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
