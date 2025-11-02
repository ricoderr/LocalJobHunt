import React, { useState } from "react";
import LoginForm from "../../components/auth_components/LoginForm";
import { Link } from "react-router-dom";

// const Base_url = import.meta.env.VITE_API_URL;

const LoginPage = () => {
  return (
    <>
      <main className="min-h-screen bg-slate-950 flex items-center justify-center p-4 relative overflow-hidden ">
        <div className="w-full max-w-md relative z-10">
          <div className="bg-white/5 rounded-2xl shadow-2xl p-8 border border-white/20">
            <div className="text-center mb-8">
              <h1 className="text-3xl font-bold text-white mb-2">Welcome!</h1>
              <p className="text-white/80">
                Login in to your account to continue"
              </p>
            </div>

            {/* Forms */}
            <LoginForm />

            {/* Toggle */}
            <div className="mt-6 text-center">
              <p className="text-white/80 text-sm">
                "Don't have an account? "
                <Link to="/signup">
                  <button className="text-white font-semibold hover:underline transition-all">
                    Sign up
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

export default LoginPage;
