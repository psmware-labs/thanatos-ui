import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';
import { Header, List } from 'semantic-ui-react';

function App() {
  const [accounts, setAccounts] = useState([])

  useEffect( () => {
    axios.get('http://localhost:5000/api/accounts/accounts/').then(response => {
      console.log(response);
      setAccounts(response.data);
    })
  }, [])

  return (
    <div>
      <Header as='h2' icon='users' content='Thanatos'/>
      <List>
      { accounts.map((activity: any) => (
            <List.Item key={activity.id}>
              { activity.name }
            </List.Item>
          ) ) }

      </List>

    </div>
  );
}

export default App;
