import { Timeline } from "../components/Timeline";
import { Topics } from "../components/Topics";
import { Link, useLocation } from "react-router-dom";
import { UserSearch } from "../components/UserSearch";
import TweetForm from "../components/TweetForm";

export const Home = () => {
  const location = useLocation();

  const topic = new URLSearchParams(location.search).get("topic");

  return (
    <div className="min-h-screen">
      <div className="grid grid-cols-3 h-screen">
        <div className="col-span-2">
          {!topic ? (
            <div className="py-8">
              <TweetForm />
            </div>
          ) : (
            <div className="py-5 px-4">
              <h2 className="text-3xl font-semibold pb-4">#{topic}</h2>
              <Link to="/" className="text-blue-500">
                Back to my timeline
              </Link>
            </div>
          )}
          <Timeline topic={topic ?? undefined} />
        </div>
        <div className="border-l border-gray-700">
          <div className="space-y-4 border-b border-gray-700 p-4">
            <h2 className="text-xl font-semibold">
              Search for an user profile
            </h2>
            <UserSearch />
          </div>
          <div className="p-4">
            <h2 className="text-xl font-semibold">Topics</h2>
            <Topics />
          </div>
        </div>
      </div>
    </div>
  );
};
