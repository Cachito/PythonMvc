import re
import datetime
from clases import *

class Controller:
     def __init__(self, model, view):
          self.model = model
          self.view = view

     def save(self, email):
          """
          Save the email
          :param email:
          :return:
          """
          try:
               # save the model
               self.model.email = email
               self.model.save()
               # show a success message
               self.view.show_success(f'The email {email} saved!')

          except ValueError as error:
               # show an error message
               self.view.show_error(error)

     def refresh(self):
          """
          limpia el trew
          trae los registros de la base de datos
          carga el tree
          """
          try:
               self.view.clean_tree()
               resultado = self.model.get_all()
               self.view.load_tree(resultado)
          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", f"error al intentar obtener noticias: {str(e)}")

     def create_data(self):
          """
          crea la base de datos carro_maier
          """
          try:
               self.model.create_data()
               self.view.salta_violeta("Carro-Maier", "Base de datos carro_meier creada con éxito")
          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", str(e))

     def create_table(self):
          """
          crea la tabla noticias
          """
          try:
               self.model.create_table()
               self.view.salta_violeta("Carro-Maier", "Tabla `Noticias` creada con éxito")

          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", str(e))

     def save_data(self, noticia):
          try:
               if self.valida(noticia):
                    self.model.save_data(noticia)
                    self.view.salta_violeta("Carro-Maier", f"registro {'insertado' if noticia.Id == '0' else 'actualizado'} con éxito")
                    self.refresh()
                    self.view.clear_data()

          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", str(e))

     def delete_data(self, search_id):
          if not search_id:
               self.view.salta_violeta("Carro-Maier", "Debe seleccionar algo")
               return

          try:
               self.model.delete_data(search_id)
               self.view.salta_violeta("Carro-Maier", f"Registro id:{search_id} eliminado")
               self.refresh()
               self.view.clear_data()

          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", str(e))

     def get_datos(self, search_id):
          if not search_id:
               self.view.salta_violeta("Carro-Maier", "Debe seleccionar algo")
               return

          try:
               return self.model.get_datos(search_id)
          except Exception as e:
               self.view.salta_violeta("Error Carro-Maier", str(e))

     def valida(self, noticia):
          msj_error = ""

          if not noticia.Fecha:
               msj_error = " fecha "
          else:
               try:
                    datetime.datetime.strptime(noticia.Fecha, '%Y-%m-%d')
               except ValueError:
                    msj_error = " el formato de la fecha debe ser YYYY-MM-dd"

          if not noticia.Medio:
               msj_error = f"{msj_error} medio "

          if not noticia.Seccion:
               msj_error = f"{msj_error} seccion "

          if not noticia.Titulo:
               msj_error = f"{msj_error} título "

          if not noticia.Cuerpo:
               msj_error = f"{msj_error} cuerpo "

          if msj_error:
               self.view.salta_violeta("Carro-Maier", f"debe ingresar: {msj_error}")
               return False
          else:
               return True