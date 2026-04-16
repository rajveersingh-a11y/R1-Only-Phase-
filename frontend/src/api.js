const API_URL = "http://localhost:8000";

export const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append("file", file);
    
    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
    });
    
    if (!response.ok) {
        throw new Error("Upload failed");
    }
    return response.json();
};

export const runPhaseMapping = async (filename) => {
    const response = await fetch(`${API_URL}/run-phase-mapping?filename=${filename}`, {
        method: "POST",
    });
    
    if (!response.ok) {
        throw new Error("Analysis failed to run.");
    }
    return response.json();
};

export const getDownloadUrl = (folder, filename) => {
    return `${API_URL}/results/download/${folder}/${filename}`;
};