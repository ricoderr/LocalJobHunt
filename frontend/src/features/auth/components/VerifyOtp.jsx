import { useState, useRef } from "react";
import { verifyOtpService } from "../services/verifyOtpService";

export default function VerifyOtp({ onBack, onUserEmail, onVerifyOtpSuccess }) {
  const email = onUserEmail;

  const [otp, setOtp] = useState(["", "", "", "", "", ""]);
  const inputRefs = useRef([]);

  const handleChange = (index, value) => {
    if (value.length > 1) return;

    const newOtp = [...otp];
    newOtp[index] = value;
    setOtp(newOtp);

    // Auto-focus next input
    if (value && index < 5) {
      inputRefs.current[index + 1]?.focus();
    }
  };

  const handleKeyDown = (index, e) => {
    // Handle backspace
    if (e.key === "Backspace" && !otp[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handleSubmit = async () => {
    // console.log("Button Clicked");
    const otpCode = otp.join("");
    const payload = {
      code: otpCode,
      email: email,
    };

    try {
      const data = await verifyOtpService(payload);
      console.log(data);

      onVerifyOtpSuccess();
      // onBack("signup");
      //   return data;
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-6">
      <div className="w-full max-w-110 animate-in fade-in zoom-in-95 duration-700">
        <div className="text-center mb-16">
          <h1 className="text-5xl font-serif text-foreground mb-6">
            <span className="text-green-800">Security </span>Verification
          </h1>
          <p className="text-muted-foreground leading-relaxed">
            Please enter the authentication code sent to your primary email.
          </p>
        </div>

        <div className="space-y-12">
          <div className="flex justify-between gap-3">
            {otp.map((digit, index) => (
              <input
                key={index}
                ref={(el) => (inputRefs.current[index] = el)}
                type="text"
                maxLength="1"
                value={digit}
                onChange={(e) => handleChange(index, e.target.value)}
                onKeyDown={(e) => handleKeyDown(index, e)}
                className="w-full h-16 text-center text-green-500 text-3xl font-serif bg-transparent border-0 border-b-2 border-border focus:border-primary focus:outline-none transition-all duration-300"
              />
            ))}
          </div>

          <button
            type="button"
            onClick={handleSubmit}
            className="w-full h-14 text-amber-50 bg-green-800  hover:bg-green-700  transition-all duration-300 text-sm uppercase tracking-[0.2em] font-bold"
          >
            Confirm Code
          </button>
        </div>

        <div className="mt-16 text-center space-y-6">
          <p className="text-xs uppercase tracking-widest text-muted-foreground font-medium">
            No code received?{" "}
            <button className="font-bold text-green-600 hover:text-green-800 border-b border-foreground/20 transition-colors">
              Resend
            </button>
          </p>

          <a
            href="/login"
            className="block text-xs uppercase tracking-widest text-muted-foreground/60 hover:text-foreground transition-colors font-bold"
          >
            ← Change Credentials
          </a>
        </div>
      </div>
    </div>
  );
}
