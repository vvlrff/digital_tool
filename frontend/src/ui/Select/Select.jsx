import { useState } from "react";
import cn from "classnames";
import "./Select.css"

export const Select = (props) => {
    const {
        options,
        className,
        title,
        placeholder = "Выберете значение",
        setSelectedOptions,
        ...otherProps
    } = props

    const [isOpen, setIsOpen] = useState(false)

    const listMods = {
        "checkboxGroup__list_open": isOpen
    }

    if (!options) return null

    const handleSelectItem = (e) => {
        const { value } = e.target;
        setSelectedOptions(prev => {
            if (prev.includes(value)) {
                return prev.filter(item => item !== value)
            }
            return [...prev, value]
        })
    }

    return (
        <div className={cn("checkboxGroup", className)} {...otherProps}>
            <span
                className="checkboxGroup__title"
                onClick={() => setIsOpen(prev => !prev)}
            >{title}</span>
            <div className={cn("checkboxGroup__list", listMods)}>
                {options.map(({label, id}) => (
                    <label key={id} className="checkboxGroup__item">
                        <input type="checkbox" value={id} onChange={handleSelectItem} />
                        <span className="checkboxGroup__label">{label}</span>
                    </label>
                ))}
            </div>
        </div>
    )
}