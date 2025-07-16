import * as Icons from "lucide-react"


type LucideIconName = keyof typeof Icons;

type ButtonIconProps = {
    name: LucideIconName
    text?: string
    size?: number
    color?: string
    className?: string
    onClick: () => void
};

export default function ButtonIcon({ name, size = 24, color = "currentColor", className, onClick, text }: ButtonIconProps) {
    const Icon = Icons[name] as Icons.LucideIcon | undefined
    const handleClick = () => {
        onClick()
    }

    if (!Icon) return null

    return <button className="btn" onClick={handleClick}>
        <Icon size={size} color={color} className={className} />
        {text}
    </button>
}