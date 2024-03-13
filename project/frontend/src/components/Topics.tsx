import { Link } from "react-router-dom"
import { useTopics } from "../hooks/useTopics"
import { Loader } from "./Loader"

export const Topics = () => {
    const { data, error, isLoading } = useTopics()

    if (isLoading) return <Loader />

    if (error) return <div>Error: {error.message}</div>

    return (
        <div>
            <ul>
                {data?.map((topic: any) => (
                    <Link to={`/?topic=${topic}`} key={topic}>
                        <li className="font-semibold" key={topic}>#{topic}</li>
                    </Link>
                ))}
            </ul>
        </div>
    )

}