import clsx from "clsx"
import ButtonIcon from "../ButtonIcon"

type CardProps = {
    className?: string
    title: string
    snippet: string
    link: string
    image: string
}

export default function Card({ className, title, image, link, snippet }: CardProps) {
    return (
        <div className={clsx("card card-side bg-base-100 shadow-sm", className)}>
            <figure className="flex flex-1">
                <img src={image} alt="Event" />
            </figure>
            <div className="card-body flex flex-2">
                <h2 className="card-title">{title}</h2>
                <p>{snippet}</p>
                <div className="card-actions justify-end">
                    <ButtonIcon name="Heart" onClick={() => { }} />
                </div>
            </div>
        </div>
    )
}