import "../styles/globals.scss";
import type { AppProps } from "next/app";
import { AuthUserContextProvider } from "../context/AuthUserContext";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthUserContextProvider>
      <Component {...pageProps} />
    </AuthUserContextProvider>
  );
}

export default MyApp;
