const API_BASE_URL = 'http://localhost:5000';
const FILE_UPLOAD_BASE_URL = 'http://localhost:5001';

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("home-section").style.display = "block";

    document.getElementById("api-section").style.display = "none";
});

function showHome() {
    document.getElementById("home-section").style.display = "block";
    document.getElementById("api-section").style.display = "none";
}

function showApi() {
    document.getElementById("home-section").style.display = "none";
    document.getElementById("api-section").style.display = "block";
}

async function makeRequest() {
    const endpointSelector = document.getElementById('endpoint');
    let endpoint = endpointSelector.value;

    if (endpoint.includes(':user_id')) {
        const userId = prompt('Enter user_id:');
        if (!userId) return alert('user_id is required.');
        endpoint = endpoint.replace(':user_id', userId);
    }

    if (endpoint.includes(':project_id')) {
        const projectId = prompt('Enter project_id:');
        if (!projectId) return alert('project_id is required.');
        endpoint = endpoint.replace(':project_id', projectId);
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`);
        const data = await response.json();
        document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById('responseData').textContent = `Error: ${error.message}`;
    }
}

async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        document.getElementById('uploadResponse').textContent = "No se seleccionó ningún archivo.";
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${FILE_UPLOAD_BASE_URL}/upload`, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            throw new Error(errorResponse.error || 'Unknown server error, please contact the administrator.');
        }

        const result = await response.json();
        document.getElementById('uploadResponse').textContent = `File uploaded successfully.`;
    } catch (error) {
        document.getElementById('uploadResponse').textContent = `Error: ${error.message}`;
    }
}

async function submitForm() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const username = document.getElementById('username').value.trim();
    const collaborators = document.getElementById('collaborators').value.trim();

    if (!file || !username) {
        document.getElementById('uploadResponse').textContent = "Please fill out all required fields.";
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('user_name', username);
    formData.append('collaborators', collaborators);

    try {
        const response = await fetch(`${FILE_UPLOAD_BASE_URL}/upload`, {
            method: 'POST',
            body: formData,
        });
    
        if (!response.ok) {
            const errorText = await response.text(); // Obtiene el texto completo de la respuesta
            throw new Error(`Server Error: ${errorText}`);
        }
    
        const result = await response.json();
        document.getElementById('uploadResponse').textContent = `Form submitted successfully. Response: ${JSON.stringify(result, null, 2)}`;
    } catch (error) {
        document.getElementById('uploadResponse').textContent = `Error: ${error.message}`;
    }
}    

