import { createContext, useState, useEffect } from "react";
import { auth } from "../firebase/firebase.utils";
const AuthUserContext = createContext();

export const AuthUserContextProvider = ({ children }) => {
  const [authUser, setAuthUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(true);
    const unsubscribe = auth.onAuthStateChanged((user) => {
      if (user) {
        setAuthUser(user);
      }
      setIsLoading(false);
    });

    return () => unsubscribe();
  }, []);

  return (
    <AuthUserContext.Provider value={{ authUser, setAuthUser, isLoading }}>
      {children}
    </AuthUserContext.Provider>
  );
};

export default AuthUserContext;
