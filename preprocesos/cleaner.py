from .temporary_models import TempProjectTerreno, TempProjectAerea


class Limpiadores:

    """
    Clase limpiadora de DataFrames
    """

    ## Para limpiar verticalmente (por valor de columnas) un dataframe
    def limpiar_verticalmente(self, prj, var, minor=None, major=None, avoid=None, select=None):
        
        limpiador_vertical = traer_limpiador_vertical(prj)
        df_limpio = limpiador_vertical(prj.df, var, minor, major, avoid, select)

        return df_limpio
    
    ## Para limpiar horizontalmente (por nombre de columnas) un dataframe
    def limpiar_horizontalmente(self, prj, id, var, geom='geometry'):
        
        limpiador_horizontal = traer_limpiador_horizontal(prj)
        df_limpio = limpiador_horizontal(prj.df, id, var, geom)
        
        return df_limpio


## Segmenta el limpiador vertical por tipo de archivo
def traer_limpiador_vertical(prj):
    
    if isinstance(prj, TempProjectTerreno):

        if prj.tipo == 'nivelacion' or prj.tipo == 'gravterrabs' or prj.tipo == 'gravterrrel':
            
            return _limpiador_vertical
        
        elif prj.tipo == 'gravs':

            print(f"El tipo {prj.tipo} no tiene métodos aún")
        
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


def traer_limpiador_horizontal(prj):

    if isinstance(prj, TempProjectTerreno):

        if prj.tipo == 'nivelacion':
            
            return _limpiador_horizontal_nivelacion
        
        elif prj.tipo == 'gravterrabs' or prj.tipo == 'gravterrrel':

            return _limpiador_horizontal_gravedades
        
        elif prj.tipo == 'gravs':

            pass
        
        else:

            raise ValueError(f"El tipo {prj.tipo} no es adecuado para un proyecto {prj}")

    elif isinstance(prj, TempProjectAerea):

        pass

    else:

        raise ValueError(f"La clase de proyecto {prj} no es adecuado")


def _limpiador_horizontal_nivelacion(df, id, var, geom):

    clean_df = df.rename(columns={id: 'ID', geom: 'GEOM', var: 'ALTURA_M_S'})
    clean_df = clean_df[['ID', 'GEOM', 'ALTURA_M_S']]
    
    return clean_df

def _limpiador_horizontal_gravedades(df, id, var, geom):

    clean_df = df.rename(columns={id: 'ID', geom: 'GEOM', var: 'GRAV'})
    clean_df = clean_df[['ID', 'GEOM', 'GRAV']]
    
    return clean_df