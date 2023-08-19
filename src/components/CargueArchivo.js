import React, { useState } from "react";
import axios from "axios";


const CargueArchivo = () => {
    
    // To create formatted data serializable to json
    const [formData, setFormData] = useState({
        nombre: "",
        tipo: "",
        detalle: "",
        archivo: null,
    });

    // To add keys with value to the serializable formatted data
    const handleChange = (e) => {
        const { name, files } = e.target;
        if (name === 'archivo') {
            setFormData((prevFormData) => ({
                ...prevFormData,
                [name]: files[0],
            }));
        } else {
            setFormData((prevFormData) => ({
                ...prevFormData,
                [name]: e.target.value,
            }));
        }
    };

    // Para enviar datos a la url http://127.0.0.1:8000/recibir
    const handleSubmit = async (e) => {

        e.preventDefault();

        // Crear una forma contenedora de datos
        const uploadData = new FormData();
        uploadData.append("nombre", formData.nombre);
        uploadData.append("tipo", formData.tipo);
        uploadData.append("detalle", formData.detalle);
        uploadData.append("archivo", formData.archivo);

        try {
            const response = await axios.post("http://127.0.0.1:8000/recibir", uploadData);
            setFormData({
                nombre: "",
                tipo: "",
                detalle: "",
                archivo: null
            });
            console.log(response);
        } catch (error) {
            console.error(error);
        }
        
    };

    return (
        <div className="container mt-5">
            <div className="row">
                <div className="col">
                    <h2>Cargue Archivos</h2>
                    <form onSubmit={handleSubmit} encType="multipart/form-data">
                        <div className="mb-3">
                        <label htmlFor="nombre" className="form-label">
                            Nombre (utilice minúsculas y no tildes):
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            id="nombre"
                            name="nombre"
                            value={formData.nombre}
                            onChange={handleChange}
                            aria-describedby="emailHelp"
                        />
                        </div>

                        <div className="mb-3">
                        <label htmlFor="archivo" className="form-label">
                            Archivo:
                        </label>
                        <input
                            type="file"
                            className="form-control"
                            id="archivo"
                            name="archivo"
                            onChange={handleChange}
                            aria-describedby="emailHelp"
                        />
                        </div>

                        <div className="mb-3">
                        <label htmlFor="tipo" className="form-label">
                            Tipo de proyecto:
                        </label>
                        <select
                            className="form-control"
                            id="tipo"
                            name="tipo"
                            value={formData.tipo}
                            onChange={handleChange}
                            aria-describedby="emailHelp"
                        >
                            <option value="">Seleccione un tipo de archivo</option>
                            <option value="nivelacion">Nivelación</option>
                            <option value="gravterrabs">Gravedad terrestre absoluta</option>
                            <option value="gravterrrel">Gravedad terrestre relativa</option>
                            <option value="gravedades">
                            Gravedades terrestres absolutas y relativas
                            </option>
                        </select>
                        </div>

                        <div className="mb-3">
                        <label htmlFor="detalle" className="form-label">
                            Detalle:
                        </label>
                        <input
                            type="text"
                            className="form-control"
                            id="detalle"
                            name="detalle"
                            value={formData.detalle}
                            onChange={handleChange}
                            aria-describedby="emailHelp"
                        />
                        </div>

                        <button type="submit" className="btn btn-outline-primary">
                            Submit
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default CargueArchivo;