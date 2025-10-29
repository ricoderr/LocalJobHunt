import "./App.css";
import React from "react";
import HomePage from "./pages/homePage";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import AuthPage from "./pages/auth_pages/AuthPage";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route element={<HomePage />} path="/"></Route>
          <Route element={<AuthPage />} path="/auth" />
          {/* <Route element={AuthPage} path="/authenticate" /> */}
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
