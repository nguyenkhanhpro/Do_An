import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";
import RegisterPage from "./pages/RegisterPage";
import { AuthProvider } from "./context/AuthContext"; // Import AuthProvider

const App = () => {
  return (
    <AuthProvider> {/* Bọc toàn bộ ứng dụng */}
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/register" element={<RegisterPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
