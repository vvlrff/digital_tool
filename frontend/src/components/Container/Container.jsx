import cn from "classnames"
import "./Container.css"

export const Container = (props) => {
    const { children, className, ...otherProps } = props

    return (
        <div
            className={cn("container__padding", className)}
            {...otherProps}
        >{children}</div>
    )
}