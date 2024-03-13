import { useState } from "react";
import { Link } from "react-router-dom";

type TweetType = {
  user: string;
  message: string;
  timestamp: string;
  id: string;
};

export const Tweet = ({ tweet }: { tweet: TweetType }) => {
  const words = tweet.message.split(" ");
  // const {data:userReposts, isLoading} = useUserResposts();

  // const isReposted = userReposts?.includes(tweet.id);

  const [isReposted, setIsReposted] = useState(false);
  const [isReposting, setIsReposting] = useState(false);
  const  handleRepost =  () =>{

    setIsReposting(true);
    setTimeout(() => {
      setIsReposted(true);
      setIsReposting(false);
    }, 1000);

  }
  return (
    <div className="p-4 border-t border-gray-700">
      <div className="flex items-center gap-2 pb-4 hover:opacity-90">
        <Link to={`/user/${tweet.user}`} className="flex items-center gap-2">
          <div className="rounded-full w-8 h-8 bg-gradient-to-r from-red-400 to-blue-600" />
          <h3 className="font-semibold text-md">@{tweet?.user}</h3>
        </Link>
        <div className="text-sm mt-2 text-gray-500 ml-auto">
          {tweet?.timestamp &&
            new Date(tweet?.timestamp).toLocaleString().slice(0, -3)}
        </div>
      </div>
      <p className="text-sm pl-10">
        {words.map((w) => {
          if (w.startsWith("#")) {
            return (
              <Link
                className="text-blue-500 hover:text-blue-700"
                to={`/?topic=${w.slice(1)}`}
              >
                {w}{" "}
              </Link>
            );
          }
          return w + " ";
        })}
      </p>
      <div className="flex items-center gap-2 pt-4 text-gray-400">
        <button onClick={handleRepost} className={`ml-auto hover:text-white ${isReposted && "text-blue-500"} ${isReposting && "animate-spin"}`}>
          <RepostIcon />
        </button>
      </div>
    </div>
  );
};

const RepostIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    strokeWidth={1.5}
    stroke="currentColor"
    className="w-6 h-6"
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M19.5 12c0-1.232-.046-2.453-.138-3.662a4.006 4.006 0 0 0-3.7-3.7 48.678 48.678 0 0 0-7.324 0 4.006 4.006 0 0 0-3.7 3.7c-.017.22-.032.441-.046.662M19.5 12l3-3m-3 3-3-3m-12 3c0 1.232.046 2.453.138 3.662a4.006 4.006 0 0 0 3.7 3.7 48.656 48.656 0 0 0 7.324 0 4.006 4.006 0 0 0 3.7-3.7c.017-.22.032-.441.046-.662M4.5 12l3 3m-3-3-3 3"
    />
  </svg>
);
