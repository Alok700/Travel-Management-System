# Travel Management System using GIS and Remote Sensing

## 🚀 Project Setup Guide

### 🔧 Prerequisites
- Python 3.8+
- Node.js & npm
- PostgreSQL with PostGIS
- QGIS (for offline processing)
- Git (optional)

### 📁 Folder Structure
- `backend/`: Flask API with route optimization and weather/RS data
- `frontend/`: React UI using Leaflet for map display
- `data/`: Sample satellite & GIS datasets
- `gis_processing/`: Scripts for spatial analysis
- `remote_sensing/`: Scripts to fetch/process satellite data

---

## 🛠️ Backend Setup (Flask + PostGIS)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

---

## 🌐 Frontend Setup (React + Leaflet)

```bash
cd frontend
npm install
npm start
```

---

## 🌍 GIS & Remote Sensing Data

- Add shapefiles, GeoTIFFs, and JSONs to `data/`
- Scripts in `gis_processing/` can convert to GeoJSON
- `remote_sensing/` has APIs to download NDVI or weather maps

---

## ✅ Sample Use Cases
- Route optimization avoiding flood zones
- Suggesting routes based on air quality or temperature
- Highlighting vegetation-dense areas for eco-tourism

---


