import React from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch} from 'react-router-dom';

import JobSectors from './job-sector/pages/JobSector';
import NewProfiles from './job-profile/pages/NewProfile';
import MainNavigation from './shared/components/Navigation/MainNavigation';
//import NavLinks from '../src/shared/components/Navigation/NavLinks'

const App = () => { 
  console("app.js");
  return <h1>Test ii</h1>;
  // return <Router>
  //   <MainNavigation/>
  //   <main>
  //   <Switch>
  //   <Route path="/" exact>
  //   <JobSectors/>
  //   </Route>
  //   <Route path="/jobprofile/new">
  //   <NewProfiles/>
  //   </Route>
  //   <Redirect to='/' />
  //   </Switch>
  //   </main>
  // </Router>;
}

export default App;
