import React, { useState } from "react";
import SignupPage from "./SignupPage";
import VerifyOtp from "../../features/auth/components/VerifyOtp";

const AuthPage = () => {
  const [currentPage, setCurrentPage] = useState("signup");
  const [userEmail, setUserEmail] = useState("");

  const handleSignupSuccess = (email) => {
    // console.log(email);
    setUserEmail(email);
    setCurrentPage("verify-otp");
  };

  const handleVerifyOtpSuccess = () => {
    setCurrentPage("signup");
  };

  const handleBackToSignup = () => {
    setCurrentPage("signup");
    setUserEmail("");
  };

  return (
    <div>
      {currentPage === "signup" && (
        <SignupPage onSignupSuccess={handleSignupSuccess} />
      )}
      {currentPage === "verify-otp" && (
        <VerifyOtp
          onUserEmail={userEmail}
          onVerifyOtpSuccess={handleVerifyOtpSuccess}
          onBack={handleBackToSignup}
        />
      )}
      {/* {currentPage === "home" } */}
    </div>
  );
};

export default AuthPage;
