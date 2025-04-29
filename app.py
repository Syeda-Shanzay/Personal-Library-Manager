import json
import os

# Path to the file where the library data is stored
data = "library.txt"

# Save library to file
def save_library(library):
    ## Open the file in write mode and save the library data as JSON
    with open(data, "w") as file:
        json.dump(library, file)

# Load library from file
def load_library():
    # Check if the file exists before trying to load
    if os.path.exists(data):
        with open(data, "r") as file:
            # Read and return the JSON data as a Python list
            return json.load(file)
    # If the file doesn't exist, return an empty list    
    return []

# Add a book
def add_books(library):
    # Collect book details from user input
    title= input("Enter the book title: ")
    author = input("Enter the author: ")
    publication_year = input("Enter the publication year: ")
    genre: str = input("Enter the genre: ")
    # Convert read status to a boolean (True if yes, False if no)
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    # Create a dictionary representing the new book
    add_new_book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status
    }
    # Add the new book to the library list
    library.append(add_new_book)
    # Save the updated library to file
    save_library(library)
    print(f"Book '{title}' added successfully!")

# Remove a book
def remove_book(library):
    # Ask user for the title of the book to remove
    title= input("Enter the title of the book to remove: ")
    # Search for the book in the library
    for book in library:
        if book['title'].lower() == title.lower():
            # If found, remove it and save the updated library
            library.remove(book)
            save_library(library)
            print(f"Book '{title}' removed successfully!")
            return
    # If not found, show a message    
    print("Book not found.")

# Search books
def searching_book(library):
    # Ask whether to search by title or author
    searching_by = input("Search by 'title' or 'author': ").lower()
    if searching_by not in ["title", "author"]:
        print("Invalid search field. Choose 'title' or 'author'.")
        return
    # Get the search term from user
    searching_terms = input(f"Enter the {searching_by}: ").lower()
    # Filter books that contain the search term
    result = [book for book in library if searching_terms in book[searching_by].lower()]
    # Display results
    if result:
        for book in result:
            status = "Read" if book["read_status"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['publication_year']} - {book['genre']} - {status}")
    else:
        print(f"No book found matching '{searching_terms}' in the {searching_by} field.")

# Display all books
def display_all_book(library):
    # Check if library is not empty
    if library:
        for book in library:
            status = "Read" if book["read_status"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['publication_year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

# Display statistics
def disply_statistic(library):
    # Calculate totals
    total_books = len(library)
    read_books = len([book for book in library if book['read_status']])
    # Avoid division by zero
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    # Print statistics
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Main menu
def main():
    # Load library from file when program starts
    library = load_library()
    # Display menu options
    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        # Get user input
        choice:str = input("Enter your choice: ")
        if choice == "1":
            add_books(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            searching_book(library)
        elif choice == "4":
            display_all_book(library)
        elif choice == "5":
            disply_statistic(library)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the main program
if __name__ == '__main__':
    main()