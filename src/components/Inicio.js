import React from "react";
import {Link} from 'react-router-dom';


const Inicio = () => {

    return (
        <div className="container mt-5">
            <div className="row">
                <div className="col">
                    <ul className="list-group">
                        <li className="list-group-item" aria-current="true">
                            <Link className="right" to="/cargarArchivo">Para subir un archivo crudo</Link>
                        </li>
                        <li className="list-group-item">
                            <Link className="right" to="/preprocesarArchivo">Para procesar archivos crudos en conjunto</Link>
                        </li>
                        <li className="list-group-item">
                            <Link className="right" to="/consultasGraficas">Geovisor de archivos</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
    
}

export default Inicio;