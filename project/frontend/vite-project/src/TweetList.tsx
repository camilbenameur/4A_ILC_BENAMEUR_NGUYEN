import React from 'react';

interface Tweet {
  timestamp: string;
  user: string;
  message: string;
}

interface TweetListProps {
  tweets: Tweet[];
}

const TweetList: React.FC<TweetListProps> = ({ tweets }) => {
  return (
    <div>
      
      {tweets.map(tweet => (
        <div key={tweet.timestamp} style={{ border: '1px solid black', padding: '10px', marginBottom: '10px' }}>
          <h3>{tweet.user}</h3>
          <p>{tweet.message}</p>
        </div>
      ))}
    </div>
  );
};

export default TweetList;
