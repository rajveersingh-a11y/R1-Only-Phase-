import os

files_to_create = {
    "frontend/package.json": '''{
  "name": "phase-mapping-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-icons": "^4.11.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.15",
    "@types/react-dom": "^18.2.7",
    "@vitejs/plugin-react": "^4.0.3",
    "eslint": "^8.45.0",
    "vite": "^4.4.5"
  }
}''',
    "frontend/vite.config.js": '''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
''',
    "frontend/index.html": '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Phase Mapping Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
''',
    "frontend/src/main.jsx": '''import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles/app.css'
import './styles/dashboard.css'
import './styles/components.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
''',
    "frontend/src/App.jsx": '''import { useState } from 'react'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <div className="logo-section">
          <div className="logo-icon">⚡</div>
          <h1>Phase Mapping AI</h1>
        </div>
        <p className="subtitle">Discover power grid phase topology using voltage clustering</p>
      </header>
      <main className="app-main">
        <Dashboard />
      </main>
      <footer className="app-footer">
        <p>&copy; 2026 Grid Analytics Dashboard. All rights reserved.</p>
      </footer>
    </div>
  )
}

export default App
''',
    "frontend/src/styles/app.css": '''
:root {
  --primary: #2563eb;
  --primary-light: #3b82f6;
  --primary-dark: #1d4ed8;
  --accent: #0ea5e9;
  
  --bg-main: #0f172a;
  --bg-card: #1e293b;
  --bg-card-hover: #334155;
  
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
  
  --border: #334155;
  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  background-color: var(--bg-main);
  color: var(--text-main);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  padding: 2rem;
  background: linear-gradient(to right, var(--bg-card), var(--bg-main));
  border-bottom: 1px solid var(--border);
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  background: linear-gradient(135deg, var(--primary), var(--accent));
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  box-shadow: 0 0 15px rgba(37, 99, 235, 0.5);
}

