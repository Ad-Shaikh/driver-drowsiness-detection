import type { NextPage } from "next";
import { useState, useContext } from "react";
import {
  AppShell,
  Burger,
  Header,
  MediaQuery,
  Navbar,
  Text,
  useMantineTheme,
  SimpleGrid,
  Button
} from "@mantine/core";
import { auth, signInWithGoogle, signOut } from "../firebase/firebase.utils";
import AuthUserContext from "../context/AuthUserContext";

const Home: NextPage = () => {
  const [opened, setOpened] = useState(false);
  const theme = useMantineTheme();
  const { authUser, setAuthUser } = useContext(AuthUserContext);

  console.log(authUser);

  const handleLogin = () => {
    if (!authUser) {
      signInWithGoogle().then((results) =>
        auth.onAuthStateChanged((user) => {
          setAuthUser(user);
        })
      );
    } else {
      signOut().then(() => {
        setAuthUser(null);
      });
    }
  };

  return (
    <AppShell
      // navbarOffsetBreakpoint controls when navbar should no longer be offset with padding-left
      navbarOffsetBreakpoint="sm"
      // fixed prop on AppShell will be automatically added to Header and Navbar
      fixed
      navbar={
        <Navbar
          padding="md"
          // Breakpoint at which navbar will be hidden if hidden prop is true
          hiddenBreakpoint="sm"
          // Hides navbar when viewport size is less than value specified in hiddenBreakpoint
          hidden={!opened}
          // when viewport size is less than theme.breakpoints.sm navbar width is 100%
          // viewport size > theme.breakpoints.sm – width is 300px
          // viewport size > theme.breakpoints.lg – width is 400px
          width={{ sm: 300, lg: 400 }}
        >
          <SimpleGrid cols={1}>
            <Button variant="subtle" color="teal">
              Home
            </Button>
            <Button variant="subtle" color="teal">
              Notifications
            </Button>
            <Button variant="subtle" color="teal">
              Logs
            </Button>
            <Button variant="subtle" color="teal" onClick={handleLogin}>
              {!authUser ? "Login" : "Logout"}
            </Button>
          </SimpleGrid>
        </Navbar>
      }
      header={
        <Header height={70} padding="md">
          {/* Handle other responsive styles with MediaQuery component or createStyles function */}
          <div
            style={{ display: "flex", alignItems: "center", height: "100%" }}
          >
            <MediaQuery largerThan="sm" styles={{ display: "none" }}>
              <Burger
                opened={opened}
                onClick={() => setOpened((o) => !o)}
                size="sm"
                color={theme.colors.gray[6]}
                mr="xl"
              />
            </MediaQuery>

            <Text>Driver Drowsiness System</Text>
          </div>
        </Header>
      }
    >
      <Text>Resize app to see responsive navbar in action</Text>
    </AppShell>
  );
};

export default Home;
