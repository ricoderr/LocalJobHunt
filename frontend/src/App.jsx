import "./App.css";
import LoginPage from "./pages/auth/LoginPage";
import { Routes, Route, BrowserRouter as Router } from "react-router-dom";
import SignupPage from "./pages/auth/SignupPage";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route element={<LoginPage />} path="/login"></Route>
          <Route element={<SignupPage />} path="/signup"></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
