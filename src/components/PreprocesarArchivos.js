import React, { useState, useEffect } from "react";
import axios from "axios";
import useProjectsEffect from "./UseProjectEffect";
import "../static/style.css";


// Items con estilo que depende de la función handleClick
const SelectableItem = ({ item, isSelected, onSelect }) => {

    return (
        <div className="selectable"
            onClick={() => onSelect(item.pk)}
            style={{
                cursor: 'pointer',
                backgroundColor: isSelected ? 'lightcoral' : 'white',
                padding: '5px',
                margin: '5px',
            }}>

            {item.fields.detalles}

        </div>
    )

};


// Rendera herramientas
const SelectableTool = ({ tool, isSelected, onSelect }) => {

    return (
        <div className="selectable"
            onClick={() => onSelect(tool.id)}
            style={{
                cursor: 'pointer',
                backgroundColor: isSelected ? 'lightcoral' : 'white',
                padding: '5px',
                margin: '5px',
            }}>

            {tool.nombre}

        </div>
    )

};


// Lista de items
const SelectableItemList = ({ items, selectedItems, setSelectedItems }) => {

    // Agrega o elimina items del Hook selectedItems
    const handleClick = (id) => {

    // Where id is the key of the element

        setSelectedItems((prevSelectedItems) => {

            if (prevSelectedItems.includes(id)) {
                return prevSelectedItems.filter((pk) => pk !== id);
            } else {
                return [...prevSelectedItems, id];
            }

        });

    };

    return (

        <div>

            {items.map((item) => (
                
                // Componente arriba dinamizado y llenado aquí con datos de
                // useProjectsEffect

                <SelectableItem
                    key={item.pk}
                    item={item}
                    isSelected={selectedItems.includes(item.pk)}
                    onSelect={handleClick}
                />

            ))}

        </div>

    );

};


// Lista de items
const SelectableToolsList = ({ tools, subProject, subTools, setSubTool, selectedTool, setSelectedTool }) => {

    const bool1 = subProject.includes('nivelacion');
    const bool2 = subProject.includes('gravterrrel');
    const bool3 = subProject.includes('gravterrabs');

    const [bool4, setBool4] = useState();

    useEffect(() => {

        if ( (bool1 && bool2 && bool3) || (bool1 && bool2) || (bool1 && bool3) ) {

            setSubTool((prevSelectedTools) => {
    
                return [...prevSelectedTools, tools.find(item => item.id === 1)];
    
            })

            setBool4(true);
    
        } else {

            setBool4(false);
            
            setSubTool((prevSelectedItems) => {

                return prevSelectedItems.filter((id) => id !== id);

            })

        }

    }, [bool1, bool2, bool3]);


    // Agrega o elimina items del Hook selectedItems
    const handleClick = (id) => {

    // Where id is the key of the element

        setSelectedTool((prevSelectedItems) => {

            if (prevSelectedItems.includes(id)) {
                return prevSelectedItems.filter((id) => id !== id);
            } else {
                return [...prevSelectedItems, id];
            }

        });

    };

    const counts = {};
    for (const item of subTools) {
        const key = JSON.stringify(item); // Convert the object to a string for use as a key
        counts[key] = (counts[key] || 0) + 1;
    }

    const newArray = subTools.filter(item => {
        const key = JSON.stringify(item);
        if (counts[key] > 1) {
            counts[key]--;
        } else {
            return item;
        }
        return false;
    });

    if (bool4) {

        return (

            <div>
    
                {newArray.map((tool) => (
                    
                    // Componente arriba dinamizado y llenado aquí con datos de
                    // useProjectsEffect
    
                    <SelectableTool
                        key={tool.id}
                        tool={tool}
                        isSelected={selectedTool.includes(tool.id)}
                        onSelect={handleClick}
                    />
    
                ))}
    
            </div>
    
        );

    } else {

        return (<div>Seleccione Proyecto(s)</div>)
    
    }
    
};


// Para enviar datos a la url http://127.0.0.1:8000/rasdf
const Submit = ({ selectedTool, selectedItems }) => {

    const [cookie, setCookie] = useState();

    useEffect(() => {
    
        // Function to fetch the CSRF token from the server and set it in Axios headers
        try {
            const response = axios.get('http://127.0.0.1:8000/preprocesos/csrf_token', {
                headers: { 'Authorization': null },
                withCredentials: true,
            });

            setCookie(response.then(data => data['data']));

        } catch (error) {
            console.error("Failed to fetch CSRF token:", error);
        }

    }, [])

    const HandleSubmit = async (e) => {

        e.preventDefault();

        // Crear una forma contenedora de datos
        const uploadData = new FormData();
        uploadData.append('tool', selectedTool);
        uploadData.append('item', selectedItems);

        try {

            console.log(uploadData);

            const request = new Request('http://127.0.0.1:8000/preprocesos/recibir_preprocesar_api',
                {
                    method: 'POST',
                    headers: {'X-XSRFToken': cookie},
                    body: uploadData
                }
            )

            const response = fetch(request);

            response.then(data => console.log(data));

        } catch (error) {

            console.error(error.message);

        }
        
    };

    return (
        <div className="row">
            <form method="post" action="http://localhost:8000/recibir_preprocesar/" onSubmit={HandleSubmit}>
                {/* <input type="hidden" name="csrfmiddlewaretoken" value={getCSRFToken()} /> */}
                <button type="submit">
                    Enviar
                </button>
            </form>
        </div>
    )

};


// Componente principal
const Inicio = () => {

    // Proyectos obtenidos dentro del hook en el módulo useProjectsEffect
    const project = useProjectsEffect();
    const [selectedItems, setSelectedItems] = useState([]);

    var subProject = project.filter((item) => selectedItems.includes(item.pk));
    subProject = subProject.map(item => item.fields.tipo);

    // Herramientas para utilizar
    const tools = [{nombre: "Unir nivelación y gravedades terrestres", id: 1}];

    const [subTools, setSubTool] = useState([]);
    const [selectedTool, setSelectedTool] = useState([]);

    // Rendera los items estilizados en <SelectableItemList> y alimentados
    // con useProjectsEffect
    return (

        <div className="container mt-5">

            <h1>Archivos disponibles</h1>

            <SelectableItemList
                items={project}
                selectedItems={selectedItems}
                setSelectedItems={setSelectedItems} />
            
            <h1>Herramientas disponibles</h1>

            <SelectableToolsList
                tools={tools}
                subProject={subProject}
                subTools={subTools}
                setSubTool={setSubTool}
                selectedTool={selectedTool}
                setSelectedTool={setSelectedTool} />

            <Submit
                selectedTool={selectedTool}
                selectedItems={selectedItems} />

        </div>

    );

};

export default Inicio;