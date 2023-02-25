// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBKU_gcYDFu-LyRgIi1jw3xT3Vs0rTyM7Q",
  authDomain: "intuition-jugaadus.firebaseapp.com",
  projectId: "intuition-jugaadus",
  storageBucket: "intuition-jugaadus.appspot.com",
  messagingSenderId: "914492053300",
  appId: "1:914492053300:web:b6fab35d94522f69027761",
  measurementId: "G-FJ5G02ZK9N"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
export {app, auth};