import React from "react";
import { ThemeProvider } from "@material-ui/styles";
import { createMuiTheme } from "@material-ui/core/styles";
import { orange, yellow } from "@material-ui/core/colors";
import Routes from "routes";
import CssBaseline from "@material-ui/core/CssBaseline/CssBaseline";

const theme = createMuiTheme({
  palette: {
    secondary: {
      main: orange[900]
    },
    primary: {
      main: yellow[700]
    }
  }
});

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Routes />
      </ThemeProvider>
    </div>
  );
}

export default App;
