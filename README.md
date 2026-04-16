# Phase Mapping System

An AI-driven full-stack system to identify phase topography (A, B, or C) from electrical grid voltage data using unsupervised machine learning.

![Dashboard Preview](frontend/public/vite.svg)

## Overview

The Grid Phase Mapping tool ingests time-series voltage data from consumer meters and transformers. It standardizes, reduces dimensionality (PCA/t-SNE), clusters the data (DBSCAN), and maps each cluster to physical phases based on known topological hints.

## Key Features
- **Frontend Dashboard:** React + Vite architecture with dynamic charting.
- **Backend Pipeline:** FastAPI + scikit-learn for unsupervised machine learning.
- **Robust Pipeline:** Emphasizes shape correlation of voltage profiles.

## Folder Structure

```
project_root/
├── backend/
│   ├── app/
│   │   ├── api/          # Endpoints
│   │   ├── services/     # ML and Processing logic
│   │   ├── data/         # Uploaded datasets
│   │   └── outputs/      # Generated models, plots, CSVs
│   ├── run.py            # FastAPI main entry point
│   └── requirements.txt  # Python deps
├── frontend/
│   ├── src/              # React code
│   ├── package.json      # Node deps
│   └── vite.config.js    # Vite configuration
├── README.md
└── .gitignore
```

## Getting Started

### 1. Backend Setup

Prerequisites: Python 3.9+

```bash
cd backend
pip install -r requirements.txt
python run.py
```

The backend server will host on: `http://localhost:8000`

### 2. Frontend Setup

Prerequisites: Node.js v16+

```bash
cd frontend
npm install
npm run dev
```

The frontend will run on: `http://localhost:5173`

## Usage Workflow

1. Open the UI at `http://localhost:5173/`.
2. Drag and drop the `sample_grid_data_3phase.xlsx` or equivalent.
3. Once uploaded, click "Start Phase Mapping Pipeline".
4. The system will perform PCA, t-SNE, DBSCAN, and KNN noise filling.
5. Watch the dashboard dynamically update with visualizations and metric scores.
6. Download the final labeled CSV predictions directly mapped to physical phases A, B, and C.

## Assumptions
- Voltage data must share common timestamps.
- Ground truth is only used for final cluster labeling and evaluation, not model fitting.
