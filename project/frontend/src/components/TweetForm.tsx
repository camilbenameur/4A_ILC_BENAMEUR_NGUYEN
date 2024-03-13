import React, { useState } from "react";
import { useTweets } from "../hooks/useTweets";

import { API_URL } from "../config";
import { Loader } from "./Loader";

export const postTweet = async (email: string | null, content: string) => {
  try {
    const response = await fetch(`${API_URL}/tweets`, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        tweet: content,
      }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error);
    }
  } catch (error) {
    throw error;
  }
};

const TweetForm: React.FC = () => {
  const [content, setContent] = useState("");
  const { mutate } = useTweets({});
  const [isLoading, setIsLoading] = useState(false);
  const email = localStorage.getItem("email");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      setIsLoading(true);
      await postTweet(email, content);
      setContent("");
      mutate();
    } catch (error) {
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="px-4">
      <div className="border border-gray-700 rounded-md">
        <textarea
          rows={4}
          name="comment"
          id="comment"
          className="block w-full bg-transparent  resize-none ring-none focus:ring-0 focus:outline-none border-none rounded-none border-b-2 border-white text-white placeholder-gray-400"
          placeholder="What are you thinking?"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      </div>
      <div className="flex justify-end">
        <button
          disabled={isLoading || content.length === 0}
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded my-4 flex items-center justify-center gap-3 disabled:opacity-50 disabled:hover:bg-blue-500 disabled:cursor-not-allowed"
        >
          {isLoading && (<Loader />)}
          Send
        </button>
      </div>
    </form>
  );
};

export default TweetForm;
