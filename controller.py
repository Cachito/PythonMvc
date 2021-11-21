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