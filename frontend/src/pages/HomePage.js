import React from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

const HomePage = () => {
  return (
    <div
      className="d-flex justify-content-center align-items-center vh-100"
      style={{
        backgroundImage: "url('https://source.unsplash.com/random/1600x900')",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      <div
        className="card text-center shadow-lg p-4"
        style={{
          width: "500px",
          backdropFilter: "blur(10px)",
          background: "rgba(255, 255, 255, 0.8)",
          borderRadius: "15px",
        }}
      >
        <h1 className="text-primary">Chào mừng bạn!</h1>
        <p className="lead">Đây là trang chủ của bạn.</p>

        <div className="mt-3">
          <Link to="/login" id = "homeLoginButton" className="btn btn-outline-primary me-2">
            Đăng nhập
          </Link>
          <Link to="/register" className="btn btn-outline-success">
            Đăng ký
          </Link>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
