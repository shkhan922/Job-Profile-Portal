import React from 'react';
import './JobSectorList.css'
//import JobSectors from '../pages/JobSector';
import JobSectorItem from './JobSectorItem';

const JobSectorList = props => {
    if (props.items.length === 0) {
        return (
        <div className="center"> 
        <h2> No Job Sector Found</h2>
        </div>
        );
    }
    return <ul>
   {props.items.map(JobSectors => {
       return <JobSectorItem
          key={JobSectors.id}
          id={JobSectors.id}
          image={JobSectors.image}
          name= {JobSectors.name}
       />; 
   })}
    </ul>;
};
 
export default JobSectorList;
