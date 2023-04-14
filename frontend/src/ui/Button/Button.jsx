import cn from "classnames"

import "./Button.css"

export const Button = (props) => {
    const { children, variant="filled", ...otherProps } = props

    if (!children) return null

    const mods = {
        "button_filled": variant === "filled",
        "button_outlined": variant === "outlined"
    }

    return (
        <button type="button" className={cn("button", mods)} {...otherProps}>{children}</button>
    )
}