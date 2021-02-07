const API_URL = "https://shter.herokuapp.com";

// const API_URL = "http://127.0.0.1:8000"; 

async function apiService(endpoint, method, data) {
    endpoint = `${API_URL}/${endpoint}`;

    const response = await fetch(
        endpoint, 
        {
            method: method,
            credentials:"include",
            headers: {
                'Content-Type': 'application/json'
            },
            body: data !== undefined ? JSON.stringify(data) : null,
        }
    );

    return response.json(); 
}

// function apiService(endpoint, method, data) {
//   endpoint = `${API_URL}/${endpoint}`;

//   const config = {
//     url: endpoint,
//     method: method,
//     withCredentials: true,
//     data: data !== undefined ? data : null,
//     headers: {
//       "content-type": "application/json"
//     }
//   };

//   return axios(config).then(response => response.data);
// }

export { apiService };
