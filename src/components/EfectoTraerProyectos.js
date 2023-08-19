import { useState, useEffect } from "react";
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';


const useEfectoTraerProyectos = (url) => {

    const [projects, setProjects] = useState([]);
  
    useEffect(() => {

        const getRequest = async (callback) => {

            try {

                const response = await fetch(

                    url,
                    {
                    method: "GET",
                    }
                    
                );
                
                const data = await response.json();
                const array = JSON.parse(data.proyectos);
                callback(array);

            } catch (error) {

                console.error(error);
                
            }

        };
    
        const myCallback = (element) => {
            setProjects(element);
        };
    
        getRequest(myCallback);

    }, []);

    return projects;
};
 
export default useEfectoTraerProyectos;