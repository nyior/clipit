import axios from "axios";

const API_URL = "https://shter.herokuapp.com";

// axios.defaults.withCredentials = true

function apiService(endpoint, method, data) {
  endpoint = `${API_URL}/${endpoint}`;

  const config = {
    url: endpoint,
    method: method,
    withCredentials: true,
    data: data !== undefined ? data : null,
    headers: {
      "content-type": "application/json"
    }
  };

  return axios(config).then(response => response.data);
}

export { apiService };
