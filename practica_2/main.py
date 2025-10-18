
import json
from enum import Enum


class MemoryManager:
    def __init__(self):
        self.heap_allocations = 0
        self.heap_deallocations = 0
        self.records = {}

    def allocate(self, obj):
        pointer = id(obj)
        self.records[pointer] = type(obj).__name__
        self.heap_allocations += 1
        print(f"[HEAP] Asignado: {type(obj).__name__} (id={pointer})")

    def deallocate(self, obj):
        pointer = id(obj)
        if pointer in self.records:
            del self.records[pointer]
            self.heap_deallocations += 1
            print(f"[HEAP] Liberado: id={pointer}")

    def display_memory_usage(self):
        print("\n---------------- MEMORIA ----------------")
        print(f"Asignaciones: {self.heap_allocations}")
        print(f"Liberaciones: {self.heap_deallocations}")
        print("------------------------------------------")
        if self.records:
            print("Objetos vivos:")
            for ptr, typename in self.records.items():
                print(f" - {typename} (id={ptr})")
        else:
            print("No hay objetos en memoria heap.")
        print("------------------------------------------\n")

class Genre(Enum):
    FICTION = 0
    NON_FICTION = 1
    SCIENCE = 2
    HISTORY = 3
    FANTASY = 4
    BIOGRAPHY = 5
    OTHER = 6

    @staticmethod
    def from_string(s: str):
        mapping = {
            "Ficcion": Genre.FICTION,
            "No Ficcion": Genre.NON_FICTION,
            "Ciencia": Genre.SCIENCE,
            "Historia": Genre.HISTORY,
            "Fantasia": Genre.FANTASY,
            "Biografia": Genre.BIOGRAPHY,
            "Otro": Genre.OTHER
        }
        return mapping.get(s, Genre.OTHER)

    def __str__(self):
        names = {
            Genre.FICTION: "Ficcion",
            Genre.NON_FICTION: "No Ficcion",
            Genre.SCIENCE: "Ciencia",
            Genre.HISTORY: "Historia",
            Genre.FANTASY: "Fantasia",
            Genre.BIOGRAPHY: "Biografia",
            Genre.OTHER: "Otro"
        }
        return names[self]


# =====================================================
# Clase Book
# =====================================================
class Book:
    def __init__(self, book_id, title, author, year, genre, quantity):
        self.id = book_id
        self.title = title
        self.author = author
        self.publication_year = year
        self.genre = genre
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "genre": str(self.genre),
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["id"],
            data["title"],
            data["author"],
            data["publication_year"],
            Genre.from_string(data["genre"]),
            data["quantity"]
        )


# =====================================================
# Clase Member
# =====================================================
class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name
        self.issued_books = []

    def issue_book(self, book_id):
        self.issued_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.issued_books:
            self.issued_books.remove(book_id)
            return True
        return False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "issued_books": self.issued_books
        }

    @staticmethod
    def from_dict(data):
        m = Member(data["id"], data["name"])
        m.issued_books = data.get("issued_books", [])
        return m


