
# 📘 Práctica 1  
# Análisis de Componentes en C

![logofiad](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-knUh2CHxFrAZzLM7pXkcL8nodRXAoP0b2Q&s)


## 1. 🏷️ Nombres
- **Ejemplos de variables:** `library`, `members`, `bookCount`, `memberCount`
- **Ejemplos de funciones:** `addBook`, `displayBooks`, `issueBook`, `returnBook`
- **Ejemplos de tipos definidos:** `book_t`, `member_t`, `genre_t`

> Los nombres identifican entidades en el programa y hacen que el código sea legible.

---

## 2. 🧠 Marcos de activación
- Cada vez que se llama una función como `addBook(&library, &bookCount)`, el compilador crea un marco en el stack con:
  - Parámetros: `book_t **library`, `int *count`
  - Variables locales: `book_t *new_book`
- Cuando la función termina, el marco se destruye y el control regresa al `main`.

> Ejemplo: cada llamada a `addBook` crea un marco que vive hasta que la función regresa.

---

## 3. 📦 Bloques de alcance (scope)
- **Globales:** `bss_var`, `static_var`, funciones y estructuras como `book_t`, `member_t`
- **Locales (main):** `int choice`, `bookCount`, `memberCount`
- **De bloque (issueBook):** `bookFound`, `memberFound` (solo existen dentro de esa función)

---

## 4. 🧮 Administración de memoria
- **Heap:**
  - `malloc` y `realloc` asignan memoria
  - Ejemplo: `book_t *new_book = (book_t *)malloc(sizeof(book_t));`
  - `free` libera memoria (`freeLibrary`, `freeMembers`)
- **Stack:** variables automáticas como `int choice` en `main`
- **Globales:** `bss_var`, `static_var`

---

## 5. 🧩 Expresiones
- **Aritméticas:** `memberFound->issued_count++`, `bookFound->quantity--`
- **Lógicas:** `if (current_book->id == bookID && current_book->quantity > 0)`
- **Relacionales:** `if (current_member->id == memberID)`

---

## 6. 🧾 Comandos
- **Secuencia:** `printf`, `scanf`, asignaciones
- **Condicionales:** `if`, `else`
- **Iterativos:** `while (current_book)`, `for (int i = 0; i < memberFound->issued_count; i++)`
- **De salto:** `return`, `break`

---

## 7. 🔁 Control de secuencia
- **Selección:** `if (bookFound && memberFound) { ... } else { ... }`
- **Iteración:** `while (current)`, `for (int i = 0; i < ...; i++)`
- **Recursión:** `displayBooksRecursive` se llama a sí misma para recorrer la lista enlazada de libros

---

## 8. 🧩 Subprogramas
- Funciones definidas: `addBook`, `displayBooks`, `issueBook`, etc.
- Encapsulan tareas específicas como “agregar libro” o “guardar miembros en archivo”

---

## 9. 🧬 Tipos de datos
- **Primitivos:** `enum`
- **Estructurados:**
  - `typedef struct _book { ... } book_t`
  - `typedef struct _member { ... } member_t`
- **Punteros:** `book_t *library`, `member_t *next`
- **Arreglos:** `char title[100]`, `char name[100]`