import { useState, useEffect } from 'react';

function ListeAuteurs() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/auteurs/')
            .then(response => response.json())
            .then(json => setData(json))
            .catch(error => console.error(error));
    }, []);

    return (
        <>
            {data ? (
                <ul>
                    {data.map((element, index) => (
                        <li key={index}>{element.nom}</li>
                    ))}
                </ul>
            ) : (
                "Chargement..."
            )}
        </>
    );
}

export default ListeAuteurs;