# =====================================================
# Clase principal LibrarySystem
# =====================================================
class LibrarySystem:
    def __init__(self):
        self.library = []
        self.members = []
        self.mem_manager = MemoryManager()

    # -----------------------------------------------
    # Métodos de gestión de libros
    # -----------------------------------------------
    def add_book(self):
        print("\n--- Agregar libro ---")
        book_id = int(input("ID del libro: "))
        title = input("Título: ")
        author = input("Autor: ")
        year = int(input("Año de publicación: "))
        genre = Genre(int(input("Género (0:Ficción, 1:No Ficción, 2:Ciencia, 3:Historia, 4:Fantasia, 5:Biografía, 6:Otro): ")))
        quantity = int(input("Cantidad: "))

        book = Book(book_id, title, author, year, genre, quantity)
        self.library.append(book)
        self.mem_manager.allocate(book)
        print("✅ Libro agregado correctamente.")
        self.mem_manager.display_memory_usage()

    def find_book(self, book_id):
        for book in self.library:
            if book.id == book_id:
                return book
        return None

    def display_books(self):
        if not self.library:
            print("No hay libros en la biblioteca.")
            return
        print("\n--- Libros disponibles ---")
        for book in self.library:
            print(f"ID: {book.id} | Título: {book.title} | Autor: {book.author} | Año: {book.publication_year} | "
                  f"Género: {book.genre} | Cantidad: {book.quantity}")
        self.mem_manager.display_memory_usage()

    # -----------------------------------------------
    # Métodos de gestión de miembros
    # -----------------------------------------------
    def add_member(self):
        print("\n--- Agregar miembro ---")
        member_id = int(input("ID del miembro: "))
        name = input("Nombre: ")
        member = Member(member_id, name)
        self.members.append(member)
        self.mem_manager.allocate(member)
        print("✅ Miembro agregado correctamente.")
        self.mem_manager.display_memory_usage()

    def display_members(self):
        if not self.members:
            print("No hay miembros registrados.")
            return
        print("\n--- Miembros registrados ---")
        for m in self.members:
            print(f"ID: {m.id} | Nombre: {m.name} | Libros prestados: {len(m.issued_books)}")
            for bid in m.issued_books:
                book = self.find_book(bid)
                if book:
                    print(f"   - {book.title} ({book.author})")
        self.mem_manager.display_memory_usage()

    # -----------------------------------------------
    # Prestamos y devoluciones
    # -----------------------------------------------
    def issue_book(self):
        member_id = int(input("ID del miembro: "))
        book_id = int(input("ID del libro: "))
        member = next((m for m in self.members if m.id == member_id), None)
        book = self.find_book(book_id)
        if not member or not book:
            print("❌ Miembro o libro no encontrado.")
            return
        if book.quantity <= 0:
            print("❌ No hay ejemplares disponibles.")
            return
        book.quantity -= 1
        member.issue_book(book_id)
        print(f"📚 Libro '{book.title}' prestado a {member.name}.")
        self.mem_manager.display_memory_usage()

    def return_book(self):
        member_id = int(input("ID del miembro: "))
        book_id = int(input("ID del libro: "))
        member = next((m for m in self.members if m.id == member_id), None)
        book = self.find_book(book_id)
        if not member or not book:
            print("❌ Miembro o libro no encontrado.")
            return
        if member.return_book(book_id):
            book.quantity += 1
            print(f"✅ Libro '{book.title}' devuelto correctamente.")
        else:
            print("⚠️ El miembro no tenía este libro prestado.")
        self.mem_manager.display_memory_usage()

    # -----------------------------------------------
    # Guardar / cargar datos en JSON
    # -----------------------------------------------
    def save_data(self):
        with open("library.json", "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.library], f, indent=4, ensure_ascii=False)
        with open("members.json", "w", encoding="utf-8") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=4, ensure_ascii=False)
        print("💾 Datos guardados correctamente.")

    def load_data(self):
        try:
            with open("library.json", "r", encoding="utf-8") as f:
                self.library = [Book.from_dict(b) for b in json.load(f)]
            with open("members.json", "r", encoding="utf-8") as f:
                self.members = [Member.from_dict(m) for m in json.load(f)]
            print("📂 Datos cargados correctamente.")
        except FileNotFoundError:
            print("⚠️ Archivos de datos no encontrados, se iniciará una nueva biblioteca.")

    # -----------------------------------------------
    # Cerrar programa
    # -----------------------------------------------
    def exit(self):
        self.save_data()
        for b in self.library:
            self.mem_manager.deallocate(b)
        for m in self.members:
            self.mem_manager.deallocate(m)
        self.mem_manager.display_memory_usage()
        print("👋 Saliendo del sistema. ¡Hasta luego!")


# =====================================================
# Programa principal
# =====================================================
if __name__ == "__main__":
    system = LibrarySystem()
    system.load_data()

    while True:
        print("\n===== Sistema de Biblioteca =====")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Agregar miembro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar miembros")
        print("7. Guardar y salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            system.add_book()
        elif choice == "2":
            system.display_books()
        elif choice == "3":
            system.add_member()
        elif choice == "4":
            system.issue_book()
        elif choice == "5":
            system.return_book()
        elif choice == "6":
            system.display_members()
        elif choice == "7":
            system.exit()
            break
        else:
            print("Opción inválida.")
