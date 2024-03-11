import React, { useState, useEffect } from 'react';
import TweetList from './TweetList';
import TweetForm from './TweetForm';
import { getTweets, getTweetsUser, getTweetsTopic, getAllTopics } from './getTweet';

interface Tweet {
  timestamp: string;
  user: string;
  message: string;
}

const Home: React.FC = () => {
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [filterOption, setFilterOption] = useState<string>('all');
  const [inputValue, setInputValue] = useState<string>('');
  const [topics, setTopics] = useState<string[]>([]); 

  useEffect(() => {
    fetchTopics(); 
  }, []);

  useEffect(() => {
    fetchTweets();
  }, [filterOption]);

  const fetchTweets = async () => {
    try {
      let response;

      if (filterOption === '') {
        response = await getTweets();
      } 
      else if (filterOption.startsWith('topic:')) {
        const topic = filterOption.substring(6);
        response = await getTweetsTopic(topic);
      } 
      else {
        const username = filterOption;
        response = await getTweetsUser(username);
        console.log(response);
      }
      

      const formattedTweets = response.map((tweet: { timestamp: string; user: string; message: string }) => ({
        timestamp: tweet.timestamp,
        user: tweet.user,
        message: tweet.message
      }));

      setTweets(formattedTweets);
    } catch (error) {
      console.error('Error fetching tweets:', error);
    }
  };

  const fetchTopics = async () => { 
    try {
      const topicsResponse = await getAllTopics();
      setTopics(topicsResponse); 
    } catch (error) {
      console.error('Error fetching topics:', error);
    }
  };

  const handleFilterChange = () => {
    if (inputValue.trim() === '') {
      alert('Please enter a value before filtering.');
      return;
    }
    setFilterOption(`${inputValue.trim()}`);
    setInputValue('');
  };



  const handleShowAll = () => {
    setFilterOption('');
  };

  const handleShowAllMine = () => {
    const email = localStorage.getItem('email');
    setFilterOption(`${email}`);
  };

  const handleLogout = async () => {
    try {
      const response = await fetch('http://localhost:5000/logout', {
        method: 'GET',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      if (response.ok) {
        localStorage.clear();
        console.log('Logged out successfully');
        window.location.href = 'http://127.0.0.1:5173/signin'; 
      } else {
        console.error('Failed to logout');
      }
    } catch (error) {
      console.error('Error logging out:', error);
    }
  };

  return (
    <div>
      {/* Blue banner */}
      <div style={{ backgroundColor: 'blue', color: 'white', padding: '10px', width: '100%', textAlign: 'center' }}>
        Welcome to the Tweet App!
      </div>

      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1, width: '100vw', borderRight: '1px solid #ccc', padding: '10px' }}>
      
        </div>
        <div style={{ flex: 2, width: '100vw', borderRight: '1px solid #ccc', padding: '10px' }}>
         
          <TweetForm />
          <TweetList tweets={tweets} />
        </div>
        <div style={{ flex: 1, width: '100vw', display: 'flex', flexDirection: 'column',  alignItems: 'center', padding: '10px' }}>
      
          <div style={{ marginBottom: '10px' }}> 
            <label htmlFor="inputField">Search by username:</label>
            <input
              type="text"
              id="inputField"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <button onClick={handleFilterChange}>Filter</button>
            <button onClick={handleShowAll}>Show All</button>
            <button onClick={handleShowAllMine}>Show my tweets</button>
          </div>
   
          <div>
            <label htmlFor="topicSelect">Select topic:</label>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              {topics.map(topic => (
                <div key={topic} style={{ border: '1px solid black', borderRadius: '5px', margin: '5px', padding: '5px', width: '200px' }}>
                  <button
                    onClick={() => setFilterOption(`topic:${topic}`)}
                    style={{ margin: '5px', width: '100%' }}
                  >
                    {topic}
                  </button>
                </div>
              ))}
            </div>
          </div>

          <button
            onClick={handleLogout}
            style={{ position: 'fixed', bottom: '10px', right: '10px', width: '200px', border: '1px solid blue'}}
          >
            Logout
          </button>

        </div>

      </div>
    </div>

  );
};

export default Home;
