import React from "react";
import p from "./MyPosts.module.css";
import Post from "./Post/Post";
import { Field, reduxForm } from "redux-form";

const MyPosts = (props) => {

let postsElements = props.posts.map((p) =>
  <Post id={p.id} message={p.message} key={p.id} likesCount={p.likesCount} />)

let newPostElement = React.createRef();

let onAddPost = (values) => {
   props.addPost(values.newPostText);
  }

  return (
    <div className={p.main}>
      <h3>My posts</h3>
      <AddNewPostFormRedux onSubmit={onAddPost} />
      <div className={p.posts}>
        { postsElements }
      </div>
    </div>
  );
};

let AddNewPostForm = (props) => {
  return (
    <form onSubmit={props.handleSubmit}>
        <div>
          <Field component="textarea" name="newPostText" />
        </div>
        <div>
          <button>Add new post</button>
        </div>
      </form>
  )
}

let AddNewPostFormRedux = reduxForm({form: "ProfileAddNewPostForm"}) (AddNewPostForm);

export default MyPosts;
