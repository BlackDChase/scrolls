import React from "react";
import { BrowserRouter, Route } from "react-router-dom";
import { MainComponent } from "components/MainComponent/Main";

export default props => (
  <BrowserRouter>
    <Route exact path="/" component={MainComponent} />
  </BrowserRouter>
);
