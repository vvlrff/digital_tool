import cn from "classnames"
import "./Input.css"

export const Input = (props) => {
    const {
        value,
        onChange,
        className,
        title,
        error = false,
        ...otherProps
    } = props

    const mods = {
        "customInput_error": error
    };

    const handleChange = (e) => {
        console.log(123)
        const { value } = e.target
        onChange(value)
    }

    return (
       <div className={cn("customInput", className)}>
            <span className="customInput__title">{title}</span>
            <input
                value={value}
                onChange={handleChange}
                className={cn("customInput__field", mods)}
                {...otherProps}
            />
       </div>
    )
}