import React from "react";
import Preloader from "../../common/Preloader/Preloader";
import p from "./ProfileInfo.module.css";
import ProfileStatus from "./ProfileStatus";
import { updateStatus } from "../../../redux/profile-reducer";


const ProfileInfo = (props) => {
  if (!props.profile) {
    return <Preloader />
  }

  return (
    <div>
      
     <div>
      <img src={require("./../../../mainimage.jfif")} className={p.img}/>
      </div>

      <div className={p.descriptionBlock}>
        <img src={props.profile.photos.large} />
        <div>Description:</div>
        <div><text>{props.profile.aboutMe}</text></div> 
        <div><text>{props.profile.contacts.facebook}</text></div>
        <div><text>{props.profile.fullName}</text></div>
        <ProfileStatus status={props.status} updateStatus={props.updateStatus} />
        </div>
      
    </div>
  );
};

export default ProfileInfo;
