import clsx from "clsx"
import ButtonIcon from "../ButtonIcon"
import { useState, type ChangeEvent } from "react"

type SearchInputProps = {
    className?: string
    onSearch: (value: string) => void
}

export default function SearchInput({ className, onSearch }: SearchInputProps) {
    const [value, setValue] = useState("")

    const handleClick = () => {
        const trimmedValue = value.trim()
        if (trimmedValue) {
            onSearch(trimmedValue)
        }
    }

    const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        setValue(event.target.value)
    }

    return (
        <div className={clsx("flex flex-row items-center", className)}>
            <label className="input">
                <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <g
                        strokeLinejoin="round"
                        strokeLinecap="round"
                        strokeWidth="2.5"
                        fill="none"
                        stroke="currentColor"
                    >
                        <circle cx="11" cy="11" r="8"></circle>
                        <path d="m21 21-4.3-4.3"></path>
                    </g>
                </svg>
                <input type="search" className="grow" placeholder="Search" onChange={(event) => handleChange(event)} />
            </label>
            <ButtonIcon name={"Search"} onClick={handleClick} />
        </div>)
}