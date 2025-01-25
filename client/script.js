const API_BASE_URL = 'http://{backend_ip}:5000';
const FILE_UPLOAD_BASE_URL = 'http://{backend_ip}:5001';

document.addEventListener("DOMContentLoaded", () => {
    showHome();
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

    // Gather query params
    const queryParams = {};
    const queryParamFields = document.querySelectorAll(".query-param");
    queryParamFields.forEach(field => {
        const key = field.querySelector(".query-key").value;
        const value = field.querySelector(".query-value").value;
        if (key) {
            queryParams[key] = value;
        }
    });

    const queryString = Object.keys(queryParams)
        .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(queryParams[key])}`)
        .join("&");

    const url = queryString ? `${API_BASE_URL}${endpoint}?${queryString}` : `${API_BASE_URL}${endpoint}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById('responseData').textContent = `Error: ${error.message}`;
    }
}

function addQueryParamField() {
    const queryParamFields = document.getElementById("queryParamFields");

    const div = document.createElement("div");
    div.className = "query-param";

    const keyInput = document.createElement("input");
    keyInput.type = "text";
    keyInput.placeholder = "Key (e.g., user1)";
    keyInput.className = "query-key";

    const valueInput = document.createElement("input");
    valueInput.type = "text";
    valueInput.placeholder = "Value (e.g., 12345)";
    valueInput.className = "query-value";

    const removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.textContent = "Remove";
    removeButton.onclick = () => div.remove();

    div.appendChild(keyInput);
    div.appendChild(valueInput);
    div.appendChild(removeButton);
    queryParamFields.appendChild(div);
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
            const errorText = await response.text();
            throw new Error(`Server Error: ${errorText}`);
        }

        const result = await response.json();
        document.getElementById('uploadResponse').textContent = `Form submitted successfully. Response: ${JSON.stringify(result, null, 2)}`;
    } catch (error) {
        document.getElementById('uploadResponse').textContent = `Error: ${error.message}`;
    }
}
