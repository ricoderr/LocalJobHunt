import React, { useState } from "react";
import LoginForm from "../../components/auth_components/LoginForm";
import SignupForm from "../../components/auth_components/SignupForm";

const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);
  return (
    <>
      <main className="min-h-screen bg-slate-950 flex items-center justify-center p-4 relative overflow-hidden ">
        <div className="w-full max-w-md relative z-10">
          <div className="bg-white/5 rounded-2xl shadow-2xl p-8 border border-white/20">
            <div className="text-center mb-8">
              <h1 className="text-3xl font-bold text-white mb-2">
                {isLogin ? "Welcome Back" : "Create Account"}
              </h1>
              <p className="text-white/80">
                {isLogin
                  ? "Sign in to your account to continue"
                  : "Join us today and get started"}
              </p>
            </div>

            {/* Forms */}
            {isLogin ? <LoginForm /> : <SignupForm />}

            {/* Toggle */}
            <div className="mt-6 text-center">
              <p className="text-white/80 text-sm">
                {isLogin
                  ? "Don't have an account? "
                  : "Already have an account? "}
                <button
                  onClick={() => setIsLogin(!isLogin)}
                  className="text-white font-semibold hover:underline transition-all"
                >
                  {isLogin ? "Sign up" : "Sign in"}
                </button>
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

export default AuthPage;
