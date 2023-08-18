import tkinter as tk
import sqlite3

class WMSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfache WMS App")

        # Verbindung zur Datenbank herstellen
        self.conn = sqlite3.connect('wms_app.db')
        self.cursor = self.conn.cursor()

        # Tabelle erstellen, falls nicht vorhanden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY,
                product_name TEXT,
                quantity INTEGER
            )
        ''')
        self.conn.commit()

        # GUI-Elemente erstellen
        self.product_label = tk.Label(root, text="Produkt:")
        self.product_label.pack()

        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.pack()

        self.quantity_label = tk.Label(root, text="Menge:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.add_to_inventory_button = tk.Button(root, text="Zum Inventar hinzufügen", command=self.add_to_inventory)
        self.add_to_inventory_button.pack()

        self.show_inventory_button = tk.Button(root, text="Inventar anzeigen", command=self.show_inventory)
        self.show_inventory_button.pack()

    def add_to_inventory(self):
        product_name = self.product_name_entry.get()
        quantity = int(self.quantity_entry.get())

        # Hier fügen Sie das Produkt und die Menge in das Inventar ein
        self.cursor.execute("INSERT INTO inventory (product_name, quantity) VALUES (?, ?)", (product_name, quantity))
        self.conn.commit()

        self.product_name_entry.delete(0, tk.END)  # Felder leeren nach dem Hinzufügen
        self.quantity_entry.delete(0, tk.END)

    def show_inventory(self):
        self.cursor.execute("SELECT * FROM inventory")
        inventory = self.cursor.fetchall()
        for item in inventory:
            print(item)  # Hier könnten Sie das Inventar in einem separaten Fenster anzeigen

if __name__ == "__main__":
    root = tk.Tk()
    app = WMSApp(root)
    root.mainloop()
