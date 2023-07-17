from .temporary_models import TempProjectTerreno, TempProjectAerea


class Limpiadores:

    """
    Clase limpiadora de DataFrames
    """

    ## Para limpiar verticalmente (por valor de columnas) un dataframe
    def limpiar_verticalmente(self, prj, var, minor=None, major=None, avoid=None, select=None):
        
        limpiador_vertical = traer_limpiador_vertical(prj)
        df_limpiado = limpiador_vertical(prj.df, var, minor, major, avoid, select)

        return df_limpiado
    
    ## Para limpiar horizontalmente (por nombre de columnas) un dataframe
    def limpiar_horizontalmente()
        pass


## Segmenta el limpiador vertical por tipo de archivo
def traer_limpiador_vertical(prj):
    
    if isinstance(prj, TempProjectTerreno):

        if prj.tipo == 'nivelacion' or prj.tipo == 'gravterrabs' or prj.tipo == 'gravterrrel':
            
            return _limpiador_vertical
        
        elif prj.tipo == 'gravs':

            pass
        
        else:

            raise ValueError(f"El tipo {prj.tipo} no es adecuado para un proyecto {prj}")
    
    elif isinstance(prj, TempProjectAerea):

        pass

    else:

        raise ValueError(f"La clase de proyecto {prj} no es adecuado")


## Limpiador vertical de dataframes
def _limpiador_vertical(df, var, minor, major, avoid, select):

    if minor != None:
                
        df = df[df[var] > minor]
        
    if major != None:
        
        df = df[df[var] < major]
    
    if avoid != None:
        
        df = df[(df[var] != avoid)]
        
    elif select != None:
            
        df = df[(df[var] == select)]
    
    elif avoid != None and select != None:
        
        raise ValueError("No puede seleccionar únicamente un valor de atributo y evitar otro")
    
    else:
        
        raise ValueError("Los parámetros de limpieza no limpiaron nada")

    return df


















































































































































































# def tipos_join(*args):
#     pass


# ## Unir gravedad absoluta y relativa
# def join_gravities(*args):
    
#     _args = list(args)
    
#     ## dataframe nuevo para almacenar
#     data = pd.DataFrame({'ID': [], 'GEOM': [], 'GRAV': []})
    
#     if check_class(args):
        
#         files = join_files(_args)
#         data = join_df_horizontal(_args)
        
#         """Crea el objeto TempProjectTerreno de gravedades absolutas
#         y relativas unidas"""
        
#         joined_gravs = TempProjectTerreno(files, data, 'gravedades')
        
#         return joined_gravs


# ## Para unir nombres de archivos
# def join_files(fs):
#     #Para trazar los archivos unidos"
#     files = ''
#     for f in fs:
        
#         files += f.file + ' '
        
#     return files.rstrip()


# ## Para unir data frames
# def join_df_horizontal(datas):
    
#     ## dataframe nuevo para almacenar
#     data = pd.DataFrame({'ID': [], 'GEOM': [], 'GRAV': []})
    
#     for d in datas:
        
#         _data = d.df
        
#         if list(d.df.columns) == ['ID', 'GEOM', 'GRAV']:
            
#             data = pd.concat([data, _data], axis=0)
        
#     return data


# ## Para verificar que objetos sean de la clase Project
# def check_class(*args):
#     _args = list(args[0])
    
#     print('args: ', args, ', _args: ', _args)
    
#     for a in _args:
        
#         if isinstance(a, TempProjectTerreno) or isinstance(a, TempProjectAerea):
#             continue
            
#         else:
#             raise ValueError(f"El objeto {a} no es ni de la clase {TempProjectTerreno} ni de la clase {TempProjectAerea}")
    
#     return True