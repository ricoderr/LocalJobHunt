import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";
import { loginService } from "../services/authServices";

import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const LoginComponent = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);

  const [loginData, setLoginData] = useState({
    identifier: "",
    password: "",
  });

  const handleChange = async (e) => {
    const { name, value } = e.target;

    setLoginData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      toast.promise(
        loginService(loginData),
        {
          pending: "logging in.....",
          success: "Login successful",
          error: {
            render({ data }) {
              return data.data?.message || "Login failed!";
            },
          },
        }
        // console.log(data.status);
      );
    } catch (error) {
      toast.error("Internal server error!");
      console.error(error.response?.data?.non_field_errors || "Login failed!");
    }
  };

  return (
    <div>
      <form onSubmit={(e) => handleLogin(e, loginData)} className="space-y-1">
        <div className="space-y-1.5">
          <label
            htmlFor="identifier"
            className="text-neutral-900 text-base font-semibold block"
          >
            Email
          </label>
          <input
            id="identifier"
            name="identifier"
            type="text"
            placeholder="Enter your email address / username"
            value={loginData.identifier}
            onChange={handleChange}
            required
            className="w-full h-12 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4"
          />
        </div>

        <div className="space-y-1.5">
          <div className="flex items-center justify-between">
            <label
              htmlFor="password"
              className="text-neutral-900 text-base font-semibold"
            >
              Password
            </label>
            <a
              href="/forgot-password"
              className="text-sm text-green-600 hover:text-green-700 transition-colors font-medium"
            >
              Forgot Password?
            </a>
          </div>
          <div className="relative">
            <input
              id="password"
              name="password"
              type={showPassword ? "text" : "password"}
              placeholder="Enter your password"
              value={loginData.password}
              onChange={handleChange}
              required
              className="w-full h-12 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4 pr-12"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-neutral-400 hover:text-neutral-600 transition-colors"
            >
              {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
            </button>
          </div>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full h-12 bg-green-800 hover:bg-green-900 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold text-base transition-colors rounded-xl mt-5"
        >
          {isLoading ? "Logging in..." : "Log in"}
        </button>
      </form>

      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop
        closeOnClick
        pauseOnHover
        draggable
      />
    </div>
  );
};

export default LoginComponent;
