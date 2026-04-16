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