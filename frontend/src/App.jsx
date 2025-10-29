import "./App.css";
import React from "react";
import HomePage from "./pages/homePage";
import { Route, Routes, BrowserRouter } from "react-router-dom";
// import AuthPage from "./pages/auth_pages/AuthPage";
import LoginPage from "./pages/auth_pages/LoginPage";
import SignupPage from "./pages/auth_pages/SignupPage";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route element={<HomePage />} path="/"></Route>
          {/* <Route element={<AuthPage />} path="/auth" /> */}
          <Route element={<LoginPage />} path="/login" />
          <Route element={<SignupPage />} path="/signup" />
          {/* <Route element={AuthPage} path="/authenticate" /> */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
