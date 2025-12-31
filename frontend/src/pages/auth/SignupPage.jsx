import React from "react";
import SignupComponent from "../../features/auth/components/SignupComponent";

const SignupPage = () => {
  return (
    <>
      <div className="min-h-screen bg-neutral-50 flex items-center justify-center p-4">
        <div className="w-full max-w-110">
          <div className="bg-white border border-neutral-200 rounded-3xl p-6 shadow-sm">
            <h1 className="text-[1.75rem] font-bold text-neutral-900 text-center mb-4 tracking-tight">
              Sign Up
            </h1>

            <div className="relative my-4">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-neutral-200"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-4 bg-white text-neutral-400">or</span>
              </div>
            </div>

            <SignupComponent />

            <div className="mt-4 text-center">
              <p className="text-neutral-600 text-sm">
                Already have an account?{" "}
                <a
                  href="/login"
                  className="text-green-600 hover:text-green-700 font-semibold transition-colors"
                >
                  Log in
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignupPage;
