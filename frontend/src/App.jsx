import { useState } from 'react'
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