import React from 'react';
import './JobSectorItem.css'

const JobSectorItem = props => {
    return (
        <li className="user-item">
            <div className="user-item__content">
                <div className="user-item__image">
                    <img src={props.image} alt={props.name} />
                </div>
                <div className="user-item__info"> 
                  <h2>{props.name}</h2>
                </div>
            </div>

        </li>

    );
};
 
export default JobSectorItem;