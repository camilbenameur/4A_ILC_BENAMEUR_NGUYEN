import React, { useState, useEffect } from 'react';
import TweetList from './TweetList';
import TweetForm from './TweetForm';
import { getTweets, getTweetsUser, getTweetsTopic } from './getTweet';

interface Tweet {
  timestamp: string;
  user: string;
  message: string;
}

const Home: React.FC = () => {
  const [tweets, setTweets] = useState<Tweet[]>([]);
  const [filterOption, setFilterOption] = useState<string>('all');
  const [inputValue, setInputValue] = useState<string>('');

  useEffect(() => {
    fetchTweets();
  }, [filterOption]); // Trigger fetchTweets whenever filterOption changes

  const fetchTweets = async () => {
    try {
      let response;

      if (filterOption === 'all') {
        response = await getTweets();
      } else if (filterOption.startsWith('user:')) {
        const username = filterOption.substring(5);
        response = await getTweetsUser(username);
      } else if (filterOption.startsWith('topic:')) {
        const topic = filterOption.substring(6);
        response = await getTweetsTopic(topic);
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

  const handleFilterChange = () => {
    if (inputValue.trim() === '') {
      alert('Please enter a value before filtering.');
      return;
    }
    setFilterOption(inputValue); // Update filterOption state
    setInputValue('');
  };

  const handleShowAll = () => {
    setFilterOption('all'); // Update filterOption state
  };

  return (
    <div>
      <h1>Home</h1>
      <div>
        <label htmlFor="inputField">Enter username or topic:</label>
        <input
          type="text"
          id="inputField"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button onClick={handleFilterChange}>Filter</button>
        <button onClick={handleShowAll}>Show All</button>
      </div>
      <TweetForm />
      <TweetList tweets={tweets} />
    </div>
  );
};

export default Home;
