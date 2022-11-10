import React from "react";
import p from "./Post.module.css";

const Post = (props) => {
  return (
    <div className={p.item}>
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRK6sjWdHxkeaLO1a_iRWSI7mpaT95ePH3PGg&usqp=CAU" />
      { props.message }
      <div>
            <span>Likes:</span> { props.likesCount }
      </div>
    </div>
  );
};

export default Post;
