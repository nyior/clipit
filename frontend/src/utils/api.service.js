import axios from "axios";

const API_URL = "https://webinge.herokuapp.com";
const SHAZAM_BASE_URL = "https://shazam.p.rapidapi.com";

function apiService(endpoint, method, data) {
  endpoint = `${API_URL}/${endpoint}`;

  const config = {
    url: endpoint,
    method: method,
    data: data !== undefined ? data : null,
    headers: {
      "content-type": "application/json"
    }
  };

  return axios(config).then(response => response.data);
}

function shazamApiService(endpoint, params) {
  endpoint = `${SHAZAM_BASE_URL}/${endpoint}`;

  const config = {
    url: endpoint,
    method: "GET",
    params: params,
    headers: {
      "x-rapidapi-key": process.env.VUE_APP_API_KEY,
      "x-rapidapi-host": "shazam.p.rapidapi.com"
    }
  };

  return axios(config).then(response => response.data);
}

export { apiService };
export { shazamApiService };
