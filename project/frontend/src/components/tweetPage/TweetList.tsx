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
  const handleRetweet = (tweet: Tweet) => {
    // Implement retweet functionality here
    console.log("Retweeting:", tweet);
  };

  return (
    <div>
      {tweets.map((tweet, index) => (
        <div key={index} style={{ position: 'relative', border: '1px solid #ccc', borderRadius: '5px', padding: '10px', marginBottom: '10px' }}>
          <p>{tweet.user}</p>
          <p>{tweet.message}</p>
          <button onClick={() => handleRetweet(tweet)} style={{ position: 'absolute', bottom: '5px', right: '5px' }}>Retweet</button>
        </div>
      ))}
    </div>
  );
};

export default TweetList;
