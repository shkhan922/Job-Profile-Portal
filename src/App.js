import React from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch} from 'react-router-dom';

import JobSectors from './job-sector/pages/JobSector';
import NewProfiles from './job-profile/pages/NewProfile';

const App = () => {
  return <Router>
    <Switch>
    <Route path="/" exact>
    <JobSectors/>
    </Route>
    <Route path="/jobprofile/new">
    <NewProfiles/>
    </Route>
    <Redirect to='/' />
    </Switch>
  </Router>;
}

export default App;
