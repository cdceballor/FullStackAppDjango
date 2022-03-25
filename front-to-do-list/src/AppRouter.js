import React from 'react';
import { Container } from 'reactstrap';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import WelcomePage from './feature/WelcomePage';

const baseUrl = document.getElementsByTagName('base')[0].getAttribute('href');

export default function AppRouter() {

  return (
    <BrowserRouter basename={baseUrl}>
      {/* <NavMenu /> */}
      <Switch>
        <Container>
          <Route exact path='/' component={WelcomePage} />
        </Container>
      </Switch>
    </BrowserRouter>
  );
}

