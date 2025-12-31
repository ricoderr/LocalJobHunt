import React, { useState } from "react";
import { Eye, EyeOff } from "lucide-react";

import { signupService } from "../services/authServices";

const SignupComponent = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  const [signupData, setSignupData] = useState({
    Fname: "",
    Lname: "",
    phone_number: "",
    email: "",
    password: "",
    confirm_password: "",
  });

  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const data = await signupService(signupData);
      console.log(data);
    } catch (error) {
      console.error(error.response?.data?.non_field_errors || "Signup failed");
    }
  };

  const handleChange = async (e) => {
    const { name, value } = e.target;

    setSignupData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <>
      <form onSubmit={handleSignup} className="space-y-3">
        <div className="grid grid-cols-2 gap-3">
          <div className="space-y-1.5">
            <label
              htmlFor="Fname"
              className="text-neutral-900 text-sm font-semibold block"
            >
              First Name{" "}
            </label>
            <input
              id="Fname"
              name="Fname"
              value={signupData.Fname}
              onChange={handleChange}
              type="text"
              placeholder="First name"
              className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4"
            />
          </div>

          <div className="space-y-1.5">
            <label
              htmlFor="Lname"
              className="text-neutral-900 text-sm font-semibold block"
            >
              Last Name{" "}
            </label>
            <input
              id="Lname"
              name="Lname"
              value={signupData.Lname}
              onChange={handleChange}
              type="text"
              placeholder="Last name"
              className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4"
            />
          </div>
        </div>

        <div className="space-y-1.5">
          <label
            htmlFor="email"
            className="text-neutral-900 text-sm font-semibold block"
          >
            Email{" "}
            <span className="text-neutral-400 font-normal">(optional)</span>
          </label>
          <input
            id="email"
            name="email"
            value={signupData.email}
            onChange={handleChange}
            type="email"
            placeholder="Enter your email address"
            className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4"
          />
        </div>

        <div className="space-y-1.5">
          <label
            htmlFor="phone_number"
            className="text-neutral-900 text-sm font-semibold block"
          >
            Phone Number{" "}
          </label>
          <input
            id="phone_number"
            name="phone_number"
            value={signupData.phone_number}
            onChange={handleChange}
            type="tel"
            placeholder="Enter your phone number"
            className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4"
          />
        </div>

        <div className="space-y-1.5">
          <label
            htmlFor="password"
            className="text-neutral-900 text-sm font-semibold block"
          >
            Password
          </label>
          <div className="relative">
            <input
              id="password"
              name="password"
              value={signupData.password}
              onChange={handleChange}
              type={showPassword ? "text" : "password"}
              placeholder="Enter your password"
              required
              className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4 pr-12"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-neutral-400 hover:text-neutral-600 transition-colors"
            >
              {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
            </button>
          </div>
        </div>

        <div className="space-y-1.5">
          <label
            htmlFor="confirm_password"
            className="text-neutral-900 text-sm font-semibold block"
          >
            Confirm Password
          </label>
          <div className="relative">
            <input
              id="confirm_password"
              name="confirm_password"
              value={signupData.confirm_password}
              onChange={handleChange}
              type={showConfirmPassword ? "text" : "password"}
              placeholder="Confirm your password"
              required
              className="w-full h-11 bg-neutral-50 border border-neutral-200 text-neutral-900 placeholder:text-neutral-400 focus:outline-none focus:border-neutral-300 rounded-xl text-base px-4 pr-12"
            />
            <button
              type="button"
              onClick={() => setShowConfirmPassword(!showConfirmPassword)}
              className="absolute right-4 top-1/2 -translate-y-1/2 text-neutral-400 hover:text-neutral-600 transition-colors"
            >
              {showConfirmPassword ? <EyeOff size={18} /> : <Eye size={18} />}
            </button>
          </div>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full h-11 bg-green-800 hover:bg-green-900 disabled:opacity-50 disabled:cursor-not-allowed text-white font-semibold text-base transition-colors rounded-xl mt-4"
        >
          {isLoading ? "Creating account..." : "Sign up"}
        </button>
      </form>
    </>
  );
};

export default SignupComponent;
