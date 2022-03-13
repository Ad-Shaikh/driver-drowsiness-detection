import firebase from "firebase/app";
import "firebase/firestore";
import "firebase/auth";

// config goes here
var firebaseConfig = {
  apiKey: "AIzaSyAFtJcDH4nnGCkLp-qFPZv5L18JvmF-s7w",
  authDomain: "driver-drowsiness-system.firebaseapp.com",
  projectId: "driver-drowsiness-system",
  storageBucket: "driver-drowsiness-system.appspot.com",
  messagingSenderId: "940577751205",
  appId: "1:940577751205:web:59ff40dfa722d8f4078d4c"
};

if (firebase.apps.length === 0) {
  firebase.initializeApp(firebaseConfig);
}

export const auth = firebase.auth();
export const db = firebase.firestore();

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: "select_account" });
export const signInWithGoogle = () => auth.signInWithPopup(provider);
export const signOut = () => firebase.auth().signOut();

export default firebase;
