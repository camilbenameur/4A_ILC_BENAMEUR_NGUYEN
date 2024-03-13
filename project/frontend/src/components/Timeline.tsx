import { GetTweetsOptions, useTweets } from "../hooks/useTweets";
import { Loader } from "./Loader";
import { Tweet } from "./Tweet";

export const Timeline = (options: GetTweetsOptions) => {
  const { data, isLoading } = useTweets(options);

  if (isLoading) {
    return <Loader />;
  }

  return (
    <div className="border-b border-gray-700">
      {data?.map((tweet: any) => (
        <Tweet key={tweet.id} tweet={tweet} />
      ))}
    </div>
  );
};