.app-header h1 {
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(to right, #60a5fa, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subtitle {
  color: var(--text-muted);
  margin-top: 0.5rem;
  font-size: 0.95rem;
}

.app-main {
  flex: 1;
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.app-footer {
  text-align: center;
  padding: 1.5rem;
  color: var(--text-muted);
  border-top: 1px solid var(--border);
  font-size: 0.875rem;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse-glow {
  0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
  100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
''',
    "frontend/src/styles/components.css": '''
.card {
  background-color: var(--bg-card);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  animation: fadeIn 0.4s ease-out forwards;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-light);
}

.card-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  border-radius: var(--radius-md);
  font-weight: 500;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
  font-family: inherit;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
}

.btn-primary:not(:disabled):hover {
  background: linear-gradient(135deg, var(--primary-light), var(--primary));
  box-shadow: 0 6px 8px rgba(37, 99, 235, 0.3);
  transform: translateY(-1px);
}

.btn-secondary {
  background-color: transparent;
  color: var(--text-main);
  border: 1px solid var(--border);
}

.btn-secondary:not(:disabled):hover {
  background-color: var(--bg-card-hover);
  border-color: var(--text-muted);
}

.btn-pulse {
  animation: pulse-glow 2s infinite;
}

/* Forms & Inputs */
.file-upload-zone {
  border: 2px dashed var(--border);
  border-radius: var(--radius-lg);
  padding: 3rem 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: rgba(30, 41, 59, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.file-upload-zone:hover, .file-upload-zone.active {
  border-color: var(--primary);
  background-color: rgba(37, 99, 235, 0.05);
}

.upload-icon {
  font-size: 3rem;
  color: var(--primary-light);
  margin-bottom: 0.5rem;
}

/* Badges */
.badge {
  padding: 0.25rem 0.6rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  background-color: rgba(59, 130, 246, 0.1);
  color: var(--primary-light);
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.badge-success { background-color: rgba(16, 185, 129, 0.1); color: #34d399; border-color: rgba(16, 185, 129, 0.2); }
.badge-warning { background-color: rgba(245, 158, 11, 0.1); color: #fbbf24; border-color: rgba(245, 158, 11, 0.2); }

/* Loader */
.loader {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: white;
  animation: spin 1s linear infinite;
}
''',
    "frontend/src/styles/dashboard.css": '''
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 1024px) {
  .dashboard-grid {
    grid-template-columns: 350px 1fr;
  }
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.content-area {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.metric-card {
  background: var(--bg-card);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  border: 1px solid var(--border);
  border-left: 4px solid var(--primary);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  animation: fadeIn 0.5s ease-out forwards;
}

.metric-card.success { border-left-color: var(--success); }
.metric-card.warning { border-left-color: var(--warning); }
.metric-card.accent { border-left-color: var(--accent); }

.metric-label {
  font-size: 0.875rem;
  color: var(--text-muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.metric-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-main);
  line-height: 1;
}

.results-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

@media (min-width: 1200px) {
  .results-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.plot-container {
  width: 100%;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid var(--border);
  background-color: #fff; /* Keep plots white background if matplotlib */
  aspect-ratio: 4/3;
  display: flex;
  align-items: center;
  justify-content: center;
}

.plot-container img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.status-panel {
  margin-top: 1rem;
  padding: 1rem;
  border-radius: var(--radius-md);
  background-color: rgba(30, 41, 59, 0.5);
  font-size: 0.9rem;
}
''',
    "frontend/src/api.js": '''
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
''',
    "frontend/src/components/FileUpload.jsx": '''
import React, { useRef, useState } from 'react';

export default function FileUpload({ onUploadSuccess }) {
  const [isUploading, setIsUploading] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const [fileName, setFileName] = useState("");
  const inputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = async (file) => {
    if (!file.name.endsWith('.xlsx')) {
      alert("Please upload a valid .xlsx file");
      return;
    }
    
    setIsUploading(true);
    setFileName(file.name);
    try {
      const { uploadFile } = await import('../api');
      const res = await uploadFile(file);
      onUploadSuccess(res.filename);
    } catch (err) {
      alert("Upload failed. Make sure backend is running.");
      setFileName("");
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="card">
      <h2 className="card-title">1. Upload Grid Data</h2>
      <div 
        className={`file-upload-zone ${dragActive ? 'active' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={() => inputRef.current.click()}
      >
        <input 
          ref={inputRef} 
          type="file" 
          accept=".xlsx" 
          onChange={handleChange} 
          style={{ display: "none" }} 
        />
        <div className="upload-icon">📄</div>
        {isUploading ? (
          <p>Uploading {fileName}...</p>
        ) : fileName ? (
          <div>
            <p style={{ color: "var(--success)" }}>Selected: <strong>{fileName}</strong></p>
            <p style={{ fontSize: "0.8rem", marginTop: "0.5rem" }}>Click or drag to change file</p>
          </div>
        ) : (
          <div>
            <p><strong>Click to upload</strong> or drag and drop</p>
            <p style={{ fontSize: "0.8rem", color: "var(--text-muted)", marginTop: "0.5rem" }}>XLSX format required</p>
          </div>
        )}
      </div>
    </div>
  );
}
''',
    "frontend/src/components/PipelineControls.jsx": '''
import React, { useState } from 'react';

export default function PipelineControls({ filename, onAnalysisComplete }) {
  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState(null);

  const handleRun = async () => {
    if (!filename) return;
    setIsRunning(true);
    setError(null);
    try {
      const { runPhaseMapping } = await import('../api');
      const res = await runPhaseMapping(filename);
      onAnalysisComplete(res.metrics, res.output_paths);
    } catch (err) {
      setError("Pipeline execution failed.");
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="card">
      <h2 className="card-title">2. Run Analysis</h2>
      
      <p style={{ marginBottom: "1rem", color: "var(--text-muted)", fontSize: "0.9rem" }}>
        Execute the full unsupervised phase mapping pipeline: extraction, PCA, t-SNE, DBSCAN clustering, and noise assignment.
      </p>

      <button 
        className={`btn btn-primary ${!isRunning && filename ? 'btn-pulse' : ''}`} 
        onClick={handleRun} 
        disabled={!filename || isRunning}
        style={{ width: "100%" }}
      >
        {isRunning ? (
          <span style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
            <span className="loader"></span> Processing Target Topologies...
          </span>
        ) : "Start Phase Mapping Pipeline"}
      </button>

      {error && <div style={{ color: "var(--danger)", marginTop: "1rem", fontSize: "0.9rem" }}>{error}</div>}
    </div>
  );
}
''',
    "frontend/src/pages/Dashboard.jsx": '''
import React, { useState } from 'react';
import FileUpload from '../components/FileUpload';
import PipelineControls from '../components/PipelineControls';
import { getDownloadUrl } from '../api';

export default function Dashboard() {
  const [filename, setFilename] = useState(null);
  const [metrics, setMetrics] = useState(null);

  return (
    <div className="dashboard-grid">
      <aside className="sidebar">
        <FileUpload onUploadSuccess={setFilename} />
        <PipelineControls 
          filename={filename} 
          onAnalysisComplete={(m) => setMetrics(m)} 
        />
        
        {metrics && (
          <div className="card">
            <h2 className="card-title">Downloads</h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              <a href={getDownloadUrl("csv", "final_phase_mapping.csv")} target="_blank" className="btn btn-secondary" download>
                📥 Download Mapping CSV
              </a>
              <a href={getDownloadUrl("csv", "tsne_embeddings.csv")} target="_blank" className="btn btn-secondary" download>
                📥 Download Embeddings
              </a>
              <a href={getDownloadUrl("plots", "tsne_dbscan_clusters.png")} target="_blank" className="btn btn-secondary" download>
                🖼️ Download Cluster Plot
              </a>
            </div>
          </div>
        )}
      </aside>

      <section className="content-area">
        {!metrics ? (
          <div className="card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '400px', flexDirection: 'column', gap: '1rem', color: 'var(--text-muted)' }}>
            <div style={{ fontSize: '4rem', opacity: 0.5 }}>⚡</div>
            <h3>Waiting for data...</h3>
            <p>Upload a grid data file and run the analysis to see results.</p>
          </div>
        ) : (
          <>
            <div className="metrics-grid">
              <div className="metric-card">
                <span className="metric-label">Consumers Analyzed</span>
                <span className="metric-value">{metrics.total_consumers}</span>
              </div>
              <div className="metric-card success">
                <span className="metric-label">Clusters Found</span>
                <span className="metric-value">{metrics.dbscan_clusters_found}</span>
              </div>
              <div className="metric-card warning">
                <span className="metric-label">Noise / Reassigned</span>
                <span className="metric-value">{metrics.noise_points_count} / {metrics.knn_reassigned_count}</span>
              </div>
              <div className="metric-card accent">
                <span className="metric-label">Silhouette Score</span>
                <span className="metric-value">{metrics.silhouette_score ? metrics.silhouette_score.toFixed(3) : "N/A"}</span>
              </div>
            </div>

            <div className="results-grid">
              <div className="card">
                <h2 className="card-title">Cluster Visualization</h2>
                <div className="plot-container">
                  <img src={getDownloadUrl("plots", "tsne_dbscan_clusters.png")} alt="t-SNE Clusters" />
                </div>
              </div>
              
              <div className="card">
                <h2 className="card-title">Phase Distribution</h2>
                <div className="plot-container">
                  <img src={getDownloadUrl("plots", "final_phase_distribution.png")} alt="Phase Distribution" />
                </div>
                
                <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem', justifyContent: 'center' }}>
                  {Object.entries(metrics.phase_counts).map(([phase, count]) => (
                    <div key={phase} style={{ textAlign: 'center', padding: '0.5rem 1rem', background: 'var(--bg-main)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border)' }}>
                      <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginBottom: '0.2rem' }}>Phase {phase}</div>
                      <div style={{ fontWeight: 'bold', fontSize: '1.2rem', color: 'var(--primary-light)' }}>{count}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </>
        )}
      </section>
    </div>
  );
}
'''
}

for path, content in files_to_create.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
        print(f"Created {path}")

