import React, { useState, useEffect } from 'react';
import TweetList from './TweetList';
import TweetForm from './TweetForm';
import {getTweets} from './getTweet'

interface Tweet {
  timestamp: string; 
  user: string; 
  message: string; 
}

const Home: React.FC = () => {
  const [tweets, setTweets] = useState<Tweet[]>([]);

  useEffect(() => {
    fetchTweets();
  }, []);

  const fetchTweets = async () => {
    try {
      const response = await getTweets();
      const formattedTweets = response.map((tweet: { timestamp: string, user: string, message: string }) => ({
        timestamp: tweet.timestamp,
        user: tweet.user,
        message: tweet.message
      }));
      setTweets(formattedTweets);
    } catch (error) {
      console.error('Error fetching tweets:', error);
    }
  };

  return (
    <div>
      <h1>Home</h1>
      <TweetForm />
      <TweetList tweets={tweets} />
    </div>
  );
};

export default Home;
