import React, { useState, useRef, useEffect } from "react";
import useEfectoTraerProyectos from "./EfectoTraerProyectos";
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import "../static/style.css";


// Items con estilo que depende de la función handleClick
const SelectableItem = ({ item, isSelected, onSelect }) => {

    return (
        <div className="selectable"
            onClick={() => { onSelect(item.pk); }}
            style={{
                cursor: 'pointer',
                backgroundColor: isSelected ? 'lightcoral' : 'white',
                padding: '5px',
                margin: '5px',
            }}>

            {item.fields.archivo_origen}

        </div>
    )

};


// Lista de items
const SelectableItemList = ({ items, data, setData }) => {

    const [selectedItems, setSelectedItems] = useState([]);
    
    const handleClick = (id) => {

        setSelectedItems((selectedItems) => {

            if (selectedItems.includes(id)) {
                    return selectedItems.filter((pk) => pk !== id);
            } else {
                return [...selectedItems, id];
            }
            
        });

    };

    const updater = async (sI) => {

        try {
    
            const response = await fetch(
    
                "http://127.0.0.1:8000/visual/enviar_puntos_visuales",
                {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({'id': sI})
                }
    
            );

            const data_d = await response.json();
            const array = JSON.parse(data_d.data);
            setData(array);
    
        } catch (error) {
    
            console.error(error);
            
        }

    }

    useEffect(() => {
        updater(selectedItems);
    }, [selectedItems])

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


// Componente principal
const Inicio = () => {

    const proyectos = useEfectoTraerProyectos("http://127.0.0.1:8000/visual/enviar_proyectos_visuales");
    const [data, setData] = useState(null);
    const mapRef = useRef(null);

    // Mapa
    useEffect(() => {

        if (!mapRef.current) {

            // Create a Leaflet map
            var map = L.map("leaflet-map").setView([4.691901, -74.074223], 5);

            L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
                maxZoom: 19,
                attribution: "© OpenStreetMap contributors"
            }).addTo(map);

            mapRef.current = map;
        
        }

    }, [])


    if ( data === null || Object.keys(data).length === 0) {

        try {

            mapRef.current.eachLayer(function(layer) {

                if (!layer._url) {
                    mapRef.current.removeLayer(layer);
                }
    
            });

        } catch {
            //pass
        }


    } else {

        // Add puntos to the map
        data.forEach((punto) => {

            var markerOptions = {
                color: "green",
                fillColor: "yellow",
                fillOpacity: 0.8,
                radius: 0.8
            };

            var marker;

            // Extract latitude and longitude from punto.coordinates string
            const regex = /POINT \(([-\d.]+) ([-\d.]+)\)/;
            const matches = punto.fields.posicion.match(regex);

            if (matches) {

                const longitude = parseFloat(matches[1]);
                const latitude = parseFloat(matches[2]);

                // Create marker with extracted latitude and longitude
                marker = L.circle([latitude, longitude], markerOptions);
                marker.addTo(mapRef.current);

            }
            
        });

    }

    // Renderar puntos
    return (

        <div className="container mt-5">

            <h1>Visor</h1>

            <div className="flex-container">

                <div className="left-panel">

                    <SelectableItemList
                        items={proyectos}
                        data={data}
                        setData={setData}
                    />

                </div>

                <div id="leaflet-map" className="leaflet-map"></div>

            </div>
            
        </div>

    );

}

export default Inicio;