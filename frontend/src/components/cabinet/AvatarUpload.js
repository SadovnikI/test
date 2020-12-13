import axios from "axios";

export const modify_user = ({ id, username, avatar, password }) => (dispatch) => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // Request Body
  const body = JSON.stringify({ id, username, password, avatar });

  axios
    .put('/api/cabinet/modify_user', body, config)
    .then((res) => {
      dispatch({

      });
    })

};