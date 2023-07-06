import React, { useEffect, useState } from 'react';
        
function something() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetchData();
    }, []);

    async function fetchData() {

        try {
            const response = await fetch("/mostrar_prjs_terr/");
            const jsonData = await response.json();
            setData(jsonData);
        } catch (error) {
            console.log("Error", error);
        }

    }

    return (
        {haha}
    );
    
}

export default something;