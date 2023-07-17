from .temporary_models import TempProjectTerreno, TempProjectAerea
from .strings import subset_string
from pathlib import Path

import os


# Para resolver directorios
BASE_URL = Path(__file__).resolve().parent.parent


# Lector de archivos de gravimetría y altimetría
def reader(prj):
    str_file = str(prj.file)
    os.chdir(BASE_URL)
    file_name, file_ext = os.path.splitext(str_file)

    ## Archivos .csv
    if file_ext == '.csv':

        df = pd.read_csv(str_file, delimiter=',')

    # Archivos .shp o .gpkg
    elif file_ext == '.zip':

        import zipfile
        import pandas as pd
        import geopandas as gpd
            
        ## Para crear archivos shx y dbf
        from shapely.geometry import shape
        import shapefile as shpf

        zip_file = str_file
        destination_folder = "media"

        # Open the zip file
        with zipfile.ZipFile(zip_file, "r") as zip_ref:

            # Extract all files to the destination folder
            zip_ref.extractall(destination_folder)
            gdf = gpd.read_file(str_file)
            df = pd.DataFrame(gdf)
        
        # Delete the extracted files
        extracted_files = zip_ref.namelist()  # Get the list of extracted files
        for file_name in extracted_files:
            file_path = os.path.join(destination_folder, file_name)
            os.remove(file_path)
    
    elif file_ext == '.gpkg':

        gdf = gpd.read_file(str_file)
        df = pd.DataFrame(gdf)

    # El resto de archivos
    else:

        return 'Formato no soportado'

    match prj.tipo:

        # Para objetos de clase Proyecto
        case 'nivelacion' | 'gravterrabs' | 'gravterrrel':

            return TempProjectTerreno(prj.file, df, prj.tipo)

        # Para objetos de clase RawProject
        case 'crudo-aereo':
            return TempProjectAerea(prj.file, df, prj.tipo)
