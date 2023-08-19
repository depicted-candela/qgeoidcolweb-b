import { useState, useEffect } from "react";


const useProjectsEffect = () => {
  
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const getRequest = async (callback) => {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/preprocesos/mostrar_prjs_terr/",
          {
            method: "GET",
          }
        );
        const data = await response.json();
        const array = JSON.parse(data.prjs);
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

export default useProjectsEffect;