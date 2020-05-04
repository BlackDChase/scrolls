import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core";

const PolicyText = "Scrolls Privacy Policy\n";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.grey["100"],
    overflow: "hidden",
    //background: `url(${backgroundShape}) no-repeat`,
    backgroundSize: "cover",
    backgroundPosition: "0 400px",
    padding: 50
  }
}));

export const PrivacyPolicyComponent = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Typography style={{ whiteSpace: "pre-line" }}>{PolicyText}</Typography>
    </div>
  );
};
