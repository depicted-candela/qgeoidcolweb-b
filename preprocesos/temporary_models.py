from pandas.core.frame import DataFrame as pdf
from django.db.models.fields.files import FieldFile
from abc import ABC

class TempProject(ABC):

    """
    Clase padre para proyectos temporales
    """

    VALID_TYPES = []

    ## Valores inicializadores
    def __init__(self, file, df, tipo, proyeccion, elipsoide='None'):
        
        # Para validar tipos de formato de objetos de entrada
        if isinstance(file, FieldFile) or isinstance(file, str) and isinstance(df, pdf) and isinstance(tipo, str):
            
            self.__file = file
            self.__df = df
            self.__proyeccion = proyeccion
            self.__elipsoide = elipsoide

        ## Para validar tipo de proyecto
        if tipo in self.VALID_TYPES:
            print(f"Inicializando objeto de {tipo}")
            self.__tipo = tipo
        else:
            raise ValueError(f"Valores válidos para tipo son: {', '.join(self.VALID_TYPES)}")
    
    ## Define el agregador como propiedad del objeto
    @property
    def df(self):
        return self.__df
    
    ## Define archivo como propiedad del objeto
    @property
    def file(self):
        return self.__file
    
    # Define el tipo como propiedad del objecto
    @property
    def tipo(self):
        return self.__tipo
    
    # Define la proyección como propiedad del objecto
    @property
    def proyeccion(self):
        return self.__proyeccion
    
    # Define el elipsoide como propiedad del objecto
    @property
    def proyeccion(self):
        return self.__elipsoide
    

    ## Reglas para tipo de dato
    def set_df_file_tipo(self, df, file, tipo):
        
        # Para validar tipos de formato de objetos de entrada
        if isinstance(file, FieldFile) and isinstance(df, pdf) and isinstance(tipo, str):
            self.__file = file
            self.__df = df
        else:
            raise TypeError(f"Los valores de entrada {(df, file, tipo)} no son del tipo indicado")
        
        ## Para validar tipo de proyecto
        if tipo in self.VALID_TYPES:
            self.__tipo = tipo
        else:
            raise ValueError(f"Valores válidos para tipo son: {', '.join(self.VALID_TYPES)}")

    # Resultado para la función print
    def __str__(self):
        return f"{self.file}"


class TempProjectTerreno(TempProject):

    """
    Clase hija para proyectos temporales terrestres
    """

    VALID_TYPES = [
        'nivelacion', 'gravterrabs', 'gravterrrel',
        'gravs'
        ]

    ## Define el agregador como propiedad del objeto
    @property
    def df(self):
        return self._TempProject__df
    
    ## Define archivo como propiedad del objeto
    @property
    def file(self):
        return self._TempProject__file
    
    # Define el tipo como propiedad del objecto
    @property
    def tipo(self):
        return self._TempProject__tipo
    
    # Define el tipo como propiedad del objecto
    @property
    def proyeccion(self):
        return self._TempProject__proyeccion
    
    # Define el elipsoide como propiedad del objecto
    @property
    def elipsoide(self):
        return self._TempProject__elipsoide

    # Resultado para la función print
    def __str__(self):
        return f"{self.file}"

class TempProjectAerea(TempProject):

    """
    Clase hija para proyectos temporales terrestres
    """

    VALID_TYPES = [
        'aerea'
        ]