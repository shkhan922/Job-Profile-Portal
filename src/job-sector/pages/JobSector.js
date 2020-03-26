import React from 'react';

import JobSectorList from '../components/JobSectorList'

const JobSectors = () => {
   const JOBSECTORS = [ { 
       id:'j1', name:'Browse By Sector', image:""
   }];
 return <JobSectorList items={JOBSECTORS} / >;

};

export default JobSectors;