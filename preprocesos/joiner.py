from .temporary_models import TempProjectTerreno


class Unificadores:

    """
    Clase para unificar dataframes
    """

    ## Para unificar verticalmente una lista de dataframes
    def unificar_verticalmente(self, lst):
        
        ## Validez del tipo de proyectos
        lst = [l for l in lst if l.tipo == 'gravterrabs' or l.tipo == 'gravterrrel']
        unificador_vertical = traer_unificador_vertical(lst)
        df_unificado = unificador_vertical(lst)

        return df_unificado


def traer_unificador_vertical(lst):

    ## Si los objectos son de proyectos adecuados
    rule = [1 if isinstance(l, TempProjectTerreno) else 0 for l in lst ]
    
    ## Valida si el parámetro del unificador es adecuado
    if all(r == 1 for r in rule) and len(lst) > 1:

        return _unificador_vertical

    else:

        raise ValueError('Los objectos son de proyectos adecuados o los proyectos de tipo gravedad no son suficientes')


def _unificador_vertical(lst):

    l = lst[0]

    files = [lst.file for lst in lst]
    files = join_files(files)

    datas = [lst.df for lst in lst]
    datas = join_df_vertical(datas)

    return TempProjectTerreno(files, datas, 'gravs', l.proyeccion, l.elipsoide)


## Para unir nombres de archivos
def join_files(fs):

    #Para trazar los archivos unidos
    files = ''
    for f in fs:
        
        files += str(f.file) + ' '
        
    return files.rstrip()


## Para unir data frames
def join_df_vertical(datas):
    import pandas as pd
    
    ## dataframe nuevo para almacenar
    col = datas[0].columns
    data = pd.DataFrame(columns=col)

    for d in datas:

        if list(d.columns) == list(col):
            
            data = pd.concat([data, d], axis=0)

    return data