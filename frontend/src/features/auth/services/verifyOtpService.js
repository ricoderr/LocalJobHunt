import axios from "axios";

const apiUrl = import.meta.env.VITE_BASE_URL;

export const verifyOtpService = async (payload) => {
  try {
    const response = await axios.post(`${apiUrl}auth/verify-otp/`, payload);
    console.log(response);

    return response;
  } catch (error) {
    console.log(error);
  }
};
