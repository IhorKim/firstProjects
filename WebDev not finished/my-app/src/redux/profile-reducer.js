import { usersAPI, profileAPI } from "../api/api";

const ADD_POST = 'ADD-POST';
const SET_USER_PROFILE = 'SET_USER_PROFILE';
const SET_STATUS = 'SET_STATUS';

let initialState = {
  posts: [
    {id: 1, message: 'Hi', likesCount: 20}, 
    {id: 2, message: 'How is it going?', likesCount: 17},
    {id: 3, message: 'Miss you!', likesCount: 27},  
],
profile: null,
status: ""
};

const profileReducer = (state = initialState, action) => {
    switch(action.type) {
        case ADD_POST: {
            let newPost = {
                id: 5,
                message: action.newPostText,
                likesCount: 0,
            };
          return {
              ...state,
              posts: [...state.posts, newPost],
              newPostText: ''
            };
          } 
        case SET_USER_PROFILE: {
          return {
            ...state,
            profile: action.profile}
        }
        case SET_STATUS: {
          return {
            ...state,
            status: action.status}
        }
        default:
            return state;
    }
}

export const addPostActionCreator = (newPostText) => {
    return {
      type: ADD_POST,
      newPostText: newPostText,
    }
  };
  
  export const setUserProfile = (profile) => {
    return {
      type: SET_USER_PROFILE, 
      profile: profile,
    }
  };

  export const getUserProfile = (userId) => (dispatch) => {
    usersAPI.getProfile(userId).then((response) => {
      dispatch(setUserProfile(response.data));
    });
  };

  export const setStatus = (status) => ({type: SET_STATUS, status})
  export const getStatus = (userId) => (dispatch) => {
    profileAPI.getStatus(userId).then((response) => {
      dispatch(getStatus(response.data));
    });
  };

  export const updateStatus = (status) => (dispatch) => {
    profileAPI.updateStatus(status).then((response) => {
      if (response.data.resultCode === 0) {
      dispatch(getStatus(status));
    }});
  };
 
export default profileReducer;