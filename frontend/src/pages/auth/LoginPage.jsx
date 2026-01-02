import { Link } from "react-router-dom";
import LoginComponent from "../../features/auth/components/LoginComponent";
// import { useState } from "react";

const LoginPage = () => {
  return (
    <>
      <div className="min-h-screen bg-neutral-50 flex items-center justify-center p-4">
        <div className="w-full max-w-[440px]">
          <div className="bg-white border border-neutral-200 rounded-3xl p-8 shadow-sm">
            <h1 className="text-[2rem] font-bold text-neutral-900 text-center mb-6 tracking-tight">
              Login
            </h1>

            <button
              type="button"
              className="w-full h-12 bg-white border border-neutral-300 hover:bg-neutral-50 text-neutral-700 text-base font-medium rounded-xl transition-colors mb-5"
            >
              Continue with Google
            </button>

            <div className="relative my-6">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-neutral-200"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-4 bg-white text-neutral-400">or</span>
              </div>
            </div>

            <LoginComponent />

            <div className="mt-5 text-center">
              <p className="text-neutral-600 text-sm">
                Don't have an account?{" "}
                <a
                  href="/signup"
                  className="text-green-600 hover:text-green-700 font-semibold transition-colors"
                >
                  Sign up
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginPage;
