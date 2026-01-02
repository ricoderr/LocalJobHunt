import "./App.css";
import LoginPage from "./pages/auth/LoginPage";
import { Routes, Route, BrowserRouter as Router } from "react-router-dom";
import SignupPage from "./pages/auth/SignupPage";
import VerifyOtp from "./features/auth/components/VerifyOtp";
import AuthPage from "./pages/auth/AuthPage";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route element={<LoginPage />} path="/login"></Route>
          <Route element={<AuthPage />} path="/signup"></Route>
          <Route element={<VerifyOtp />} path="/verify-otp"></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
