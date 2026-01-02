import React, { useState } from "react";
import SignupPage from "./SignupPage";
import VerifyOtp from "../../features/auth/components/VerifyOtp";

const AuthPage = () => {
  const [currentPage, setCurrentPage] = useState("signup");
  const [userPhoneNumber, setUserPhoneNumber] = useState("");

  useEffect(() => {
    console.log("currentPage changed to:", currentPage);
  }, [currentPage]);

  const handleSignupSuccess = (phone_number) => {
    setUserPhoneNumber(phone_number);
    setTimeout(() => {
      setCurrentPage("verify-otp");
    }, 0);
  };

  const handleVerifyOtpSuccess = () => {
    setCurrentPage("");
  };

  const handleBackToSignup = () => {
    setCurrentPage("signup");
    setUserPhoneNumber("");
  };

  return (
    <div>
      {currentPage === "signup" && <SignupPage />}
      {currentPage === "verify-otp" && (
        <VerifyOtp
          onUserPhoneNumber={userPhoneNumber}
          onVerifyOtpSuccess={handleVerifyOtpSuccess}
        />
      )}
      {/* {currentPage === "home" } */}
    </div>
  );
};

export default AuthPage;
