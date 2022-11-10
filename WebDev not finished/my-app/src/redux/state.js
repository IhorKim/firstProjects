import profileReducer from "./profile-reducer";
import dialogsReducer from "./dialogs-reducer";
import sidebarReducer from "./sidebar-reducer";

let store = {
  _state: {
  profilePage: {
      posts: [
      {id: 1, message: 'Hi', likesCount: 20}, 
      {id: 2, message: 'How is it going?', likesCount: 17},
      {id: 3, message: 'Miss you!', likesCount: 27},  
  ],
  newPostText: '',    
        },
  
  dialogsPage: {
      dialogs: [
          { id: 1, name: "Ihor" },
          { id: 2, name: "Iryna" },
          { id: 3, name: "Viktoriia" },
          { id: 4, name: "Vova" },
          { id: 5, name: "Liuda" },
          { id: 6, name: "Sashlyk" },
        ],
      messages: [
          { id: 1, message: "Hi" },
          { id: 2, message: "How is it going?" },
          { id: 3, message: "How are you?" },
          { id: 4, message: "Yo" },
          { id: 5, message: "Privet" },
          { id: 6, message: "Kak ty?" },
        ],
      newMessageText: '',    
  },
  sidebar: {},
          },
  _callSubscriber() {
            console.log('State changed');
                 },

  getState() {
    return this._state;
  },        
  subscribe(observer) {
    this._callSubscriber = observer;
  },
  
  dispatch(action) {
    this._state.profilePage = profileReducer(this._state.profilePage, action);
    this._state.dialogsPage = dialogsReducer(this._state.dialogsPage, action);
    this._state.sidebar = sidebarReducer(this._state.sidebar, action);
    
    this._callSubscriber(this._state);
  }
};

export default store;
  window.store = store;

// store OOP