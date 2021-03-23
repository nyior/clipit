const API_URL = 'https://shter.herokuapp.com'

async function apiService (endpoint, method, data) {
  endpoint = `${API_URL}/${endpoint}`

  const response = await fetch(
    endpoint,
    {
      method: method,
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data !== undefined ? JSON.stringify(data) : null
    }
  )

  return response.json()
}

export { apiService }
