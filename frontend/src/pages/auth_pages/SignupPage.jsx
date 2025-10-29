import React, { useState } from "react";
import { Link } from "react-router-dom";
import SignupForm from "../../components/auth_components/SignupForm";

const SignupPage = () => {
  return (
    <>
      <main className="min-h-screen bg-slate-950 flex items-center justify-center p-4 relative overflow-hidden ">
        <div className="w-full max-w-md relative z-10">
          <div className="bg-white/5 rounded-2xl shadow-2xl p-8 border border-white/20">
            <div className="text-center mb-8">
              <h1 className="text-3xl font-bold text-white mb-2">
                Create Account
              </h1>
              <p className="text-white/80">Join us today and get started</p>
            </div>

            {/* Forms */}
            <SignupForm />

            {/* Toggle */}
            <div className="mt-6 text-center">
              <p className="text-white/80 text-sm">
                Already have an account?
                <Link to="/login">
                  <button className="text-white font-semibold hover:underline transition-all">
                    Login
                  </button>
                </Link>
              </p>
            </div>
          </div>

          {/* Footer */}
          <p className="text-center text-white/70 text-xs mt-6">
            Your data is secure and encrypted
          </p>
        </div>
      </main>
    </>
  );
};

export default SignupPage;
