# qgeoidcolweb

## Distinctiveness and Complexity

This project is distinctive because provides a sort of tools to facilitate the processing of raw file in order to order such data within a postgres database. It have the enough complexity to join horizontally and to intersect pandas dataframes vertically. The joined and intersected data comes from the https://www.colombiaenmapas.gov.co/ web geovisor of the IGAC. As first step the projects are packaged in shp format, one capability of this development its for load them; when are loaded enough files (projects) to be processed together another capability gives us a sort of tools to process and save them (related to a table that have the metadata for the data) in the postgres  database that is actually reachable to see way pgadmin4 for web browsers; when there are successfully data loaded in the database we can access to them in the last capability of this project: the web geoviewer that let us to see the selected.

In order to provide a wider set of tools to the front-end part of this project React was selected to develop the user interface that actually gives to the user the facility of use the back end services written in python and modeled in the postgres database with not only django but with the django rest framework.

The functionality of join and intersects raw files into a relational database enables to the users of the Modelo Geoidal Colombiano the following facilities:
- join and intersect data from terrain gravity and levelling projects from [IGAC](https://geoportal.igac.gov.co/contenido/datos-abiertos-geodesia) into a postgres database connected to another tabla of raw files metadata
- compute geopotential numbers with the geometric (levelling) and physical (gravity) loaded data
- manage and edit data following the postgres standard

This project was also developed to allow contributors from IGAC to write solutions for processing activities. The connection to the postgis extension of the postgres frame work (using the djangorestframework library) enables contributors to do queries, updates and loading spatial data within an ordered relational database. At first the qgeoicolweb project was conceived unite people from the geodesy division of the colombian governmental organization IGAC. Thus is open to be a project able to unite services of data processing within a relational database that proposes to enhance the data interoperability.


## Objectives

1. To facilitate the usage of [qgeoidcol library](https://github.com/nicalcoca/qgeoidcol) functionalities to the Quasi-Geoid colombian database
2. To enable integration of the [IGAC](https://geoportal.igac.gov.co/contenido/datos-abiertos-geodesia) geodesy division's processing projects 
3. To conform a work team oriented to the software development to unite the data processing of the [IGAC](https://geoportal.igac.gov.co/contenido/datos-abiertos-geodesia) geodesy division


## Tools

# Para subir un archivo crudo (To upload a raw file)

It's conform by a form that enables the user to load a shapefile raw file, is needed to provide enough metadata to desing a well informed database


# Para procesar archivos crudos en conjunto (To process raw files together)

Process with sets of files:
- One levelling project and one gravity project
- One levelling project and two gravity project

Just two gravity projects can't be processed because to calculate geopotential numbers are needed both geometrical and physical values.


# Geovisor de archivos preprocesados (geoviewer of preprocessed files)

Allows users to see graphically the spatial representation of the preprocessed files.
