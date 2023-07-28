from .temporary_models import TempProjectTerreno
from .joiner import join_files

import pandas as pd

UMBRAL = 0.5

class Intersectadores:
    
    """
    Clase para intersectar dataframes
    """

    ## Constructor de intersectador por nomenclatura
    def intersectar_nomenclatura(self, prj1, prj2):

        intersectador_nomenclatura = traer_intersectador_nomenclatura(prj1, prj2)
        return intersectador_nomenclatura

    ## Constructor de intersectador por coordenadas
    def intersectar_coordenadas(self, prj1, prj2):

        intersectador_coordenadas = traer_intersectador_coordenadas(prj1, prj2)

        return intersectador_coordenadas
    

## Para segmentar por funcionalidad y necesidad
def traer_intersectador_nomenclatura(prj1, prj2):

    ## Validez de clase de proyectos
    cond1 = isinstance(prj1, TempProjectTerreno)
    cond2 = isinstance(prj2, TempProjectTerreno)
    cond3 = prj1.file != prj2.file

    ## Valida tipos de proyectos de terreno y segmenta utilidades por tipos
    if cond1 and cond2 and cond3:

        n = TempProjectTerreno.VALID_TYPES[0]
        g = TempProjectTerreno.VALID_TYPES[1:]

        ## Para intersectar por nomenclatura gravedades con nivelaciones
        if prj1.tipo in g and prj2.tipo == n:

            return _intersectador_nomenclatura_grv(prj1=prj1, prj2=prj2)
        
        elif prj2.tipo in g and prj1.tipo == n:

            return _intersectador_nomenclatura_niv(prj1=prj1, prj2=prj2)
        
        else:
            raise ValueError(f"Tipos de proyectos {prj1, prj2} no son adecuados")

    elif not cond1 or not cond2:

        raise ValueError(f"Los objetos {prj1, prj2} no son instancias de las clase {TempProjectTerreno, TempProjectTerreno}, respectivamente")
    
    elif not cond3:

        raise ValueError(f"Los objetos {prj1, prj2} son el mismo")


## Intersecta por nomenclatura utilizando coordenadas de gravedad
def _intersectador_nomenclatura_grv(prj1, prj2):

    files = join_files([prj1, prj2])
    dfgrv = prj1.df
    dflev = prj2.df
    common = pd.merge(dfgrv, dflev, left_on='ID', right_on='ID')
    del common['GEOM_y']
    common.rename(columns={'GEOM_x': 'GEOM'})
    
    return {'files': files, 'df': common}


## Intersecta por nomenclatura utilizando coordenadas de gravedad
def _intersectador_nomenclatura_niv(prj1, prj2):

    files = join_files([prj1, prj2])
    dfgrv = prj2.df
    dflev = prj1.df
    common = pd.merge(dflev, dfgrv, left_on='ID', right_on='ID')
    del common['GEOM_y']
    common.rename(columns={'GEOM_x': 'GEOM'})
        
    return {'files': files, 'df': common}


## Para segmentar por funcionalidad y necesidad
def traer_intersectador_coordenadas(prj1, prj2):

    ## Validez de clase de proyectos
    cond1 = isinstance(prj1, TempProjectTerreno)
    cond2 = isinstance(prj2, TempProjectTerreno)
    cond3 = prj1.file != prj2.file

    n = TempProjectTerreno.VALID_TYPES[0]
    g = TempProjectTerreno.VALID_TYPES[1:]

    ## Valida tipos de proyectos de terreno y segmenta utilidades por tipos
    if cond1 and cond2 and cond3:

        ## Para intersectar por nomenclatura gravedades con nivelaciones
        if prj1.tipo in g and prj2 == n:

            return _intersectador_coordenadas_grv
        
        elif prj2.tipo in g and prj1.tipo == n:

            return _intersectador_coordenadas_niv
        
        else:
            raise ValueError(f"Tipos de proyectos {prj1, prj2} no son adecuados")

    elif not cond1 or not cond2:

        raise ValueError(f"Los objetos {prj1, prj2} no son instancias de las clase {TempProjectTerreno, TempProjectTerreno}, respectivamente")
    
    elif not cond3:

        raise ValueError(f"Los objetos {prj1, prj2} son el mismo")


## Intersecta por coordenadas utilizando coordenadas de gravedad
def _intersectador_coordenadas_grv(prj1, prj2):

    from copy import deepcopy

    files = join_files([prj1, prj2])
    dfgrv = prj1.df
    dflev = prj2.df
    common = dfgrv[dfgrv['GEOM'].apply(lambda point: any(point.distance(other) <= UMBRAL for other in dflev['GEOM']))]
    __dflev = deepcopy(dflev)
    del __dflev['GEOM']
    common = pd.merge(common, __dflev, left_on='ID', right_on='ID')
    del common['GEOM_y']
        
    return {'files': files, 'df': common.rename(columns={'GEOM_x': 'GEOM'})}


## Intersecta por coordenadas utilizando coordenadas de nivelación
def _intersectador_coordenadas_niv(prj1, prj2):

    from copy import deepcopy

    files = join_files([prj1, prj2])
    dflev = prj1.df
    dfgrv = prj2.df
    common = dflev[dflev['GEOM'].apply(lambda point: any(point.distance(other) <= UMBRAL for other in dfgrv['GEOM']))]
    __dfgrv = deepcopy(dfgrv)
    del __dfgrv['GEOM']
    common = pd.merge(common, __dfgrv, left_on='ID', right_on='ID')
    del common['GEOM_y']
        
    return {'files': files, 'df': common.rename(columns={'GEOM_x': 'GEOM'})}