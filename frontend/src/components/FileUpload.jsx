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