# **Práctica 4 — Migración del Sistema de Biblioteca a Python con Programación Orientada a Objetos**

**Materia:** Paradigmas de la programacion
**Carrera:** Ingeniero en Software y Tecnologías Emergentes  
**Institución:** FIAD - UABC  
**Alumno:** Abraham Armenta Marrufo 
**Fecha:** 17-OCT-2025

---

## 🧩 **Objetivo**

Migrar el programa de **Biblioteca** desarrollado previamente en **C con estructuras** hacia **Python** utilizando los principios de la **Programación Orientada a Objetos (POO)**, aplicando los conceptos de **clase, objeto, herencia, encapsulamiento, abstracción y polimorfismo**.  
Además, se debe agregar persistencia de datos, un menú interactivo en consola y permitir operaciones de alta, búsqueda, préstamo y devolución de ítems.

---

## ⚙️ **Diseño e Implementación**

### 📘 Clases Principales

| Clase | Descripción |
|-------|--------------|
| `LibrarySystem` | Clase principal que gestiona toda la biblioteca, los usuarios y las operaciones. |
| `Book` | Representa un libro dentro del sistema. Hereda de `Item`. |
| `Magazine` | Representa una revista. Hereda de `Item`. |
| `Member` | Representa a los usuarios registrados que pueden pedir préstamos. |
| `Item` | Clase abstracta base que define los atributos comunes entre libros y revistas. |
| `MemoryManager` | Clase auxiliar que simula el control de memoria dinámica (inspirada en la versión en C). |

---

### 🧠 **Conceptos POO Aplicados**

#### **1. Clase**
Una **clase** es una plantilla que define las propiedades y comportamientos de un objeto.  
Ejemplo:

```python
class Book(Item):
    def __init__(self, book_id, title, author, year, genre, quantity):
        super().__init__(book_id, title, year, quantity)
        self.author = author
        self.genre = genre
