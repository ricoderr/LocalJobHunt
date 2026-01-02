import axios from "axios";

const apiUrl = import.meta.env.VITE_BASE_URL;

export async function loginService(loginData) {
  try {
    const response = await axios.post(`${apiUrl}auth/login/`, loginData);
    // console.log(response);

    return response;
  } catch (error) {
    console.error(error.response?.data?.non_field_errors || error.message);
    throw error;
  }
}

export async function signupService(signupData) {
  try {
    const response = await axios.post(`${apiUrl}auth/signup/`, signupData);
    // console.log(response);

    return response;
  } catch (error) {
    console.error(error.response?.data?.non_field_errors || error.message);
    throw error;
  }
}
