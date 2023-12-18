import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

from connection import *


db = DataBase()


class Mecanico(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        self.nombre = ttk.StringVar(value="")
        self.patente = ttk.StringVar(value="")
        self.modelo = ttk.StringVar(value="")
        self.description = ttk.StringVar(value="")
        self.Monto = ttk.StringVar(value="")

        self.data = []
        self.colors = master_window.style.colors

        instruction_text = "Ingrese los datos de la Moto: "
        instruction = ttk.Label(self, text=instruction_text, width=50)
        instruction.pack(fill=X, pady=10)

        self.create_form_entry("Nombre: ", self.nombre)
        self.create_form_entry("PATENTE ", self.patente)
        self.create_form_entry("MODELO: ", self.modelo)
        self.create_form_entry("DESCRIPCION: ", self.description)
        self.create_form_entry("MONTO: ", self.Monto)

        self.create_buttonbox()
        self.table = self.create_table()

    def create_form_entry(self, label, variable):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)

        form_field_label = ttk.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)

        form_input = ttk.Entry(master=form_field_container, textvariable=variable)
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

        add_regex_validation(form_input, r'^[a-zA-Z0-9_\s-.<span class="math-inline">\]\*</span>')

        return form_input

    def create_buttonbox(self):
        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))

        cancel_btn = ttk.Button(
            master=button_container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )

        cancel_btn.pack(side=RIGHT, padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text="Submit",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )

        submit_btn.pack(side=RIGHT, padx=5)

    def create_table(self):
        coldata = [
            {"text": "Nombre"},
            {"text": "PATENTE", "stretch": False},
            {"text": "MODELO"},
            {"text": "DESCRIPCION", "stretch": False},
            {"text": "MONTO", "stretch": False},
        ]

        table = Tableview(
            master=self,
            coldata=coldata,
            rowdata=self.data,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.colors.light, None),
        )

        table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        return table

    def on_submit(self):
        """
        Save data to database and update table.
        """
        nombre = self.nombre.get()
        patente = self.patente.get()
        modelo = self.modelo.get()
        description = self.description.get()
        Monto = self.Monto.get()

        # Save data to database
        try:
            sql = """INSERT INTO clientes (nombre, patente, modelo, description, Monto)
                    VALUES (%s, %s, %s, %s, %s)"""
            values = (nombre, patente, modelo, description, Monto)
            db.cursor.execute(sql, values)
            db.connection.commit()
        except Exception as e:
            print(e)
            toast = ToastNotification(
                title="Error al guardar datos",
                message="No se pudo guardar los datos en la base de datos.",
                duration=3000,
            )
            toast.show_toast()

        # Refresh table
        self.data.clear()
        self.table.destroy()
        self.table = self.create_table()

        
    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()
        
if __name__ == "__main__":

    app = ttk.Window("Mecanico", "superhero", resizable=(False, False))
    Mecanico(app)
    app.mainloop()