const ADD_MESSAGE = "ADD-MESSAGE";

let initialState = {
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
  
};

const dialogsReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_MESSAGE:
      let newMessage = {
        id: 7,
        message: action.newMessageText,
      };
      return {
        ...state,
        messages: [...state.messages, newMessage],
      };
    
    default:
      return state;
  }
};

export const addMessageActionCreator = (newMessageText) => {
  return {
    type: ADD_MESSAGE,
    newMessageText: newMessageText
  };
};

export default dialogsReducer;
