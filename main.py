import db

def show_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto por nombre")
    print("4. Mostrar inventario ordenado por categoría")
    print("5. Exportar inventario a CSV")
    print("6. Actualizar producto")
    print("7. Eliminar producto")
    print("8. Salir")

def main():
    db.create_table()

    while True:
        show_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            name = input("Nombre del producto: ")
            category = input("Categoría: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            db.add_product(name, category, quantity, price)
            print("Producto agregado exitosamente.")

        elif choice == "2":
            products = db.get_all_products()
            print("\nID | Nombre | Categoría | Cantidad | Precio")
            for p in products:
                print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | ${p[4]:.2f}")

        elif choice == "3":
            name = input("Nombre del producto a buscar: ")
            results = db.search_product_by_name(name)
            if results:
                print("\nID | Nombre | Categoría | Cantidad | Precio")
                for p in results:
                    print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | ${p[4]:.2f}")
            else:
                print("Producto no encontrado.")

        elif choice == "4":
            products = db.get_products_sorted_by_category()
            print("\nID | Nombre | Categoría | Cantidad | Precio")
            for p in products:
                print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]} | ${p[4]:.2f}")

        elif choice == "5":
            db.export_to_csv("inventario.csv")
            print("Inventario exportado a 'inventario.csv'.")

        elif choice == "6":
            id = int(input("ID del producto a actualizar: "))
            q = input("Nueva cantidad (deja vacío si no cambia): ")
            p = input("Nuevo precio (deja vacío si no cambia): ")
            quantity = int(q) if q else None
            price = float(p) if p else None
            db.update_product(id, quantity, price)
            print("Producto actualizado.")

        elif choice == "7":
            id = int(input("ID del producto a eliminar: "))
            db.delete_product(id)
            print("Producto eliminado.")

        elif choice == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
