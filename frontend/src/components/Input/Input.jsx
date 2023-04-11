import cn from "classnames"
import "./Input.css"

export const Input = (props) => {
    const {
        value,
        onChange,
        className,
        error = false,
        ...otherProps
    } = props

    const mods = {
        "customInput_error": error
    };

    const handleChange = (e) => {
        const { value } = e.target
        onChange(value)
    }

    return (
        <input
            value={value}
            onChange={handleChange}
            className={cn("customInput", className, mods)}
            {...otherProps}
        />
    )
}